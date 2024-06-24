#!/usr/bin/env python3

import os
import sys
import subprocess
import re
import time
from police_style import *
from rep_generation import *
from rep_style import *

input_file = sys.argv[1] if len(sys.argv) > 1 else None

app_attributes = [
    "android:allowBackup=", "android:allowClearUserData=", "android:backupInForeground=",
    "android:debuggable=", "android:networkSecurityConfig=", "android:longClickable=",
    "android:inputType=", "android:usesCleartextTraffic=", "android:sharedUserId=",
    "android:directBootAware=", "android:targetSandboxVersion=", "android:directBootAware=",
    "android:fullBackupContent=", "android:process=", "android:allowTaskReparenting=",
    "android:largeHeap=", "android:extractNativeLibs=", "android:hardwareAccelerated="
]

sdk_attributes = [
    "android:compileSdkVersion=", "android:minSdkVersion=", "android:targetSdkVersion="
]

def check_apktool_installed():
    if not subprocess.call(["which", "apktool"], stdout=subprocess.DEVNULL) == 0:
        install_apktool()
        return False
    return True

def install_apktool():
    print("apktool is not installed.")
    choice = input("Do you want to install apktool? (y/n): ")

    if choice.lower() == "y":
        print("Installing apktool...")
        subprocess.run(["sudo", "apt-get", "update"])
        result = subprocess.run(["sudo", "apt-get", "install", "apktool", "-y"])
        if result.returncode != 0:
            print("Installation of apktool failed.")
            sys.exit(1)
    else:
        print("Installation of apktool cancelled.")
        sys.exit(1)

def decompilation():
    print("\n")
    temp_dir = subprocess.check_output(["mktemp", "-d"]).decode().strip()
    print(f"{Cyan}{bold}Decompiling {input_file} with apktool...{reset}\n")
    result = subprocess.run(["apktool", "-f", "d", input_file])
    subprocess.run(["cp", "-r", input_file.split('.')[0], "./temp"])

    if result.returncode != 0:
        print(f"{Red}Decompilation failed for {input_file}.{reset}")
        sys.exit(1)
    else:
        print(f"\n{Green}{bold}Decompilation successfully completed for {input_file}{reset}")
        time.sleep(5)
        clear_screen()

def verify_f():
    android_manifest = f"{os.path.splitext(input_file)[0]}/AndroidManifest.xml"
    if not os.path.isfile(android_manifest):
        print("The AndroidManifest.xml file does not exist.")
        sys.exit(1)

def check_obfuscated_names(file, count_obfuscated, count_no_obfuscated):
    if not os.path.isfile(file):
        print(f"{Red}{bold}File {file} not found.{reset}")
        return count_obfuscated, count_no_obfuscated

    with open(file, 'r') as f:
        content = f.read()
    
    if re.search(r'\b[a-zA-Z]{1,2}\b', content):
        print(f"{bold}{Green}Obfuscated names found in {reset}{bold}{file}{reset}")
        count_obfuscated += 1
    else:
        print(f"{Red}{bold}No obfuscated names found in {reset}{bold}{file}{reset}")
        count_no_obfuscated += 1
    
    return count_obfuscated, count_no_obfuscated

def Ob_perC(count_obfuscated, count_no_obfuscated):
    total = count_obfuscated + count_no_obfuscated
    if total != 0:
        percentage = (count_obfuscated / total) * 100
    else:
        percentage = 0
    print(f"Application is {percentage:.2f}% obfuscated")

def check_obfuscation_files():
    obfuscation_files = ["mapping.txt", "proguard-rules.pro", "allatori.xml", "dasho.xml"]
        
    print(f"\n{bold}{Yellow}Checking obfuscation configuration files...{reset}\n")
        
    for file in obfuscation_files:
        if os.path.isfile(file):
            print(f"{bold}{Green}Obfuscation configuration file {bold}{reset}{file}{reset} {Green}{bold}found, indicating obfuscation.{reset}")
            return True
        
    print(f"{bold}{Red}No obfuscation configuration files found.{reset}")
    return False

def code_ob(temp_dir, input_file):
    count_obfuscated = 0
    count_no_obfuscated = 0
    base_path = os.path.join(temp_dir, os.path.splitext(input_file)[0])

    # Checking AndroidManifest.xml
    manifest_file = os.path.join(base_path, "AndroidManifest.xml")
    if os.path.isfile(manifest_file):
        print("\nChecking AndroidManifest.xml for obfuscated names...\n")
        count_obfuscated, count_no_obfuscated = check_obfuscated_names(manifest_file, count_obfuscated, count_no_obfuscated)
    else:
        print("AndroidManifest.xml not found.")

    # Checking smali files
    smali_dir = os.path.join(base_path, "smali")
    if os.path.isdir(smali_dir):
        print("\nChecking smali files for obfuscated names...\n")
        for root, _, files in os.walk(smali_dir):
            for file in files:
                if file.endswith(".smali"):
                    smali_file = os.path.join(root, file)
                    count_obfuscated, count_no_obfuscated = check_obfuscated_names(smali_file, count_obfuscated, count_no_obfuscated)
    else:
        print("No smali directory found.")

    # Checking directory and file names in smali for obfuscation
    print("\nChecking directory and file names in smali for obfuscation...\n")
    for root, dirs, files in os.walk(smali_dir):
        for name in dirs + files:
            if re.search(r'/[a-zA-Z]{1,2}/', os.path.join(root, name)):
                print(f"Potential obfuscated path found: {os.path.join(root, name)}")

    print("\nObfuscation check completed.\n")
    return count_obfuscated, count_no_obfuscated

def principal_menu():
    temp_dir = "/path/to/temp"  # Adjust this path as needed
    input_file = "input.apk"    # Adjust this file name as needed
    
    while True:
        choice_menu()
        choice = input("Select option: ")
        print("\n")

        if choice == "1":
            check_obfuscation_files()
            code_ob(temp_dir, input_file)
            press_any_key()
        elif choice == "2":
            return "manifest"
        elif choice == "3":
            print("Generating Report...")
            with open("Report.txt", "w") as report:
                check_obfuscation_files_rep(report)
                code_ob_rep(report)
                attribute_style(report)
                manifest_main_rep(report)
                app_permissions_rep(report)
                exported_component_rep(report)
                check_sdk_rep(report)
                deep_links_rep(report)
            print("\nReport completed")
            press_any_key()
        elif choice.lower() == "q":
            sys.exit(0)
        else:
            print("Invalid value. Choose one of the options between 1 and 3.")
            time.sleep(2)
            clear_screen()

def manifest_menu():
    android_manifest = f"{os.path.splitext(input_file)[0]}/AndroidManifest.xml"
    while True:
        choice_manifest()
        choice = input("Select option: ")
        print("\n")

        if choice == "1":
            manifest_main(app_attributes, android_manifest)
            press_any_key()
        elif choice == "2":
            app_permissions(input_file)
            press_any_key()
        elif choice == "3":
            exported_component(android_manifest)
            press_any_key()
        elif choice == "4":
            check_sdk(sdk_attributes, android_manifest)
            press_any_key()
        elif choice == "5":
            deep_links(android_manifest)
            press_any_key()
        elif choice == "6":
            return "main"
        elif choice.lower() == "q":
            sys.exit(0)
        else:
            print("Invalid value. Choose one of the options between 1 and 6.")
            time.sleep(2)
            clear_screen()


def simulate_long_task():
    time.sleep(5)

def loading_animation():
    # Implement a loading animation here
    pass

def check_attribute(attribute, android_manifest):
    with open(android_manifest, 'r') as file:
        content = file.read()
    result = re.search(f'{attribute}"([^"]*)', content)
    
    if result:
        value = result.group(1)
        if value == "true":
            print_true(attribute)
        elif value == "false":
            print_false(attribute)
        else:
            print_found(attribute, value)
    else:
        print_not_found(attribute)

def manifest_main(app_attributes, android_manifest):
    simulate_long_task()
    loading_animation()
    
    print(f"{Yellow}{bold}Checking for Application Attributes...\n{reset}")
    for attribute in app_attributes:
        check_attribute(attribute, android_manifest)
    
    simulate_long_task()

def app_permissions(input_file):
    simulate_long_task()
    loading_animation()
    
    print(f"{Yellow}{bold}Checking for Permission...\n{reset}")
    manifest_path = f"{input_file.rsplit('.', 1)[0]}/AndroidManifest.xml"
    
    with open(manifest_path, 'r') as file:
        content = file.read()
    
    permissions = re.findall(r'android:name="(android\.permission\.[^"]*)"', content)
    for permission in permissions:
        print(f"{Green}{permission}{reset}")
    
    print("\n")

def exported_component(android_manifest):
    simulate_long_task()
    loading_animation()
    
    print(f"{Yellow}{bold}Checking for Exported Component...\n{reset}")
    with open(android_manifest, 'r') as file:
        for line in file:
            if 'android:exported="' in line:
                print(line.strip())
                print()

def check_sdk(sdk_attributes, android_manifest):
    simulate_long_task()
    loading_animation()
    
    print(f"{Yellow}{bold}Checking for SDK version...\n{reset}")
    with open(android_manifest, 'r') as file:
        content = file.read()
    
    result = re.search(f'{sdk_attributes[0]}"([^"]*)', content)
    if result:
        value = result.group(1)
        for attribute in sdk_attributes:
            print_found(attribute, value)

def deep_links(android_manifest):
    simulate_long_task()
    loading_animation()
    
    print(f"{Yellow}{bold}Checking for DeepLinks...\n{reset}")
    with open(android_manifest, 'r') as file:
        content = file.read()
    
    intent_filters = re.findall(r'<intent-filter>(.*?)</intent-filter>', content, re.DOTALL)
    for intent_filter in intent_filters:
        scheme = re.search(r'android:scheme="([^"]*)"', intent_filter)
        host = re.search(r'android:host="([^"]*)"', intent_filter)
        if scheme and host:
            print(f"{Green}Scheme: {scheme.group(1)}, Host: {host.group(1)}{reset}")

def press_any_key():
    print("\n")
    input("Press any key to continue...")
    print("")
    time.sleep(1)
    subprocess.call('clear' if os.name == 'posix' else 'cls', shell=True)

if __name__ == "__main__":
    if not input_file:
        print(f"Usage: {sys.argv[0]} input_file")
        sys.exit(1)

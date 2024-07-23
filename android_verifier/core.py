#!/usr/bin/env python3



import os

import sys

import subprocess

import re

import time

from pyaxmlparser import APK

from android_verifier.police_style import clear_screen, load_animation, decomp_animation, simulate_long_task

from android_verifier.rep_generation import *

from android_verifier.rep_style import *



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



temp_dir=""

choice=""

count_obfuscated=0

count_no_obfuscated=0

total=0



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

    print(f"{Cyan}{bold}Decompiling {input_file} with apktool...{reset}\n")

    result = subprocess.run(["apktool", "-f", "d", input_file])

    if result.returncode != 0:

        print(f"{Red}Decompilation failed for {input_file}.{reset}")

        sys.exit(1)

    else:

        print(f"\n{Green}{bold}Decompilation successfully completed for {input_file}{reset}")

        time.sleep(5)

        clear_screen()


def extract():

    subprocess.run(["7z", "x", input_file, "-otemp_dir"])




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

        #print(count_obfuscated)

    else:

        print(f"{Red}{bold}No obfuscated names found in {reset}{bold}{file}{reset}")

        count_no_obfuscated += 1

        #print(count_no_obfuscated)

    

    return count_obfuscated, count_no_obfuscated



def Ob_perC(count_obfuscated, count_no_obfuscated):

    count_obfuscated, count_no_obfuscated = code_ob(input_file)

    total = count_obfuscated + count_no_obfuscated

    if total != 0:

        percentage = (count_obfuscated / total) * 100

    else:

        percentage = 5

    print(f"{bold}{Yellow}Application is {percentage:.2f}% obfuscated{reset}")



def check_obfuscation_files():

    obfuscation_files = ["mapping.txt", "proguard-rules.pro", "allatori.xml", "dasho.xml"]

        

    print(f"\n{bold}{Yellow}Checking obfuscation configuration files...{reset}\n")

        

    for file in obfuscation_files:

        if os.path.isfile(file):

            print(f"{bold}{Green}Obfuscation configuration file {bold}{reset}{file}{reset} {Green}{bold}found, indicating obfuscation.{reset}")

            return True

        

    print(f"{bold}{Red}No obfuscation configuration files found.{reset}")

    return False



def code_ob(input_file):

    count_obfuscated = 0

    count_no_obfuscated = 0

    #base_path = os.path.join(temp_dir, os.path.splitext(input_file)[0])



    # Checking AndroidManifest.xml

    manifest_file = os.path.join(os.path.splitext(input_file)[0], "AndroidManifest.xml")

    if os.path.isfile(manifest_file):

        print(f"\n{bold}{Yellow}Checking AndroidManifest.xml for obfuscated names...{reset}\n")

        count_obfuscated, count_no_obfuscated = check_obfuscated_names(manifest_file, count_obfuscated, count_no_obfuscated)

    else:

        print("AndroidManifest.xml not found.")



    # Checking smali files

    smali_dir = os.path.join(os.path.splitext(input_file)[0], "smali")

    if os.path.isdir(smali_dir):

        print(f"\n{bold}{Yellow}Checking smali files for obfuscated names...{bold}\n")

        for root, _, files in os.walk(smali_dir):

            for file in files:

                if file.endswith(".smali"):

                    smali_file = os.path.join(root, file)

                    count_obfuscated, count_no_obfuscated = check_obfuscated_names(smali_file, count_obfuscated, count_no_obfuscated)

    else:

        print("{bold}No smali directory found.{bold}")



    # Checking directory and file names in smali for obfuscation

    print(f"\n{bold}{Yellow}Checking directory and file names in smali for obfuscation...{reset}\n")

    for root, dirs, files in os.walk(smali_dir):

        for name in dirs + files:

            if re.search(r'/[a-zA-Z]{1,2}/', os.path.join(root, name)):

                print(f"{Red}{bold}Potential obfuscated path found:{reset} {os.path.join(root, name)}")



    print(f"\n{bold}{Cyan}Obfuscation check completed.{reset}\n")

    return count_obfuscated, count_no_obfuscated



def principal_menu():


    while True:
        
        clear_screen()

        choice_menu()

        choice = input("Select option: ")

        print("\n")

        if choice == "1":

            struct_apk()

            press_any_key()

        elif choice == "2":

            load_animation()

            check_obfuscation_files()

            code_ob(input_file)

            Ob_perC(count_obfuscated, count_no_obfuscated)

            press_any_key()

        elif choice == "3":

            return "manifest"

        elif choice == "4":

            return "Meta"

        elif choice == "5":

            rep_animation()

            with open("/tmp/report.txt", "w") as report:

                check_obfuscation_files_rep(report)

                code_ob_rep(temp_dir, input_file, report)

                android_manifest = os.path.join(temp_dir, f"{os.path.splitext(input_file)[0]}", "AndroidManifest.xml")

                attribute_style(report)

                manifest_main_rep(app_attributes, android_manifest, report)

                permission_style(report)

                app_permissions_rep(input_file, report)

                exported_style(report)

                exported_component_rep(android_manifest, report)

                sdk_style(report)

                check_sdk_rep(sdk_attributes, android_manifest, report)

                deep_links_style(report)

                deep_links_rep(android_manifest, report)

            print(f"{Purple}**Report saved into{reset} {Green}'/tmp/report.txt'.{reset}")

            press_any_key()

        elif choice.lower() == "q":

            current_menu ='q'

            sys.exit(0)

        else:

            print(f"{bold}{Red}Invalid value. Choose one of the options between 1 and 5 or q.{reset}")

            time.sleep(2)

            clear_screen()



def manifest_menu():

    android_manifest = f"{os.path.splitext(input_file)[0]}/AndroidManifest.xml"

    while True:
    
        clear_screen()

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

            current_menu = 'q'

            sys.exit(0)

        else:

            print("Invalid value. Choose one of the options between 1 and 6 or q.")

            time.sleep(2)

            clear_screen()



def meta_menu():

    file = os.path.join("temp_dir", "META-INF" ,"CERT.RSA")

    while True:

        clear_screen()

        choice_meta()

        choice = input("Select option: ")

        print("\n")



        if choice == "1":

            load_animation()

            check_MF(file)

            press_any_key()

        elif choice == "2":

            load_animation()

            check_CSF(file)

            press_any_key()


        elif choice == "3":

            load_animation()

            check_CRSA(file)  

            press_any_key()      

        elif choice == "4":

            return "main"

        elif choice.lower() == "q":

            current_menu = 'q'

            sys.exit(0)

        else:

            print("Invalid value. Choose one of the options between 1 and 4 or q.")

            time.sleep(2)

            clear_screen()
        


def struct_apk():

    # Create an APK object
    apk = APK(input_file)

    # Display the APK information
    apk.show()




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

    load_animation()



    

    print(f"{Yellow}{bold}Checking for Application Attributes...\n{reset}")

    for attribute in app_attributes:

        check_attribute(attribute, android_manifest)

    



def app_permissions(input_file):

    load_animation()

    

    print(f"{Yellow}{bold}Checking for Permission...\n{reset}")

    manifest_path = f"{input_file.rsplit('.', 1)[0]}/AndroidManifest.xml"

    

    with open(manifest_path, 'r') as file:

        content = file.read()

    

    permissions = re.findall(r'android:name="(android\.permission\.[^"]*)"', content)

    for permission in permissions:

        print(f"{Green}{permission}{reset}")

    

    print("\n")



def exported_component(android_manifest):

    load_animation()

    

    print(f"{Yellow}{bold}Checking for Exported Component...\n{reset}")

    with open(android_manifest, 'r') as file:

        for line in file:

            if 'android:exported="' in line:

                print(line.strip())

                print()



def check_sdk(sdk_attributes, android_manifest):

    load_animation()

    

    print(f"{Yellow}{bold}Checking for SDK version...\n{reset}")

    with open(android_manifest, 'r') as file:

        content = file.read()

    

    result = re.search(f'{sdk_attributes[0]}"([^"]*)', content)

    if result:

        value = result.group(1)

        for attribute in sdk_attributes:

            print_found(attribute, value)



def deep_links(android_manifest):

    load_animation()

    

    print(f"{Yellow}{bold}Checking for DeepLinks...\n{reset}")

    with open(android_manifest, 'r') as file:

        content = file.read()

    

    intent_filters = re.findall(r'<intent-filter>(.*?)</intent-filter>', content, re.DOTALL)

    for intent_filter in intent_filters:

        scheme = re.search(r'android:scheme="([^"]*)"', intent_filter)

        host = re.search(r'android:host="([^"]*)"', intent_filter)

        if scheme and host:

            print(f"{Green}Scheme: {scheme.group(1)}, Host: {host.group(1)}{reset}")



def check_MF(file):

    manifest_mf_path = os.path.join("temp_dir", "META-INF" ,"MANIFEST.MF")

    with open(manifest_mf_path, 'r') as f:

        content = f.read()

    print(content)


def check_CSF(file):

    cert_sf_path = os.path.join("temp_dir", "META-INF" ,"CERT.SF")

    with open(cert_sf_path, 'r') as f:

        content = f.read()

    print(content)



def check_CRSA(file):

    cert_rsa_path = os.path.join("temp_dir", "META-INF" ,"CERT.RSA")

    subprocess.run(["keytool", "-printcert", "-file", cert_rsa_path])



def press_any_key():

    print("\n")

    input("Press any key to continue...")

    print("")

    time.sleep(1)

    subprocess.call('clear' if os.name == 'posix' else 'cls', shell=True)


def remove_directory(dir_path):

    if os.path.exists(dir_path):

        shutil.rmtree(dir_path)

        print(f"Deleted directory: {dir_path}")

    else:

        print(f"Directory does not exist: {dir_path}")


def main():

    if len(sys.argv) < 2:

        print(f"Usage: {sys.argv[0]} path_to_apk_file")
        
        sys.exit(1)
    
    input_file = sys.argv[1]

    clear_screen()

    simulate_long_task()

    check_apktool_installed()

    decomp_animation()

    decompilation()

    extract()

    verify_f()



    current_menu = "main"


    try:

        while True:

            if current_menu == "main":

                current_menu = principal_menu()

            elif current_menu == "manifest":

                current_menu = manifest_menu()
            
            elif current_menu == "Meta":

                current_menu = meta_menu()

            elif current_menu == "q":

                break

    except KeyboardInterrupt:
    
        pass
    
    finally:

        directories = ["android_verifier/__pycache__", "InsecureShop", "temp_dir"]

        for dir_path in directories:
            remove_directory(dir_path)

        print("Cleanup complete.")



if __name__ == "__main__":

    if not input_file:

        print(f"Usage: {sys.argv[0]} input_file")

        sys.exit(1)

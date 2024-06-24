import os
import re
import time
import subprocess
from police_style import *

def check_obfuscated_names_rep(file):
    with open(file, 'r') as f:
        content = f.read()
        if re.search(r'\b[a-zA-Z]{1,2}\b', content):
            print(f"Obfuscated names found in {file}")
            return True
        else:
            print(f"No obfuscated names found in {file}")
            return False

def check_obfuscation_files_rep(report_file):
    filesob_style(report_file)
    obfuscation_files = ["mapping.txt", "proguard-rules.pro", "allatori.xml", "dasho.xml"]
    
    for file in obfuscation_files:
        if os.path.isfile(file):
            print(f"Obfuscation configuration file {file} found, indicating obfuscation.", file=report_file)
            return True
    
    print("\nNo obfuscation configuration files found.\n", file=report_file)
    return False

def code_ob_rep(temp_dir, input_file):
    manifest_file = os.path.join(temp_dir, f"{os.path.splitext(input_file)[0]}", "AndroidManifest.xml")
    if os.path.isfile(manifest_file):
        manifestob_style()
        check_obfuscated_names_rep(manifest_file)
    else:
        print("AndroidManifest.xml not found.")

    smali_dir = os.path.join(temp_dir, f"{os.path.splitext(input_file)[0]}", "smali")
    if os.path.isdir(smali_dir):
        smaliob_style()
        for root, dirs, files in os.walk(smali_dir):
            for file in files:
                if file.endswith('.smali'):
                    check_obfuscated_names_rep(os.path.join(root, file))
    else:
        print("No smali directory found.")

    file_foldob_style()
    for root, dirs, files in os.walk(smali_dir):
        for name in dirs + files:
            if re.search(r'/[a-zA-Z]{1,2}/', os.path.join(root, name)):
                print(f"Potential obfuscated path found: {os.path.join(root, name)}")

    print("\nObfuscation check completed.\n")

def manifest_main_rep(app_attributes, android_manifest):
    def check_attribute(attribute):
        with open(android_manifest, 'r') as f:
            content = f.read()
        result = re.search(f'{attribute}"([^"]*)', content)
        
        if result:
            value = result.group(1)
            if value == "true":
                print_true_rep(attribute)
            elif value == "false":
                print_false_rep(attribute)
            else:
                print_found_rep(attribute, value)
        else:
            print_not_found_rep(attribute)

    for attribute in app_attributes:
        check_attribute(attribute)

def app_permissions_rep(input_file):
    permission_style()
    manifest_path = f"{os.path.splitext(input_file)[0]}/AndroidManifest.xml"
    with open(manifest_path, 'r') as f:
        content = f.read()
    permissions = re.findall(r'android:name="(android\.permission\.[^"]*)"', content)
    for permission in permissions:
        print(permission)
    print("\n")

def exported_component_rep(android_manifest):
    exported_style()
    with open(android_manifest, 'r') as f:
        content = f.read()
    exported_components = re.findall(r'android:exported="[^"]+"', content)
    for component in exported_components:
        print(component)
        print()

def check_sdk_rep(sdk_attributes, android_manifest):
    sdk_style()
    with open(android_manifest, 'r') as f:
        content = f.read()
    result = re.search(f'{sdk_attributes[0]}"([^"]*)', content)
    if result:
        value = result.group(1)
        for attribute in sdk_attributes:
            print_found_rep(attribute, value)

def deep_links_rep(android_manifest):
    deep_links_style()
    with open(android_manifest, 'r') as f:
        content = f.read()
    intent_filters = re.findall(r'<intent-filter>(.*?)</intent-filter>', content, re.DOTALL)
    for intent_filter in intent_filters:
        scheme = re.search(r'android:scheme="([^"]*)"', intent_filter)
        host = re.search(r'android:host="([^"]*)"', intent_filter)
        if scheme and host:
            print(f"Scheme: {scheme.group(1)}, Host: {host.group(1)}")

def simulate_long_task():
    time.sleep(5)

def press_any_key():
    print("\n")
    input("Press any key to continue...")
    print("")
    time.sleep(1)
    subprocess.call('clear' if os.name == 'posix' else 'cls', shell=True)

# You'll need to implement the style functions (filesob_style, manifestob_style, etc.)
# and the print functions (print_true_rep, print_false_rep, etc.) from the police_style module

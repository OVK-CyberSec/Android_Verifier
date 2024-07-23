import os

import re

import time

import subprocess

from pyaxmlparser import APK

from android_verifier.police_style import *

from android_verifier.rep_style import *

from android_verifier.core import *




def Ob_perC(count_obfuscated, count_no_obfuscated, report):

    count_obfuscated, count_no_obfuscated = code_ob(temp_dir, input_file)

    total = count_obfuscated + count_no_obfuscated

    if total != 0:

        percentage = (count_obfuscated / total) * 100

    else:

        percentage = 5

    print(f"{bold}{Yellow}Application is {percentage:.2f}% obfuscated{reset}", file=report)


def check_obfuscated_names_rep(file, report):

    with open(file, 'r') as f:

        content = f.read()

        if re.search(r'\b[a-zA-Z]{1,2}\b', content):

            print(f"- Obfuscated names found in {file}", file=report)

            return True

        else:

            print(f"- No obfuscated names found in {file}", file=report)

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



def code_ob_rep(temp_dir, input_file, report):

    manifest_file = os.path.join(temp_dir, f"{os.path.splitext(input_file)[0]}", "AndroidManifest.xml")

    if os.path.isfile(manifest_file):

        manifestob_style(report)

        check_obfuscated_names_rep(manifest_file, report)

    else:

        print("AndroidManifest.xml not found.", file=report)



    smali_dir = os.path.join(temp_dir, f"{os.path.splitext(input_file)[0]}", "smali")

    if os.path.isdir(smali_dir):

        smaliob_style(report)

        for root, dirs, files in os.walk(smali_dir):

            for file in files:

                if file.endswith('.smali'):

                    check_obfuscated_names_rep(os.path.join(root, file), report)

    else:

        print("No smali directory found.", file=report)



    fF_ob_style(report)

    for root, dirs, files in os.walk(smali_dir):

        for name in dirs + files:

            if re.search(r'/[a-zA-Z]{1,2}/', os.path.join(root, name)):

                print(f"- Potential obfuscated path found: {os.path.join(root, name)}", file=report)



def overview_rep(input_file, report):

    apk = APK(input_file)
    
    print(apk.show(), file=report)



def manifest_main_rep(app_attributes, android_manifest, report):

    def check_attribute(attribute):

        with open(android_manifest, 'r') as f:

            content = f.read()

        result = re.search(f'{attribute}"([^"]*)', content)

        

        if result:

            value = result.group(1)

            if value == "true":

                print_true_rep(attribute, report)

            elif value == "false":

                print_false_rep(attribute, report)

            else:

                print_found_rep(attribute, value, report)

        else:

            print_not_found_rep(attribute, report)



    for attribute in app_attributes:

        check_attribute(attribute)



def app_permissions_rep(input_file, report):

    manifest_path = f"{os.path.splitext(input_file)[0]}/AndroidManifest.xml"

    with open(manifest_path, 'r') as f:

        content = f.read()

    permissions = re.findall(r'android:name="(android\.permission\.[^"]*)"', content)

    for permission in permissions:

        print(permission, file=report)

    print("\n")



def exported_component_rep(android_manifest, report):

    with open(android_manifest, 'r') as f:

        for line in f:

            if 'android:exported="' in line:

                print(line.strip(), file=report)

                print()



def check_sdk_rep(sdk_attributes, android_manifest, report):


    with open(android_manifest, 'r') as f:

        content = f.read()


        result = re.search(f'{sdk_attributes[0]}"([^"]*)', content)

        if result:

            value = result.group(1)

            for attribute in sdk_attributes:

                print_found_rep(attribute, value, report)



def deep_links_rep(android_manifest, report):

    with open(android_manifest, 'r') as f:

        content = f.read()

    intent_filters = re.findall(r'<intent-filter>(.*?)</intent-filter>', content, re.DOTALL)

    for intent_filter in intent_filters:

        scheme = re.search(r'android:scheme="([^"]*)"', intent_filter)

        host = re.search(r'android:host="([^"]*)"', intent_filter)

        if scheme and host:

            print(f"Scheme: {scheme.group(1)}, Host: {host.group(1)}", file=report)



def check_MF_rep(manifest_mf_path, report):

    manifest_mf_path = os.path.join("temp_dir", "META-INF" ,"MANIFEST.MF")

    with open(manifest_mf_path, 'r') as f:

        content = f.read()

    print(content, file=report)


def check_CSF_rep(cert_sf_path, report):

    cert_sf_path = os.path.join("temp_dir", "META-INF" ,"CERT.SF")

    with open(cert_sf_path, 'r') as f:

        content = f.read()

    print(content, file=report)


def check_CRSA_rep(cert_rsa_path, report):

    cert_rsa_path = os.path.join("temp_dir", "META-INF" ,"CERT.RSA")

    result = subprocess.run(["keytool", "-printcert", "-file", cert_rsa_path], capture_output=True, text=True)

    print(result.stdout, file=report)



def simulate_long_task():

    time.sleep(5)



def press_any_key():

    print("\nPress any key to continue...", end='', flush=True)

    input()

    print("")

    time.sleep(1)

    subprocess.call('clear' if os.name == 'posix' else 'cls', shell=True)


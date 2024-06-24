#!/usr/bin/env python3

def print_false_rep(attribute, report):
    print(f"{attribute} is set to \"False\"\n".replace('=', ''), file=report)

def print_true_rep(attribute, report):
    print(f"{attribute} is set to \"True\"\n".replace('=', ''), file=report)

def print_not_found_rep(attribute, report):
    print(f"{attribute} Takes \"Default Value\" \n".replace('=', ''), file=report)

def print_found_rep(attribute, value, report):
    print(f"{attribute} is set to {value}\n".replace('=', ''), file=report)

def print_red_rep(attribute, report):
    print(f"{attribute} is set to False\n".replace('=', ''), file=report)

def print_green_rep(attribute, report):
    print(f"{attribute} is set to True\n".replace('=', ''), file=report)

def attribute_style(report):
    print(" =============================================================================", file=report)
    print(" ================= Checking for Application Attributes... ====================", file=report)
    print(" =============================================================================", file=report)

def permission_style(report):
    print(" =================================================================", file=report)
    print(" ================= Checking for Permission... ====================", file=report)
    print(" =================================================================", file=report)

def exported_style(report):
    print(" =================================================================", file=report)
    print(" =========== Checking for Exported Component... ==================", file=report)
    print(" =================================================================", file=report)

def sdk_style(report):
    print(" =================================================================", file=report)
    print(" ============== Checking for SDK version... ======================", file=report)
    print(" =================================================================", file=report)

def deep_links_style(report):
    print(" =================================================================", file=report)
    print(" ================ Checking for DeepLinks... ======================", file=report)
    print(" =================================================================", file=report)

def manifestob_style(report):
    print(" ============================================================================================", file=report)
    print(" ================ Checking AndroidManifest.xml for obfuscated names... ======================", file=report)
    print(" ============================================================================================", file=report)

def smaliob_style(report):
    print(" ============================================================================================", file=report)
    print(" ===================== Checking smali files for obfuscated names... =========================", file=report)

#!/usr/bin/env python3



import os

import sys

import time

from police_style import clear_screen, loading_animation, simulate_long_task

from functions import check_apktool_installed, decompilation, verify_f, principal_menu, manifest_menu



def main():

    clear_screen()

    simulate_long_task()

    loading_animation()



    check_apktool_installed()

    decompilation()

    verify_f()



    current_menu = "main"



    while True:

        if current_menu == "main":

            current_menu = principal_menu()

        elif current_menu == "manifest":

            current_menu = manifest_menu()



if __name__ == "__main__":

    if len(sys.argv) < 2:

        print(f"Usage: {sys.argv[0]} path_to_apk_file")

        sys.exit(1)

    

    input_file = sys.argv[1]

    main()

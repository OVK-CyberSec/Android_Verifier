#!/usr/bin/env python3

import os
import shutil
import time

Red = "\033[31m"
Green = "\033[32m"
Yellow = "\033[33m"
Cyan = "\033[36m"
bold = "\033[1m"
reset = "\033[0m"

def print_false(attribute):
    print(f"{reset}{bold}{Yellow}{attribute}{reset}{Cyan} is set to {reset}{bold}{Red}\"False\"{reset}\n".replace('=', ''))

def print_true(attribute):
    print(f"{bold}{Yellow}{attribute}{reset}{Cyan} is set to {reset}{bold}{Green}\"True\"{reset}\n".replace('=', ''))

def print_not_found(attribute):
    print(f"{reset}{bold}{Yellow}{attribute}{reset}{Cyan} Takes{bold} \"Default Value\" {reset}\n".replace('=', ''))

def print_found(attribute, value):
    print(f"{reset}{bold}{Yellow}{attribute}{reset}{Cyan} is set to {reset}{Yellow}{bold}{value}{reset}\n".replace('=', ''))

def center_text(text):
    width = shutil.get_terminal_size().columns
    padding = (width - len(text)) // 2
    return " " * padding + text + " " * padding

def loading_animation():
    import itertools
    import time
    import sys

    spinner = itertools.cycle(['-', '\\', '|', '/'])
    loading_text = "Loading"

    for _ in range(10):  # Adjust the number of iterations as needed
        sys.stdout.write(f"\r{center_text(f'[{next(spinner)}] {loading_text}')}")
        sys.stdout.flush()
        time.sleep(0.1)

    sys.stdout.write('\r' + ' ' * shutil.get_terminal_size().columns)
    sys.stdout.flush()

def simulate_long_task():
    time.sleep(5)  # Simulates a task that takes 5 seconds

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def choice_manifest():
    print(f"{Cyan}{bold}Menu :{reset}")
    print("\n")
    print(f"{bold}{Red} ====================================================================================={reset}")
    print(f"{bold}{Red}| {Green}{bold}Options{reset}                {Red}|{reset}              {Green}{bold}Description{reset}                                   {Red}|{reset}")
    print(f"{bold}{Red} ====================================================================================={reset}")
    print(f"{bold}{Red}| {Green}{bold}1{reset}                     {Red}|{reset}       {Green}{bold}Checking for Application Attributes...{reset}                {Red}|{reset}")
    print(f"{bold}{Red}| {Green}{bold}2{reset}                     {Red}|{reset}       {Green}{bold}Checking for Permission...{reset}                            {Red}|{reset}")
    print(f"{bold}{Red}| {Green}{bold}3{reset}                     {Red}|{reset}       {Green}{bold}Checking for Exported Component...{reset}                    {Red}|{reset}")
    print(f"{bold}{Red}| {Green}{bold}4{reset}                     {Red}|{reset}       {Green}{bold}Checking for SDK version...{reset}                           {Red}|{reset}")
    print(f"{bold}{Red}| {Green}{bold}5{reset}                     {Red}|{reset}       {Green}{bold}Checking for DeepLinks...{reset}                             {Red}|{reset}")
    print(f"{bold}{Red}| {Green}{bold}6{reset}                     {Red}|{reset}       {Green}{bold}Returning to previous menu...{reset}                         {Red}|{reset}")
    print(f"{bold}{Red}| {Green}{bold}q{reset}                     {Red}|{reset}       {Green}{bold}Quit{reset}                                                  {Red}|{reset}")
    print(f"{bold}{Red} ====================================================================================={reset}")
    print("\n")

def choice_menu():
    print("\n")
    print(f"{Cyan}{bold}Menu :{reset}")
    print("\n")
    print(f"{bold}{Red} ============================================================================={reset}")
    print(f"{bold}{Red}| {Green}{bold}Options{reset}               {Red}|{reset}             {Green}{bold}Description{reset}                             {Red}|{reset}")
    print(f"{bold}{Red} ============================================================================={reset}")
    print(f"{bold}{Red}| {Green}{bold}1{reset}                     {Red}|{reset}       {Green}{bold}Checking for Code Obfuscation...{reset}              {Red}|{reset}")
    print(f"{bold}{Red}| {Green}{bold}2{reset}                     {Red}|{reset}       {Green}{bold}Checking for AndroidManifest File...{reset}          {Red}|{reset}")
    print(f"{bold}{Red}| {Green}{bold}3{reset}                     {Red}|{reset}       {Green}{bold}Generate Full Report...{reset}                       {Red}|{reset}")
    print(f"{bold}{Red}| {Green}{bold}q{reset}                     {Red}|{reset}       {Green}{bold}Quit{reset}                                          {Red}|{reset}")
    print(f"{bold}{Red} ============================================================================={reset}")
    print("\n")
    print("\n")

if __name__ == "__main__":
    # This file is meant to be imported, not run directly
    pass

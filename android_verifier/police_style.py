#!/usr/bin/env python3



import os

import shutil

import time

import itertools

import sys

Red = "\033[31m"

Green = "\033[32m"

Purple = "\033[35m"

Yellow = "\033[33m"

Cyan = "\033[36m"

bold = "\033[1m"

reset = "\033[0m"

HEADER = '\033[95m'

VERSION = "1.0.0"


def print_false(attribute):

    print(f"{bold}{Yellow}{attribute}{reset}{Cyan} is set to {reset}{bold}{Red}\"False\"{reset}\n".replace('=', ''))



def print_true(attribute):

    print(f"{bold}{Yellow}{attribute}{reset}{Cyan} is set to {reset}{bold}{Green}\"True\"{reset}\n".replace('=', ''))



def print_not_found(attribute):

    print(f"{bold}{Yellow}{attribute}{reset}{Cyan} Takes{bold} \"Default Value\" {reset}\n".replace('=', ''))



def print_found(attribute, value):

    print(f"{bold}{Yellow}{attribute}{reset}{Cyan} is set to {reset}{Yellow}{bold}{value}{reset}\n".replace('=', ''))



def center_text(text):

    width = shutil.get_terminal_size().columns

    padding = (width - len(text)) // 2

    return " " * padding + text + " " * padding



def load_animation():

    spinner = itertools.cycle(['-', '\\', '|', '/'])

    loading_text = "Loading"

    for _ in range(10):  # Adjust the number of iterations as needed

        sys.stdout.write(f"\r{center_text(f'[{next(spinner)}] {loading_text}')}")

        sys.stdout.flush()

        time.sleep(0.3)

    sys.stdout.write('\r' + ' ' * shutil.get_terminal_size().columns)

    sys.stdout.flush()


def decomp_animation():

    print('\n')

    spinner = itertools.cycle(['-', '\\', '|', '/'])

    loading_text = "Decompilation in progress ..."

    for _ in range(10):  # Adjust the number of iterations as needed

        sys.stdout.write(f"\r{center_text(f'[{next(spinner)}] {loading_text}')}")

        sys.stdout.flush()

        time.sleep(0.3)

    sys.stdout.write('\r' + ' ' * shutil.get_terminal_size().columns)

    sys.stdout.flush()


def rep_animation():

    spinner = itertools.cycle(['-', '\\', '|', '/'])

    loading_text = "Generating Report ..."

    for _ in range(10):  # Adjust the number of iterations as needed

        sys.stdout.write(f"\r{center_text(f'[{next(spinner)}] {loading_text}')}")

        sys.stdout.flush()

        time.sleep(0.3)

    sys.stdout.write('\r' + ' ' * shutil.get_terminal_size().columns)

    sys.stdout.flush()


def simulate_long_task():

    time.sleep(3)  # Simulates a task that takes 5 seconds



def clear_screen():

    os.system('cls' if os.name == 'nt' else 'clear')



def choice_manifest():

    print(f"{Cyan}{bold}Menu :{reset}")

    print("\n")

    print(f"{bold}{Red} ==============================================================={reset}")

    print(f"{bold}{Red}| {Green}{bold}Options{reset}   {Red}|{reset}              {Green}{bold}Description{reset}                          {Red}|{reset}")

    print(f"{bold}{Red} ==============================================================={reset}")

    print(f"{bold}{Red}| {Green}{bold}1{reset}         {Red}|{reset}       {Green}{bold}Checking for Application Attributes...{reset}      {Red}|{reset}")

    print(f"{bold}{Red}| {Green}{bold}2{reset}         {Red}|{reset}       {Green}{bold}Checking for Permission...{reset}                  {Red}|{reset}")

    print(f"{bold}{Red}| {Green}{bold}3{reset}         {Red}|{reset}       {Green}{bold}Checking for Exported Component...{reset}          {Red}|{reset}")

    print(f"{bold}{Red}| {Green}{bold}4{reset}         {Red}|{reset}       {Green}{bold}Checking for SDK version...{reset}                 {Red}|{reset}")

    print(f"{bold}{Red}| {Green}{bold}5{reset}         {Red}|{reset}       {Green}{bold}Checking for DeepLinks...{reset}                   {Red}|{reset}")

    print(f"{bold}{Red}| {Green}{bold}6{reset}         {Red}|{reset}       {Green}{bold}Returning to previous menu...{reset}               {Red}|{reset}")

    print(f"{bold}{Red}| {Green}{bold}q{reset}         {Red}|{reset}       {Green}{bold}Quit{reset}                                        {Red}|{reset}")

    print(f"{bold}{Red} ==============================================================={reset}")

    print("\n")



def choice_meta():

    print(f"{Cyan}{bold}Menu :{reset}")

    print("\n")

    print(f"{bold}{Red} ================================================================={reset}")

    print(f"{bold}{Red}| {Green}{bold}Options{reset}  {Red}|{reset}          {Green}{bold}Description{reset}                                {Red}|{reset}")

    print(f"{bold}{Red} ================================================================={reset}")

    print(f"{bold}{Red}| {Green}{bold}1{reset}        {Red}|{reset}       {Green}{bold}Checking for MANIFEST.MF...{reset}                   {Red}|{reset}")

    print(f"{bold}{Red}| {Green}{bold}2{reset}        {Red}|{reset}       {Green}{bold}Checking for CERT.SF...{reset}                       {Red}|{reset}")

    print(f"{bold}{Red}| {Green}{bold}3{reset}        {Red}|{reset}       {Green}{bold}Checking for CERT.RSA...{reset}                      {Red}|{reset}")

    print(f"{bold}{Red}| {Green}{bold}4{reset}        {Red}|{reset}       {Green}{bold}Returning to previous menu...{reset}                 {Red}|{reset}")

    print(f"{bold}{Red}| {Green}{bold}q{reset}        {Red}|{reset}       {Green}{bold}Quit{reset}                                          {Red}|{reset}")

    print(f"{bold}{Red} ================================================================={reset}")

    print("\n")




def choice_menu():


    print(f"{Cyan}{bold}Menu :{reset}")

    print("\n")

    print(f"{bold}{Red} ==========================================================================={reset}")

    print(f"{bold}{Red}| {Green}{bold}Options{reset}  {Red}|{reset}          {Green}{bold}Description{reset}                                          {Red}|{reset}")

    print(f"{bold}{Red} ==========================================================================={reset}")

    print(f"{bold}{Red}| {Green}{bold}1{reset}        {Red}|{reset}     {Green}{bold}Checking Overview [FILES/ACTIVITIES/SERVICES/etc...]{reset}      {Red}|{reset}")

    print(f"{bold}{Red}| {Green}{bold}2{reset}        {Red}|{reset}     {Green}{bold}Checking for Code Obfuscation...{reset}                          {Red}|{reset}")

    print(f"{bold}{Red}| {Green}{bold}3{reset}        {Red}|{reset}     {Green}{bold}Checking for AndroidManifest File...{reset}                      {Red}|{reset}")

    print(f"{bold}{Red}| {Green}{bold}4{reset}        {Red}|{reset}     {Green}{bold}Checking for META-INT File...{reset}                             {Red}|{reset}")

    print(f"{bold}{Red}| {Green}{bold}5{reset}        {Red}|{reset}     {Green}{bold}Generate Full Report...{reset}                                   {Red}|{reset}")

    print(f"{bold}{Red}| {Green}{bold}6{reset}        {Red}|{reset}     {Green}{bold}Scanning for EndPoints/Links/Ips... (External Script){reset}     {Red}|{reset}")

    print(f"{bold}{Red}| {Green}{bold}q{reset}        {Red}|{reset}     {Green}{bold}Quit{reset}                                                      {Red}|{reset}")

    print(f"{bold}{Red} =========================================================================={reset}")

    print("\n")



def banner():

    print(HEADER + f"""
   ___           __         _    __                      
  / _ | ___  ___/ /______  (_)__/ /      
 / __ |/ _ \/ _  / __/ _ \/ / _  /      
/_/ |_/_//_/\_,_/_/  \___/_/\_,_/  {Green} __        _ ____      
                               | | / /__ ____(_) _(_)__ ____                    
Version 1.2                    | |/ / -_) __/ / _/ / -_) __/                    
{HEADER}(c) 2024, By OVK-CyberSec {Green}     |___/\__/_/ /_/_//_/\__/_/""".format(VERSION) +
reset, file=sys.stderr)
    
    simulate_long_task()



   # Obfuscation Check
    #Manifest Check
    #Integrity Check

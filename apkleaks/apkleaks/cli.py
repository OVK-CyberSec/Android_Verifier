#!/usr/bin/env python3
import argparse
import os
import sys
from pathlib import Path

from apkleaks.apkleaks import APKLeaks
from apkleaks.colors import color as col

def header():
	try:
		from importlib import metadata
		VERSION = "v" + metadata.version("apkleaks")
	except ImportError:
		try:
			import pkg_resources
			VERSION = "v" + pkg_resources.require("apkleaks")[0].version
		except Exception:
			VERSION = open(os.path.join(str(Path(__file__).parent.parent), "VERSION"), "r").read().strip()

def argument():
	parser = argparse.ArgumentParser()
	parser.add_argument("-f", "--file", help="APK file to scanning", type=str, required=True)
	parser.add_argument("-o", "--output", help="Write to file results (random if not set)", type=str, required=False)
	parser.add_argument("-p", "--pattern", help="Path to custom patterns JSON", type=str, required=False)
	parser.add_argument("-a", "--args", help="Disassembler arguments (e.g. --threads-count 5 --deobf)", type=str, required=False)
	parser.add_argument("--json", help="Save as JSON format", required=False, action="store_true")
	arg = parser.parse_args()
	return arg

def main():
	header()
	args = argument()
	init = APKLeaks(args)
	try:
		init.integrity()
		init.decompile()
		init.scanning()
	finally:
		init.cleanup()

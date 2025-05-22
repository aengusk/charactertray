#!pythonw
# @DONE add json parse functionality
# @DONE add copymode functionality
# @DONE restructure as package
# @DONE store image as binary
# @DONE decide names:
    # repository: charactertray
    # app: Character Tray
    # logo: Æ
# @DONE create new Æ backgroundless logo
# @TODO make sure only one instance can run at a time
# @TODO add argparse functionality and installation
    # run_on_startup (bool)
    # reload (to update JSON)
    # How would you make sure that there is only one instance running? 
# @DONE add self to PATH or Python's syspath
# @TODO add description, author, license to pyproject.toml
# @TODO clean all documentation, comments, and files

import subprocess
import sys
import argparse

def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='A Windows system tray utility to type special characters')
    parser.add_argument('--customize', '-c', action='store_true', 
                       help='open the directory containing characters.json')
    parser.add_argument('--reload', '-r', action='store_true',
                       help='reload the characters.json file')
    parser.add_argument('--test1', '-t', action='store_true', 
                       help='print test message 1')
    parser.add_argument('--test2', '-u', action='store_true',
                       help='print test message 2')
    return parser.parse_args()

def main():
    """Launch the headless version of Character Tray using pythonw.exe"""
    args = parse_args()
    
    # Handle test arguments
    if args.test1:
        print("Test message 1: Arguments are being passed correctly!")
        return 0
    if args.test2:
        print("Test message 2: Multiple arguments work too!")
        return 0

    cmd = ['pythonw', '-m', 'charactertray.run_icon']
    subprocess.Popen(cmd, creationflags=subprocess.CREATE_NO_WINDOW)
    return 0

if __name__ == '__main__':
    sys.exit(main()) # @TODO is this necessary?

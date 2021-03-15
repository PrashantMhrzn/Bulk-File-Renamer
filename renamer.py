from utils import Renamer
import argparse

parser = argparse.ArgumentParser(description='Renames every file inside the given folder.')
parser.add_argument('path', help='Absolute path of the folder')
parser.add_argument('-n','--naming_convention', metavar='', help='Not specifing will default to the name <file>')
args = parser.parse_args()

r = Renamer()
try:
    # path = input('Enter the folder path: ')
    # naming_convention = input(
    #     'Enter the naming convention(Empty for default name):')
    if args.naming_convention == None:
        args.naming_convention = 'file'
    r.rename(args.path, args.naming_convention)
    print("File Renaming Completed!")
except FileNotFoundError:
    print("File Not Found Enter Correct Path!")
except ValueError:
    print("Please Enter The Correct!")
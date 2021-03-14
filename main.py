from utils import Renamer

r = Renamer()
r.heading
try:
    path = input('Enter the folder path: ')
    naming_convention = input(
        'Enter the naming convention(Empty for default name):')
    if bool(naming_convention) == False:
        naming_convention = 'file'
    r.rename(path, naming_convention)
    print("File Renaming Completed!")
except FileNotFoundError:
    print("File Not Found Enter Correct Path!")
except ValueError:
    print("Please Enter The Correct!")
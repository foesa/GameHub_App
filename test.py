import os

def main():
   filepath = input("Please enter the filepath for games to be found: ")
   filepath = filepath.replace("\\", "/")
   filepath = filepath.replace('"',"")
   print(filepath)
   walker(filepath)

def walker(filepath):
    for folderName, subfolders, filenames in os.walk(filepath):
        print("The current folder is: " + folderName)
        for subfolder in subfolders:
            print("Subfolder of " + folderName + ": " + subfolder)
        for filename in filenames:
            print("File inside: "+ folderName + ": "+filename)

if __name__ == "__main__":
    main()

"""
TODO
Get info on list of launchers to compare names to
Create List of launchers based of .exe ending and is on Launcher list
Add games to Launchers
Display in console to show it works
Pickle all the stuff
Make UI using Kivy or something similar
"""
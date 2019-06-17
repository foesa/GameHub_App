import os

def main():
    filepath = input("Please enter the filepath for games to be found: ")
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

print("Guru99")
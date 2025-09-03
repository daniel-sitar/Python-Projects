import os

print("What kind of task do you want to do?\nList files\nCreate new files or folders\nDelete documents\n")

task = str(input("\nType selected action\nList\nCreate\nDelete\n"))
path = str(input("\nWhere do you want to do the action\nHome\nDesktop\nDocuments\nDownloads\nPictures\nVideos\nRoot\n"))

#Lists files from the most common folders using ls.
def listFiles(path,user):
    if path == "Home" or path == "home" or path == "HOME":
        os.system(f"ls /{path}")
    elif path == "Root" or path == "root" or path == "ROOT":
        os.system(f"ls /")
    elif path == "Desktop" or path == "desktop" or path == "DESKTOP":
        os.system(f"ls /home/{user}/Desktop")
    elif path == "Documents" or path == "documents" or path == "DOCUMENTS":
        os.system(f"ls /home/{user}/Documents")
    elif path == "Downloads" or path == "downloads" or path == "Downloads":
        os.system(f"ls /home/{user}/Downloads")
    elif path == "Pictures" or path == "pictures" or path == "PICTURES":
        os.system(f"ls /home/{user}/Pictures")
    elif path == "Videos" or path == "videos" or path == "VIDEOS":
        os.system(f"ls /home/{user}/Videos")
    else:
        print("Invalid path")


def createNew(path):
    executionType = str(input("\nDo you want to create a new file or folder?\nFile\nFolder\n"))
    if executionType == "Folder" or executionType == "folder" or executionType == "FOLDER":
        folderName = str(input("\nType in name of the folder you want to create\n"))



#Executes selected function
if task == "List" or task == "list" or task == "LIST":
    user = str(input("\nType in the name of your home directory\n"))
    listFiles(path,user)
elif task == "Create" or task == "create" or task == "CREATE":
    createNew(path)

import os
import getpass

print("What kind of task do you want to do?\nList files\nCreate new files or folders\nDelete documents\n")

#Used to determine what the user wants to do
task = str(input("\nType selected action\nList\nCreate\nDelete\n"))
#Used to figure out where the user wants to perform their action
path = str(input("\nWhere do you want to do the action\nHome\nDesktop\nDocuments\nDownloads\nPictures\nVideos\nRoot\n"))
#Used to figure out the users home directory
user = getpass.getuser()

#Lists files from the desired path using ls.
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


#Create new files or folders
def createNew(path,user):

    executionType = str(input("\nDo you want to create a new file or folder?\nFile\nFolder\n"))
    if executionType == "Folder" or executionType == "folder" or executionType == "FOLDER":
        folderName = str(input("\nType in name of the folder you want to create\n"))
        if path == "Home" or path == "home" or path == "HOME":
            os.system(f"mkdir /$HOME/{folderName}")
        elif path == "Root" or path == "root" or path == "ROOT":
            print("Error : It is not wise to manipulate root folder in linux")
        elif path == "Desktop" or path == "desktop" or path == "DESKTOP":
            os.system(f"mkdir /home/{user}/Desktop/{folderName}")
        elif path == "Documents" or path == "documents" or path == "DOCUMENTS":
            os.system(f"mkdir /home/{user}/Documents/{folderName}")
        elif path == "Downloads" or path == "downloads" or path == "DOWNLOADS":
            os.system(f"mkdir /home/{user}/Downloads/{folderName}")
        elif path == "Pictures" or path == "pictures" or path == "PICTURES":
            os.system(f"mkdir /home/{user}/Pictures/{folderName}")
        elif path == "Videos" or path == "videos" or path == "VIDEOS":
            os.system(f"mkdir /home/{user}/Videos/{folderName}")
        else:
            print("Path not found")

    elif executionType == "File" or executionType == "file" or executionType == "FILE":
        #Used to figure out how many files the user wants
        amount = int(input("\nHow many files to create?\n"))
        #Used to figure out what file type the user needs
        fileType = str(input("\nWhat kind of file do you want to create?\ntxt\n"))
        #Used to figure out the name for the new files a _ is added + number of the file
        fileName = str(input("\nType in the name that you want for the files\n"))
        #Loops in range of how many files there are supposed to be
        for x in range(1,amount+1):
            if path == "Home" or path == "home" or path == "HOME":
                os.system(f"touch /$HOME/{fileName}_{x}.{fileType}")
            elif path == "Root" or path == "root" or path == "ROOT":
                print("Error : It is not wise to manipulate root folder in linux")
            elif path == "Desktop" or path == "desktop" or path == "DESKTOP":
                os.system(f"touch /home/{user}/Desktop/{fileName}_{x}.{fileType}")
            elif path == "Documents" or path == "documents" or path == "DOCUMENTS":
                os.system(f"touch /home/{user}/Documents/{fileName}_{x}.{fileType}")
            elif path == "Downloads" or path == "downloads" or path == "DOWNLOADS":
                os.system(f"touch /home/{user}/Downloads/{fileName}_{x}.{fileType}")
            elif path == "Pictures" or path == "pictures" or path == "PICTURES":
                os.system(f"touch /home/{user}/Pictures/{fileName}_{x}.{fileType}")
            elif path == "Videos" or path == "videos" or path == "VIDEOS":
                os.system(f"touch /home/{user}/Pictures/{fileName}_{x}.{fileType}")
            else:
                print("Invalid path")


#Deletes documents and folders
def deleteContent(path,user):
    deleteType = str(input("\nDo you want to delete files or a folder?\nFile\nFolder\n"))
    #Deletes folders
    if deleteType == "Folder" or deleteType == "folder" or deleteType == "FOLDER":
        print("\nCAUTION : BE CAREFUL WHEN TYPING THE FOLDER NAME, DO NOT REMOVE SYSTEM FOLDERS\n")
        folderName = str(input("\nType in name of the folder you want to delete\n"))
        if path == "Home" or path == "home" or path == "HOME":
            os.system(f"rm -r /$HOME/{folderName}")
        elif path == "Root" or path == "root" or path == "ROOT":
            print("Error : It is not wise to manipulate root folder in linux")
        elif path == "Desktop" or path == "desktop" or path == "DESKTOP":
            os.system(f"rm -r /home/{user}/Desktop/{folderName}")
        elif path == "Documents" or path == "documents" or path == "DOCUMENTS":
            os.system(f"rm -r /home/{user}/Documents/{folderName}")
        elif path == "Downloads" or path == "downloads" or path == "DOWNLOADS":
            os.system(f"rm -r /home/{user}/Downloads/{folderName}")
        elif path == "Pictures" or path == "pictures" or path == "PICTURES":
            os.system(f"rm -r /home/{user}/Pictures/{folderName}")
        elif path == "Videos" or path == "videos" or path == "VIDEOS":
            os.system(f"rm -r /home/{user}/Videos/{folderName}")
        else:
            print("Invalid path")
    if deleteType == "File" or deleteType == "file" or deleteType == "FILE":
        fileName = str(input("\nType in the name of the files that you want to delete\n"))
        fileType = str(input("\nType in the type of file that you want to delete\n"))
        if path == "Home" or path == "home" or path == "HOME":
            os.system(f"rm -r /$HOME/{fileName}.{fileType}")
        elif path == "Root" or path == "root" or path == "ROOT":
            print("Error : It is not wise to manipulate root folder in linux")
        elif path == "Desktop" or path == "desktop" or path == "DESKTOP":
            os.system(f"rm -r /home/{user}/Desktop/{fileName}.{fileType}")
        elif path == "Documents" or path == "documents" or path == "DOCUMENTS":
            os.system(f"rm -r /home/{user}/Documents/{fileName}.{fileType}")
        elif path == "Downloads" or path == "downloads" or path == "DOWNLOADS":
            os.system(f"rm -r /home/{user}/Downloads/{fileName}.{fileType}")
        elif path == "Pictures" or path == "pictures" or path == "PICTURES":
            os.system(f"rm -r /home/{user}/Pictures/{fileName}.{fileType}")
        elif path == "Videos" or path == "videos" or path == "VIDEOS":
            os.system(f"rm -r /home/{user}/Videos/{fileName}.{fileType}")
        else:
            print("Invalid path")


#Executes selected function
if task == "List" or task == "list" or task == "LIST":
    listFiles(path,user)
elif task == "Create" or task == "create" or task == "CREATE":
    createNew(path,user)
elif task == "Delete" or task == "delete" or task == "DELETE":
    deleteContent(path,user)
else:
    print("Invalid task")
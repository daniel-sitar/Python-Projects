import os

print("What kind of task do you want to do?\nList files\nCreate folders\nDelete documents")

task = str(input("Type selected action\nList\nCreate\nDelete\n"))
path = str(input("Where do you want to do the action\nHome\nDesktop\nDocuments\nDownloads\nPictures\nVideos\nRoot\n"))

#Lists files from the most common folders using ls.
def ListFiles(path):
    if path == "Home" or path == "home" or path == "HOME":
        os.system(f"ls /{path}")
    elif path == "Root" or path == "root" or path == "ROOT":
        os.system(f"ls /")
    elif path == "Desktop" or path == "desktop" or path == "DESKTOP":
        os.system(f"ls /home/lunar/{path}")
    elif path == "Documents" or path == "documents" or path == "DOCUMENTS":
        os.system(f"ls /home/lunar/{path}")
    elif path == "Downloads" or path == "downloads" or path == "Downloads":
        os.system(f"ls /home/lunar/{path}")
    elif path == "Pictures" or path == "pictures" or path == "PICTURES":
        os.system(f"ls /home/lunar/{path}")
    elif path == "Videos" or path == "videos" or path == "VIDEOS":
        os.system(f"ls /home/lunar/{path}")
    else:
        print("Invalid path")



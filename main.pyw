import sys
import zipfile
import os
import time
import shutil
import tkinter as tk
from PIL import Image, ImageTk



from tkinter import filedialog

file_path = ""
def select_file():
    global file_path
    file_path = filedialog.askopenfilename()
    if file_path:
        print("Selected file:", file_path)
        makeDirectoryFromZippedFile()
    else:
        print("No file selected.")

def unzip_file(zip_file, extract_to):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print("Bestanden succesvol gekopieerd naar:", extract_to)

def makeDirectoryFromZippedFile():
    #make directory name based on zipped file_path name
    global file_path
    extract_to = file_path[:-4]
    print("De bestanden worden gekopieerd naar " + extract_to + ".")
    print("...")
    time.sleep(0)
    # Make sure the extraction directory exists
    os.makedirs(extract_to,exist_ok=True)
    unzip_file(file_path, extract_to)
    copy_folders_to_higher_directory(extract_to+"/"+os.path.basename(os.path.normpath(extract_to)), extract_to)
    # Unzip the file
    shutil.rmtree(extract_to+"/"+os.path.basename(os.path.normpath(extract_to)))





def copy_folders_to_higher_directory(src_dir, dest_dir):
    # Ensure the destination directory exists
    os.makedirs(dest_dir, exist_ok=True)
    print("bronmap:"+src_dir)
    print("doelmap:" + dest_dir)
    # Traverse the source directory
    print(os.walk(src_dir))
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            # Get the absolute path of the current file
            filePath = os.path.join(root, file)

            # Get the name of the parent folder
            parent_folder = os.path.basename(root)

            # Construct the destination file path with the parent folder name and unique identifier
            dest_file_path = os.path.join(dest_dir, f"{parent_folder}_{file}")

            # Copy the file to the destination directory
            shutil.copy2(filePath, dest_file_path)


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)






# Create the main window
root = tk.Tk()
root.title("Unzip Smartschool Upload Folder ")
root.configure(bg="white")
# Create a button to select a file
select_button = tk.Button(root, text="Open Zipbestand...", bg="#006082", fg="white", command=select_file)
select_button.pack(pady=20)
# Adjust size
root.geometry("400x220")
# Run the Tkinter event loop

# Open the image vesalius file
image = Image.open(resource_path("Images/VesaliusLogo.png"))
image = image.resize((80,50))
# Convert the Image object into a Tkinter-compatible object
tk_image = ImageTk.PhotoImage(image)

# Create a label widget to display the image
labelVesalius = tk.Label(root, image=tk_image,bg="white")
labelVesalius.place(x=0,y=50)
labelVesalius.pack()

# Open the image DOS file
imageDos = Image.open(resource_path("Images/dos.png"))
imageDos = imageDos.resize((80,80))
# Convert the Image object into a Tkinter-compatible object
tk1_image = ImageTk.PhotoImage(imageDos)

# Create a label widget to display the image
labelDos = tk.Label(root, image=tk1_image ,bg="white")
labelDos.place(x=0,y=50)
labelDos.pack()
root.mainloop()








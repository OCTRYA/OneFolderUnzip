import zipfile
import os
import time
import shutil
import tkinter as tk

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









# Create the main window
root = tk.Tk()
root.title("File Selection")

# Create a button to select a file
select_button = tk.Button(root, text="Select File", command=select_file)
select_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()








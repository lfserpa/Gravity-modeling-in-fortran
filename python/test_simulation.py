from gm import GMModel
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
# Get a file path from a file dialog
file_path = ""
file_path = filedialog.askopenfilename()

if file_path == "":
    print("Nothing to read")
else:
    gm_model = GMModel(project_file=file_path, new_project=False)
    print(gm_model)

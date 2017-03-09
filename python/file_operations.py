# Import statements for the libraries used
import tkinter as tk
from tkinter import filedialog

# Declare function that opens a file through a file open dialog window
def open_file():
    root = tk.Tk()
    root.withdraw()
    # Open file dialog to open a file
    file_path = filedialog.askopenfilename()
    return file_path

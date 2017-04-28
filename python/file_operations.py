# Import statements for the libraries used
import tkinter as tk
from tkinter import filedialog
import csv


# Declare function that opens a file through a file open dialog window
def get_file_path():
#    The purpose of this function is to read in a data set of
#    gravity and magnetic data and output it in as a list with
#    station, distance, elevation, gravity, and magnetic values
    # Set a tk window root
    root = tk.Tk()
    root.withdraw()
    # Get a file path from a file dialog
    file_path = filedialog.askopenfilename()
    return file_path

def open_file(file_path):
    data = []
    with open(file_path) as csvfile:
        csvData = csv.reader(csvfile, delimiter='\t')
        for row in csvData:
            data.append(row)
            
    print(data[0])
    return data

# THIS PROGRAM COMPUTES THE ATTRACTION OF BOTH GRAVITY AND MAGNETICS
# FOR A SINGLE BODY AND INVERTS IT TO FIT THE SOLUTION
# ORIGINALLY WRITE BY L. SERPA 9-12-1979 REVISED MARCH 2016

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
#    print(file_path)
    return file_path

def open_file(file_path):
    data = []
    with open(file_path) as csvfile:
        csvData = csv.reader(csvfile, delimiter='\t')
        for row in csvData:
            data.append(row)

#    print(data[0])
    return data


# Import file operations code
# from file_operations import *

#  Set up project parameters

project = {'name':' ','ambient_field':0.55, 'inclination': 65.0,'units':'km'}
answer = input("is this a new project? type yes or no ")
inc = 0

if answer == "yes":
    project['name'] = input("Enter a name for this project ")

    answer = input("what do you want to model: gravity, magnetics, both? ")
    if answer != "gravity":
        ambient_field = input("what is the ambient magnetic field? ")
        inclination = input("what is the magnetic inclination? ")
        azimuth = input("what is the azimuth of the profile?  ")
    #  need to write these values to a file now
else:
    print("Select your project file")
    print("  ")
    file_location_and_name = get_file_path()
    project_file = open_file(file_location_and_name)
    for num in project_file:
        if inc == 0:
            project['name'] = num[0]
            inc += 1
        elif inc == 1:
            project['ambient_field'] = float(num[0])
            inc += 1
        elif inc == 2:
            project['inclination'] = float(num[0])
            inc += 1
        else:
            inc == 3
            project['units'] = num[0]

print("ambient field = ", project['ambient_field']," Oersteds")
print("inclination = ", project['inclination'], " degrees")
print("units are ", 'units')

#  Get magnetic parameters if needed

#more things need to be written to something here

profile = input("Input a unique name for your profile ")
azimuth = input("What is the azimuth of the profile? ")

print("azimuth = ", azimuth, " degrees")
# Open file through a dialog box
file_location_and_name = get_file_path()
print(file_location_and_name)
data_return = open_file(file_location_and_name)
for i in data_return:
    print(*i)
#    print(data_return)

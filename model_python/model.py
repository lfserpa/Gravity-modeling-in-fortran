# Created on Thu Mar 16 06:11:02 2017
#
# @author: lfserpa

# This program computes the attraction of both gravity and magnetics
# for a single body and inverts it to fit the solution.
# Written by Laura Serpa 9/12/1979, revised March 2017
#
# The long range plan is to replace all of the input with a form.
import tkinter as tk
from tkinter import filedialog
import csv
import pdb

def dataInput():
#    The purpose of this function is to read in a data set of
#    gravity and magnetic data and output it in as a list with
#    station, distance, elevation, gravity, and magnetic values
    data = []
    # Set a tk window root
    root = tk.Tk()
    root.withdraw()
    # Get a file path from a file dialog
    file_path = filedialog.askopenfilename()
    with open(file_path) as csvfile:
        csvData = csv.reader(csvfile, delimiter='\t')
        for row in csvData:
            data.append(row)
    print(data[0])
    return data

#    try:
#        #fn = open(filein, 'r')
#        #except IOError:
#        #    print('cannot open', filein)
#        else:
#    print("success!")


#
#
#    for new in fh:
#        if new != '\n':  # return
#            addIt = new[:-1].split(',')  # remove trailing ln
#            data.append(addIt)
#    finally:
#        fn.close()  # close.file even if fail
#
#    gradesData = []
#    if data:
#        for student in data:
#            try:
#                name = student[0:-1]
#                grades = int(student[-1])
#                gradesData.append([name, [grades]])
#            except ValueError:
#                gradesData.append([student[:], []])
#    profile = input("Input a unique name for your profile  ")
#    answer = input("what do you want to model: gravity, magnetics, both?  ")
#    units = input("units? km, m, ft")
#    if answer != 'gravity':
#        ambient_field = float(input("what is the ambient magnetic field?  "))
#        inclination = float(input("what is the inclination  ?"))
#        azimuth = float(input("what is the azimuth of the profile? start to end "))
#    filein = input("Enter the name of your data file  ")

dataInput()

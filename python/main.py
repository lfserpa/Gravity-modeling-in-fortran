# THIS PROGRAM COMPUTES THE ATTRACTION OF BOTH GRAVITY AND MAGNETICS
# FOR A SINGLE BODY AND INVERTS IT TO FIT THE SOLUTION
# ORIGINALLY WRITE BY L. SERPA 9-12-1979 REVISED MARCH 2016

# Import file operations code
from file_operations import *

# Open file through a dialog box
file_location_and_name = get_file_path()
data_return = open_file(file_location_and_name)
print(data_return)

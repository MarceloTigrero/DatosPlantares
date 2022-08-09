import os
import sys

# Open the Recoleccion1 folder
os.chdir("Recoleccion1")
# Get the list of files in the folder
files = os.listdir()
print(files)

# Open the file for reading
f = open("S101RDH_R1M1.csv", "r")
print(f.read())
f.close()
# Read the files from the file
#files = f.readlines()
#print(files)
# Close the file


import argparse
import os
from PyPDF2 import PdfFileMerger
import sys

# Argument Parsing
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--directory",
                    help="directory (the working directory by default)")
parser.add_argument("-f", "--file",
                    help="output file name without path or ending" +
                    " (the working directorys name by default)")
args = parser.parse_args()

# Directory to merge files in
directory = args.directory or os.getcwd()

# Get all PDFs in folder, if none: exit
files = [file for file in os.listdir(directory) if file.endswith(".pdf")]
if len(files) == 0:
    exit

# Merge PDFs
merger = PdfFileMerger()
for pdf in files:
    with open(os.path.join(directory, pdf), 'rb') as fin:
        merger.append(fin)

# Save new PDF
destinationFileName = (args.file or os.path.basename(directory)) + ".pdf"
with open(os.path.join(directory, destinationFileName), "wb") as fout:
    merger.write(fout)

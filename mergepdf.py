import argparse
import os
import sys

from PyPDF2 import PdfFileMerger

# Argument Parsing
parser = argparse.ArgumentParser()
parser.add_argument(
    '-d', '--directory',
    help='directory (default: working directory)')
parser.add_argument(
    '-f', '--file',
    help='output file (default: the name of the working directory)')
args = parser.parse_args()

# Directory to merge files in
directory = args.directory or os.getcwd()

# Get all PDFs in folder, if none: exit
files = [file for file in os.listdir(directory) if file.endswith('.pdf')]
if len(files) == 0:
    exit

# Merge PDFs
merger = PdfFileMerger()
for pdf in files:
    with open(os.path.join(directory, pdf), 'rb') as fin:
        merger.append(fin)

# Save new PDF
dest_file_name = args.file or os.path.basename(directory)
if dest_file_name.endswith('.pdf') == False:
    dest_file_name += '.pdf'
with open(os.path.join(directory, dest_file_name), 'wb') as fout:
    merger.write(fout)
    
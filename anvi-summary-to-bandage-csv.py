# This script provides a CSV file for coloring contigs in Bandage by bins produced in Anvi'o.

# Helpful contributions by Antti Karkman, 2/2018

import argparse
import os

parser = argparse.ArgumentParser(description="This script provides a CSV file for coloring contigs in Bandage by bins produced in Anvi'o.")
parser.add_argument('-D', '--directory', help='anvi-summarize output folder')
parser.add_argument('-d', '--delimiter', help='Contig delimiter preceding contig ID in the assembly file e.g. "k141_"')
parser.add_argument('-o', '--output', default='bins-color.csv', help='Output file')

args = parser.parse_args()

# Output folder from anvi-summarize, which contains a folder for each bin:
directory_summary = args.directory

# Contig delimiter, separating ">" from the contig number:
# For example
# A contig number 124534 produced by MEGAHIT would have header ">k141_124534"
# and delimiter "k141_"
delimiter = args.delimiter

# Output file
output = args.output

# List of colors in hex format (e.g. "#0e264d") or standard color names (e.g. 'skyblue'):
# Color blind-friendly colors obtained from http://mkweb.bcgsc.ca/colorblind/
# Humans have a hard time detecting more colors than ~12 at once

colors = ["2F6D80", # Magenta
          "733E98", # Purple
          "2A66B1", # Blue
          "559FD7", # Sky Blue
          "C895C3", # Pink
          "67CAD5", # Light pink
          "9C2D44", # Dark red
          "E9815C", # Red
          "57AB57", # Orange
          "F3E945", # Yellow
          "BCDA82", # Peach
          "F8E5C0", # Tan
         ]

######


# List of bins present in directory
bins = [bin for bin in os.listdir(directory_summary + "/bin_by_bin/")]

# Create header of CSV file: Name,color
fh_csv = open(output, 'w')
fh_csv.write("Name,color,bin\n")

n = 0 # Count for determining colors

# For each bin in list:
for bin in bins:    

    # Assign color and track position in color list
    hexcolor = colors[n]
    n = n + 1
    if n >= len(colors): n = 0
    
    # Open file containing contigs, or another list of contigs headers with ">"
    fh = open(directory_summary + "/bin_by_bin/" + bin + "/" + bin + "-contigs.fa", 'r')
    for line in fh.readlines(): # Iterate through file
        
        # Write contig number to CSV with hexcolor and bin ID
        if ">" in line: # FASTA header
            contig = line.strip().split(delimiter)[1]
            fh_csv.write(contig + "," + hexcolor + "," + bin + "\n") 
            
fh_csv.close()
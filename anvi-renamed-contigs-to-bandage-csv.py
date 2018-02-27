
# coding: utf-8

# This script provides a CSV file for coloring contigs in Bandage by bins produced in Anvi'o.
#
#
# Output: "bins-color.csv"

# Modified by Antti Karkman, 1/2018

import argparse

parser = argparse.ArgumentParser(description="This script provides a CSV file for coloring contigs in Bandage by bins produced in Anvi'o.")
parser.add_argument('-b','--bins',  help='List of bins')
parser.add_argument('-D', '--directory', help='anvi-summarise output folder')
parser.add_argument('-d', '--delimiter', help='Contig delimiter in the assembly file e.g. "k141_"')
parser.add_argument('-r', '--report', help='anvi-script-reformat-fasta report file')
parser.add_argument('-o', '--output', default='bins-color.csv', help='Output file')

args = parser.parse_args()

# File listing bins:
file_listing_bins = args.bins

# Output folder from anvi-summarize, which contains a folder for each bin:
directory_summary = args.directory

# Contig delimiter, separating ">" from the contig number:
# For example
# A contig number 124534 produced by MEGAHIT would have header ">k141_124534"
# and delimiter "k141_"
delimiter = args.delimiter

# Report from Anvi'o contig renaming
report = args.report

# Output file
output = args.output

# List of colors in hex format (e.g. "#0e264d") or standard color names (e.g. 'skyblue'):
# Color blind-friendly colors obtained from http://mkweb.bcgsc.ca/colorblind/
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

###############

# Obtain list of bins
fh = open(file_listing_bins,'r')
bins = [] # Empty list of bins
for line in fh.readlines():
    bins.append(line.strip())
fh.close()

# Create header of CSV file: Name,color
fh_csv = open(output,'w')
fh_csv.write("Name,color,bin\n")

n = 0 # Count for determining colors

# make dictionary from the report file to match the contigs and renamed contigs
if args.report is not None:
	report_dict = {}
	with open(report) as f:
		for line in f:
			(key, val) =line.split("\t")
			val = val.split()[0]
			report_dict[key] = val

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
        if ">" in line:
		contig = line.rstrip()
		contig = contig.split(">")[1]
		if args.report is not None:
			contig = report_dict[contig]
		contig = contig.split(delimiter)[1]
		fh_csv.write(contig + "," + hexcolor + "," + bin + "\n")

fh_csv.close()

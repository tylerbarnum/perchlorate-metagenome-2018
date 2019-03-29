# Supplemental scripts for Barnum et. al 2018

In a recent study, I obtained metagenome-assembled genomes (MAGs) from enrichment communities totaling about 40 genomes. This repo contains code for assisting with similar work and a PDF of the publication.

Citation:
>Barnum, Tyler P. et al. 2018. “Genome-Resolved Metagenomics Identifies Genetic Mobility, Metabolic Interactions, and Unexpected Diversity in Perchlorate-Reducing Communities.” ISME Journal 12: 1568–1581.

## Using assembly graphs for binning

The script anvi-summary-to-bandage-csv.py is a part of the following tutorial: https://tylerbarnum.com/2018/02/26/how-to-use-assembly-graphs-with-metagenomic-datasets/. Specifically, it converts output from Anvi'o, a MAG binning tool, to the coloring scheme preferred by Bandage, an assembly visual tool, to improve binning especially for mobile genes (tranposons, recently horizontally transferred, etc.)

Figure 4: Manual assembly of perchlorate reduction genes within mobile genetic elements

Dependencies:

- Python 2.7 (untested in Python 3)

## Plotting a genomic summary of the community: custom gene annotation, relative abundance, and index of replication (iRep)

The notebook summarize-community.ipynb produces plots for summarizing the community based on coverage and replication data (externally produced) and functional annotations using custom HMMs and thresholds.

Figure 1: Summary of energy metabolism genes, abundance, and activity of metagenome-assembled genomes.
Figure 5: Relative abundance of metabolisms.

Dependencies:

- hmmer v. 3.1b2+
- Python 3.7

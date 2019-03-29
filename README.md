# Supplemental code for Barnum et. al 2018

In a recent study, I obtained metagenome-assembled genomes (MAGs) from enrichment communities totaling about 40 genomes. This repo contains code for assisting with similar work and a PDF of the publication.

Citation:
>Tyler P. Barnum, Israel A. Figueroa, Charlotte I. Carlström, Lauren N. Lucas, Anna L. Engelbrektson, and John D. Coates.2018. “Genome-Resolved Metagenomics Identifies Genetic Mobility, Metabolic Interactions, and Unexpected Diversity in Perchlorate-Reducing Communities.” ISME Journal 12: 1568–1581.

## Using assembly graphs for binning

The script anvi-summary-to-bandage-csv.py is a part of the following tutorial: https://tylerbarnum.com/2018/02/26/how-to-use-assembly-graphs-with-metagenomic-datasets/. Specifically, it converts output from Anvi'o, a MAG binning tool, to the coloring scheme preferred by Bandage, an assembly visual tool, to improve binning especially for mobile genes (tranposons, recently horizontally transferred, etc.)

#### Example fig: assembly graph color by bin
![assembly graph image](https://github.com/tylerbarnum/perchlorate-metagenome-2018/blob/master/images/graph-2.png)

Figures in paper:
- Figure 4: Manual assembly of perchlorate reduction genes within mobile genetic elements

Dependencies:
- Python 2.7 (untested in Python 3)

## Plotting a genomic summary of the community: custom gene annotation, relative abundance, and index of replication (iRep)

The notebook summarize-community.ipynb produces plots for summarizing the community based on coverage and replication data (externally produced) and functional annotations using custom HMMs and thresholds (generated here with the program hmmer).

![example plot](https://github.com/tylerbarnum/perchlorate-metagenome-2018/blob/master/data/output/community-summary.png)

Figure 1: Summary of energy metabolism genes, abundance, and activity of metagenome-assembled genomes.

Figure 5: Relative abundance of metabolisms.

Dependencies:

- hmmer v. 3.1b2+ (must be installed and in the path)
- Python 3.7

Input:

- ./data/genomes-data.csv table with genome data (coverage and index of replication)
- ./data/genomes/ directory with protein annotations for each genome in a separate .faa file
- For each protein (e.g. rpS3), an HMM (rpS3.hmm) and threshold score (rpS3.T)

#### About HMMS:

The .hmm file is constructed from an alignment of proteins using the hmmer function hmmbuild. The threshold score in the .T file limits the reported hits to only those above the threshold value. Take care to create an HMM from many representative proteins and a score that appropriately selects hits - it should be an iterative process. The better the HMM, the easier selecting a score threshold will be. Using HMMs may not be appropriate for you. In that case, edit the code to replace the HMM annotations with uploading gene presence/absence from another source.

```bash
# Build HMM and test
PROTEIN=rps3
muscle -in $PROTEIN.faa > $PROTEIN.aln
hmmbuild $PROTEIN.hmm $PROTEIN.aln
hmmsearch $PROTEIN.hmm protein_database.faa

# Select threshold from output and test
THRESHOLD=50
hmmsearch -T $THRESHOLD $PROTEIN.hmm protein_database.faa
```

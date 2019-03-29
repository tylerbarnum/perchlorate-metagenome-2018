import os
import subprocess as sp
import numpy as np
import pandas as pd

def hmmsearch_ea_genome(hmm_directory, genome_directory):

    """
    
    """
    
    # Create output directory
    output = './data/output/'
    if not os.path.exists(output):
        os.mkdir('./data/output/')

    # Initialize dataframe
    genomes = [filename.split('.faa')[0] for filename in os.listdir(genome_directory) if ".faa" in filename]
    df = pd.DataFrame({'Genome' : genomes})
    
    ### Hmmsearch
    
    # Load previously produced HMMs and score thresholds from folder
    # HMM file: <protein>.hmm
    # Score threshold file: <protein>.T 
    print('\n',"Searching %s genomes with HMMs...." % str(len(genomes)),'\n')
    HMMS = [filename.split('.hmm')[0] for filename in os.listdir(hmm_directory) if ".hmm" in filename]
    print("HMM", "\t", "Threshold score", "\t", "N genomes")
    for HMM in HMMS:
        
        # Store {genome : len(list of hits)}
        hmm_hits = {}

        # Only proceed if threshold file is available
        if HMM+".T" in os.listdir(hmm_directory):
            with open(hmm_directory + HMM + ".T") as fh:
                THRESHOLD = fh.readline().strip()
            

            # Run hmmsearch on each genome
            for N, genome in enumerate(genomes):

                # hmmsearch input
                genome_file = genome_directory + genome + ".faa"
                hmm_file = hmm_directory + HMM + ".hmm"
                output_table = output + genome + "." + HMM + ".table.txt"

                # hmmsearch
                hmmsearch="hmmsearch -T " + THRESHOLD + " --tblout " + output_table + " " + hmm_file + " " + genome_file
                sp.call(hmmsearch,shell=True)

                hits = []
                with open(output_table,'r') as fh:
                    for line in fh.readlines():
                        line = line.strip().split()
                        if "#" not in line[0]:
                            hits.append(line[0])

                hmm_hits[genome] = len(hits)
                
                # Remove every output table
                if os.path.exists(output_table):
                    os.remove(output_table)

            df[HMM] = df['Genome'].map(hmm_hits)
            N_genomes = df[HMM][df[HMM] > 0].count()
            print(HMM,"\t", THRESHOLD, "\t", N_genomes)
    
    print('\n','Search completed.')
    
    # For presence (1) and absence (0) only:
    df = df.set_index('Genome')
    df[df > 1] = 1
    
    return df

# Script to BLAST HCN genes against clover reference genome

import argparse
import subprocess 
import os

import pandas as pd
from create_blast_db import exit_status


def args():

    parser = argparse.ArgumentParser(
        description='BLAST input FASTA sequences against BLAST database',
        usage='python3.7 blast_sequences.py [options]')

    parser.add_argument('-i', '--fasta_in', required=True, type=str,
        help='Path to input FASTA file containing sequences to BLAST')
    parser.add_argument('-d', '--db_in', required=True, type=str,
        help='Path in BLAST database')
    parser.add_argument('-o', '--csv_out', required=True, type=str,
        help='Path to output CSV file')

    args = parser.parse_args()

    return args.fasta_in, args.db_in, args.csv_out

def blast_sequences(fasta_in, db, outfile):
    """BLAST's a set of sequences against BLAST database
 
    Args:
        fasta_in ('str'): Full path to input FASTA file from which database should be created
        db ('str'): Full path to input BLAST database
        outfile ('str'): Name of output file
 
    Returns"
        None: Writes BLAST results with header to disk
    """ 
    full_fasta_in_path = os.path.abspath(fasta_in)
    
    print('Blasting {0} against DB {1}'.format(full_fasta_in_path, db))
    print('BLAST results being written to: {0}'.format(outfile))
    
    Blast_Command = "blastn -query {0} -db {1} -out {2} -outfmt '6 qseqid sseqid pident length mismatch gapopen qstart qend qlen sstart send slen evalue bitscore qcovs qcovhsp' -num_threads 2 -evalue 1e-10 -max_hsps 5 -max_target_seqs 5".format(fasta_in, db, outfile)
    
    exit_code = subprocess.call(Blast_Command, shell=True)
    exit_status(exit_code)
    
    columns = ['qseqid', 'sseqid', 'pident', 'length', 'mismatch', 'gapopen', 'qstart', 'qend', 'qlen', 'sstart', 'send', 'slen', 'evalue', 'bitscore', 'qcovs', 'qcovhsp']
    blast_results = pd.read_table(outfile, sep = '\t', names = columns)
    
    blast_results.to_csv(outfile, sep = '\t', index = False)


if __name__ == '__main__':

    blast_sequences(*args())



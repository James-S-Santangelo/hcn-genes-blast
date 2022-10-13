# Script to create BLAST databsae from input FASTA file

import subprocess
import argparse

def args():

    parser = argparse.ArgumentParser(
        description='Creates a BLAST database from input FASTA file',
        usage='python3.7 create_blast_db.py [options]')
    parser.add_argument('-i', '--fasta_in', required=True, type=str,
        help='Full path to input FASTA file')

    args = parser.parse_args()

    return args.fasta_in

def exit_status(exit_code):
    """Prints success/fail of subprocess based on exit code
 
    Args:
        exit_code: ('int'): Exit code of subprocess
 
    Returns:
        None: Print to stdout.
    """
    if exit_code == 0:
        print("\nSubprocess completed successfully \n")
    else:
        print("\nThere was an error with the subprocess.\n Double check the command and try again.")

        
def makebBlastDatabase(fasta_in):
    """Creates BLAST database from fasta file.
 
    Args:
        fasta_in ('str'): Full path to input FASTA file from which database should be created
 
    Returns"
        None: Writes BLAST database to disk
    """ 
    # Name of database
    db_out = fasta_in + '.db'
  
    # Command to make BLAST database
    MakeBlastDb_Command = "makeblastdb -in " + fasta_in + " -out " + db_out + " -parse_seqids" + " -dbtype nucl"

    # Check whether subprocess successfully completed
    exit_code = subprocess.call(MakeBlastDb_Command, shell=True)
    exit_status(exit_code)


if __name__ == '__main__':
    fasta_in = args()
    makebBlastDatabase(fasta_in)

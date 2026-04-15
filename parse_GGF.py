#!/usr/bin/env python3

import argparse

def main():
    parser = argparse.ArgumentParser(
        description= "Fasta file Parse"
    )
    parser.add_argument("Fasta", help="covid.fasta")
    args = parser.parse_args()
    

    print(f"covid.fasta: {args.fasta}")

    if __name__ == '_main_':
        main()
    
    parser.add_argument("GFF", help="parse_GGF.py")

    from gff_functions import read_fasta, read_gff, write_output
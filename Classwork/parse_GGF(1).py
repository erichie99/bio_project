#!/usr/bin/env python3

import argparse
import gff_functions


def main():
    parser = argparse.ArgumentParser(description="Parse FASTA and GFF")

    parser.add_argument("fasta")
    parser.add_argument("gff")

    args = parser.parse_args()

    fasta_seq = gff_functions.read_fasta(args.fasta)
    gff_data = gff_functions.read_gff(args.gff)

    gff_functions.write_output(fasta_seq, gff_data)


if __name__ == '__main__':
    main()
    
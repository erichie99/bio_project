#!/usr/bin/env python3

def read_fasta(file):
    sequence = ""

    with open(file) as f:
        for line in f:
            if not line.startswith(">"):
                sequence += line.strip()

    return sequence


def read_gff(file):
    features = []

    with open(file) as f:
        for line in f:
            if line.startswith("#"):
                continue

            parts = line.strip().split()

            if len(parts) < 5:
                continue

            features.append({
                "type": parts[2],
                "start": int(parts[3]),
                "end": int(parts[4])
            })

    return features


def write_output(fasta, gff):
    print("FASTA length:", len(fasta))
    print("Number of features:", len(gff))

    for feature in gff[:5]:
        start = feature["start"] - 1
        end = feature["end"]

        seq = fasta[start:end]

        print(feature["type"], feature["start"], feature["end"])
        print(seq[:30], "...\n")
        
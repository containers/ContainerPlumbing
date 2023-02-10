#!/usr/bin/python3

import csv
import argparse
import os
import re

# Generate speakers list for the conference.  Outputs a speakers.md file.
#  Expects a CSV with the following columns:
# Title, Presenter, Co-Presenters, Company, Session Type, Track, Projects, Description

arg = argparse.ArgumentParser()
arg.add_argument("-f", "--file", help="sessions csv file", required=True)
arg.add_argument("-y", "--year", help="four-digit year", required=False)
args = arg.parse_args()
    
speakers = {}

with open(args.file) as csvfile:
    sessreader = csv.reader(csvfile)
    for sess in sessreader:
        speakers[sess[1]] = sess[3]
        cospks = sess[2].split(sep=',')
        for cospk in cospks:
            speakers[cospk.strip()] = sess[3]

with open('speakers.md','w') as spk:
    spk.write("|       Speaker         |  Affiliation  |\n")
    spk.write("| --------------------- | ------------- |\n")
    for speaker, company in sorted(speakers.items()):
        spk.write(f"| {speaker} | {company} |\n")

print("done")

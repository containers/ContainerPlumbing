#!/usr/bin/python3

import csv
import argparse
import os
import re

# Generate session links for the conference.  Outputs a links.md file.
#  Expects a CSV with the following columns:
# Title, Presenter, Co-Presenters, Company, Session Type, Track, Projects, Description

arg = argparse.ArgumentParser()
arg.add_argument("-f", "--file", help="sessions csv file", required=True)
arg.add_argument("-y", "--year", help="four-digit year", required=True)
args = arg.parse_args()
    
links = open('links.md','w')

with open(args.file) as csvfile:
    sessreader = csv.reader(csvfile)
    for sess in sessreader:
        sessname = (re.sub(r'\W+', '_', sess[0])).lower()[:16]
        sesspath = f"/sessions/{args.year}/{sessname}"
        sesslink = f"[{sess[0]}]({sesspath})\n"
        links.write(sesslink)

links.close()
        

print("done")

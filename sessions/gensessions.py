#!/usr/bin/python3

import csv
import argparse
import os
import re

arg = argparse.ArgumentParser()
arg.add_argument("-f", "--file", help="sessions csv file", required=True)
arg.add_argument("-y", "--year", help="four-digit year", required=True)
args = arg.parse_args()

if not os.path.exists(args.year):
    os.makedir(args.year)

with open(args.file) as csvfile:
    sessreader = csv.reader(csvfile)
    for sess in sessreader:
        sessname = (re.sub(r'\W+', '_', sess[0])).lower()[:16] + '.md'
        print(sessname)
        with open(os.path.join(args.year, sessname), 'w') as sessfile:
            stxt = f"# {sess[0]} \n\n"
            stxt += f"**Presenters**: {sess[1]}"
            if len(sess[2]) > 0:
                stxt += f", {sess[2]}"
            stxt += f" ({sess[3]})\n\n"
            stxt += f"**Session Type:** {sess[4]}\n\n"
            stxt += f"**Topics**: {sess[5]}, {sess[6]}\n\n"
            stxt += "## Session Details:\n\n"
            stxt += f"{sess[7]}\n"
            sessfile.write(stxt)

print("done")

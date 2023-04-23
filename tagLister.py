"""
By: James Hassel

This script is used to compile a list of every metadata tag available between all files included in
the "input" directory. The findings will be outputted to "out.csv".
"""

import os
import csv
import re

list = os.listdir("input")
output = ""

for item in list:
    output += os.popen("exiftool input/" + str(item)).read()

tokenOutput = output.split("\n")
for item in range(len(tokenOutput)):
    tokenOutput[item] = re.split(":", tokenOutput[item].replace(" ", ""))

tags = set()
for item in tokenOutput:
    tags.add(item[0])

tags = sorted(tags)
with open ("out.csv", "w") as f:
    writer = csv.writer(f)
    for item in range(len(tags)):
        writer.writerow([tags[item]])



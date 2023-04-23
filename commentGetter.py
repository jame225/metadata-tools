"""
By: James Hassel

This script is used to collect comments from .html, .css and .wolf files. It will create a list of files from the directory
this script is currently in, and findings will be in 'out.csv', a file created in the same directory this script is in.
"""

from bs4 import BeautifulSoup
from bs4 import Comment
import os
import csv

# Creating list of files
htmlfiles = [os.path.join(root, name)
             for root, dirs, files in os.walk("./")
             for name in files
             if name is not dir()
             and not name.__contains__(".jpg")
             and not name.__contains__(".png")
             and not name.__contains__(".jpeg")
             and not name.__contains__(".mp4")
             and not name.__contains__(".gif")]

stored = []
# Checking each file for comments
for file in htmlfiles:
    with open(file, "r", encoding="cp850") as html_file:
        soup = BeautifulSoup(html_file, 'html.parser')

    # find all comments in the file
    comments = soup.find_all(string=lambda text: isinstance(text, Comment))

    # create tuples of file, value for exporting
    for comment in comments:
        values = (file, comment)
        stored.append(values)

# exporting as csv
with open('out.csv', 'w') as f:
    writer = csv.writer(f)
    for item in stored:
        writer.writerow(item)


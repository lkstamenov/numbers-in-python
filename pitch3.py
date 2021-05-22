#
# Description: This script parses a data file into TAB delimited file, sort the Volume column
#              in ascending order and print Top 10 lines
## Author: Lachezar Stamenov
# Company: Winning Trade

import csv
import codecs
from operator import itemgetter

# Parse new_data file to TAB delimited file. TAB is also at the end of each line

contents = codecs.open('new_data', encoding='utf-8').read()

newcontents4 = contents.replace('    ','\t')      # Replace '    ' with TAB
newcontents3 = newcontents4.replace('   ','\t')   # Replace '   ' with TAB
newcontents2 = newcontents3.replace('  ','\t')    # Replace '  ' with TAB

delimiter = '\t'
newcontents_tab = newcontents2.replace('\n', delimiter + '\n')  # Add TAB at the end of each line to complete TAB delimited file

# Save the TAB delimited file into new_data2 file

new_data2 = open("new_data2","w")
new_data2.write(newcontents_tab)
new_data2.close

# Sort the Top 10 lines by volume in ascending order and print Top 10 lines

volume_sorted = csv.reader(open("new_data2"), delimiter="\t")

print('\nSorted Top 10 by Volume Ascending\n')

line_count = 0
for line in sorted(volume_sorted, key=itemgetter(1), reverse=True):
    if line_count <= 9:
        print(line)
        line_count += 1
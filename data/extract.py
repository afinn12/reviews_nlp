import csv
from tqdm import tqdm
import sys
from collections import defaultdict
import argparse

# allow large files
csv.field_size_limit(sys.maxsize)

# PRODUCT_ID = 'B004Z1CZDK'
parser = argparse.ArgumentParser()
parser.add_argument('--id', type=str, required=True, help='product id')
parser.add_argument('--infile', type=str, required=True, help='Input File (file.tsv)')
args = parser.parse_args()
PRODUCT_ID = args.id
# input and output files
infile = args.infile
outfile = f"data/extract/toy_{PRODUCT_ID}.tsv"

# write the reviews for a specific product to the output file
with open(infile, newline='', encoding='utf-8') as input, open(outfile, mode='w', newline='', encoding='utf-8') as output:
    reader = csv.DictReader(input, delimiter='\t')
    writer = csv.DictWriter(output, fieldnames=reader.fieldnames, delimiter='\t')
    
    writer.writeheader()
    for row in tqdm(reader, desc="writing"):
        # only keep reviews where the product id matches
        if row["product_id"] == PRODUCT_ID:
            writer.writerow(row)

import csv
from neural_net.src.config.embedding_config import APPLE_ROOT

input_file = APPLE_ROOT
output_file = 'deduped.csv'
name_column = 'trackName'  # change this to your actual ID column name
artist_column = 'artistName'

seen = set()
rows = []

total = 0
unique = 0

with open(input_file, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    for row in reader:
        total += 1
        row_id = (row[name_column], row[artist_column])
        if row_id not in seen:
            seen.add(row_id)
            rows.append(row)
            unique += 1

with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Original rows: {total}")
print(f"Unique rows: {unique}")
print(f"Duplicates removed: {total - unique}")
import csv
from neural_net.src.config.embedding_config import APPLE_ROOT

input_file = APPLE_ROOT
output_file = 'deduped.csv'
id_column = 'trackId'  # change this to your actual ID column name

seen = set()
rows = []

with open(input_file, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    for row in reader:
        row_id = row[id_column]
        if row_id not in seen:
            seen.add(row_id)
            rows.append(row)

with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Original rows: {len(seen) + (len(rows) - len(seen))}")
print(f"Unique rows: {len(rows)}")
print(f"Duplicates removed: {len(seen) - len(rows) + (len(rows) - len(seen))}")
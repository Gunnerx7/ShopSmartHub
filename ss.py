import json

# Open the original file in UTF-16 encoding
with open('dumpdata.json', 'r', encoding='utf-16') as f:
    data = json.load(f)

# Save the data to a new file in UTF-8 encoding
with open('dumpdata_utf8.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)

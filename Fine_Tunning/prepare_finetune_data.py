import json

# Open the JSON file for reading
with open('C:/Users/TapasSaha/Desktop/Fine_Tunning/prompt_completion_pairs.json', 'r') as json_file:
    # Parse the JSON data into a Python object
    data = json.load(json_file)

# Open a new file for writing in JSONL format
with open('C:/Users/TapasSaha/Desktop/Fine_Tunning/data.jsonl', 'w') as jsonl_file:
    # Loop through the parsed data and write each item as a separate line
    for item in data:
        jsonl_file.write(json.dumps(item) + '\n')

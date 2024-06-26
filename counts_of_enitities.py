import json
from collections import defaultdict

# Function to count occurrences of each entity type and calculate the ratio
def count_entities_and_ratio(json_file_path, target_entity_type):
    # Load the JSON data from the file
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    
    # Initialize counts
    target_entity_count = 0
    total_entities = 0

    # Iterate over each item in the list
    for item in data:
        annotations = item.get('annotations', '')
        entities = item.get('entities', [])

        # Increment total entities count
        total_entities += len(entities)

        # Count occurrences of target entity type
        for entity in entities:
            if len(entity) >= 3 and entity[2] == target_entity_type:
                target_entity_count += 1

    # Calculate the ratio
    ratio = target_entity_count / total_entities if total_entities > 0 else 0

    print(f"Count of '{target_entity_type}': {target_entity_count}")
    print(f"Total number of entities: {total_entities}")
    print(f"Ratio: {ratio}")

# Path to your JSON file
json_file_path = 'annotations.json'
# Entity type to search for
target_entity_type = "SYMPTOMS"

# Call the function to count the entity type and calculate the ratio
count_entities_and_ratio(json_file_path, target_entity_type)

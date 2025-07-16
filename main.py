from modules.detector import detect_items
from modules.inventory import create_table, insert_items, get_latest_items

create_table()

# Detect from image
image_path = "C:\\Users\\tharu\\Desktop\\smart_fridge_ai\\data\\data\\stock-photo-open-refrigerator-or-fridge-door-with-food-inside-1769700395.jpg"
new_items = detect_items(image_path)

# Get previous state
old_items = get_latest_items()

# Find added and removed items
added = [item for item in new_items if item not in old_items]
removed = [item for item in old_items if item not in new_items]

# Save current state
insert_items(new_items)

print("Added items:", added)
print("Removed items:", removed)


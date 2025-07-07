# list_demo.py

# 🧪 Creating a list
inventory = ["sword", "shield", "healing potion", "cloak"]

# 🎯 Accessing elements
print("First item:", inventory[0])
print("Last item:", inventory[-1])

# 🛠️ Modifying elements
inventory[2] = "greater healing potion"
print("Updated inventory:", inventory)

# ➕ Adding elements
inventory.append("map")  # Adds to the end
inventory.insert(1, "dagger")  # Inserts at index 1
print("After adding items:", inventory)

# ❌ Removing elements
inventory.remove("cloak")  # Removes by value
removed_item = inventory.pop()  # Removes and returns the last item
print("Removed:", removed_item)
print("Inventory after removal:", inventory)

# 🔄 List operations
inventory += ["rope", "lantern"]
print("Extended inventory:", inventory)

# 📦 Slicing
print("First three items:", inventory[:3])
print("Last two items:", inventory[-2:])

# 🔍 Searching
if "map" in inventory:
    print("You’ve got the map!")

# 📊 Sorting & reversing
sorted_inventory = sorted(inventory)
print("Sorted:", sorted_inventory)
inventory.reverse()
print("Reversed:", inventory)

# 🧵 Looping through a list
print("\n-- Inventory Check --")
for item in inventory:
    print("•", item)

inventory.clear()
print("Cleared inventory:", inventory)
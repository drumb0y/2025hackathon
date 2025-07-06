# tuple_demo.py

# 🧱 Creating tuples
coordinates = (32.7767, -96.7970)
character_stats = ("Knight", 85, 420)

# 🎯 Accessing tuple elements
print("Latitude:", coordinates[0])
print("Character type:", character_stats[0])

# 📦 Nested tuples
game_data = (
    ("Archer", 70, 380),
    ("Mage", 65, 250),
    ("Rogue", 80, 310)
)

print("\n-- Game Data --")
for character in game_data:
    name, strength, hp = character
    print(f"{name}: Strength={strength}, HP={hp}")

name, strength, hp = character_stats
print(f"\nUnpacked:\nName={name}, Strength={strength}, HP={hp}")

print("\nNumber of characters:", len(game_data))
print("Count of 'Mage':", [char[0] for char in game_data].count("Mage"))

mage_index = next((i for i, c in enumerate(game_data) if c[0] == "Mage"), None)
print("Mage is at index:", mage_index)

names = ["Paladin", "Druid", "Warlock"]
levels = [90, 78, 66]
stats_tuple = tuple(zip(names, levels))
print("\nZipped tuples:", stats_tuple)


print("\n-- Stats Overview --")
for name, level in stats_tuple:
    print(f"{name}: Level {level}")


# Uncommenting the following line would raise an error
# character_stats[1] = 90  

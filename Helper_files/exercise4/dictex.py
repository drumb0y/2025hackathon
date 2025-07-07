# dictionary_demo.py

game_character = {
    "name": "Arcanist",
    "level": 12,
    "magic_type": "Dark",
    "hp": 340
}

print("Name:", game_character["name"])
print("Level:", game_character.get("level"))

game_character["hp"] = 380
print("Updated HP:", game_character["hp"])

game_character["mana"] = 210
print("Added Mana:", game_character["mana"])

removed = game_character.pop("magic_type")
print("Removed magic type:", removed)

if "mana" in game_character:
    print("Mana exists!")

print("\n-- Character Stats --")
for key, value in game_character.items():
    print(f"{key}: {value}")

print("\nKeys:", list(game_character.keys()))
print("Values:", list(game_character.values()))
print("Items:", list(game_character.items()))

update = {"level": 13, "special_ability": "Shadow Burst"}
game_character.update(update)
print("\nAfter update:", game_character)

game_character.clear()
print("Cleared dictionary:", game_character)
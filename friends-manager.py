import json

# Load friends from file (if it exists), otherwise start with defaults
try:
    with open("friends.json", "r") as f:
        friends = json.load(f)
except FileNotFoundError:
    friends = [
        {"name": "Adam", "age": 22},
        {"name": "Arya", "age": 21},
        {"name": "Mustafa", "age": 23},
        {"name": "Jay", "age": 24}
    ]

# Show current friends
print("Current friends:")
for friend in friends:
    print(f"- {friend['name']} ({friend['age']} years old)")

while True:
    action = input("\nType 'add', 'remove', or 'exit': ").lower()

    if action == "exit":
        break

    elif action == "add":
        name = input("What is your name? ")
        age = int(input("How old are you? "))

        # Check if already exists
        exists = False
        for friend in friends:
            if friend["name"].lower() == name.lower():
                exists = True
                break

        if exists:
            print(f"{name} is already in the list!")
        else:
            friends.append({"name": name, "age": age})
            print(f"Added {name}, {age} years old.")

    elif action == "remove":
        name = input("Who do you want to remove? ")
        removed = False
        for friend in friends:
            if friend["name"].lower() == name.lower():
                friends.remove(friend)   # delete the dictionary
                remove

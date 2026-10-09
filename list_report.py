items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]

number = 1
for item in items:
    print(f"{number}. {item}")
    number += 1

long_name_count = 0
for item in items:
    if len(item) > 4:
        long_name_count += 1

print(f"Items with more than 4 letters: {long_name_count}")

longest_item = items[0]
for item in items:
    if len(item) > len(longest_item):
        longest_item = item

print(f"Longest item name: {longest_item}")
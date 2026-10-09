shopping_list = []

while True:
    action = input("add / remove / show / done: ").strip().lower()

    if action == "add":
        item = input("What item would you like to add? ")
        shopping_list.append(item)
    elif action == "remove":
        item = input("What item would you like to remove? ")
        if item in shopping_list:
            shopping_list.remove(item)
        else:
            print("That item is not on your list.")
    elif action == "show":
        for item in shopping_list:
            print(item)
    elif action == "done":
        print("Goodbye!")
        break
# Problem : Check if all elemenmts in a list are unique. If a duplicate is found, exit the loop and print the suplicate.


items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()


for item in items:
    if item in unique_item:
        print("duplicate: ", item)
        break
    unique_item.add(item)

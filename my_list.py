my_list = [] # Creates an empty list called my_list


my_list.extend([10, 20, 30, 40]) # Append the following elements to my_list: 10, 20, 30, 40


my_list.insert(1, 15) # Insert the value 15 at the second position in the list


my_list.extend([50, 60, 70]) # Extend my_list with another list: [50, 60, 70]


my_list.pop() # Remove the last element from my_list


my_list.sort() # Sort my_list in ascending order

# Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print(f"The index of 30 in my_list is: {index_of_30}")

# Print the final my_list
print("Final my_list:", my_list)

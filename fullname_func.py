def concat_lists(salutations, names, surnames):
    """Function to concatenate three lists element-by-element using a for loop."""
    full_names = []
    # Loop through the lists using their index
    for i in range(len(salutations)):
        # Combine the elements with spaces in between
        full_name = f"{salutations[i]} {names[i]} {surnames[i]}"
        full_names.append(full_name)
    return full_names

# --- Taking Input from the User ---
saluation_list = []
name_list = []
surname_list = []

# Ask the user how many entries they want to make
num_entries = int(input("How many entries do you want to add? "))

print("\n--- Enter the Details ---")
for i in range(num_entries):
    print(f"\nEntry #{i+1}:")
    saluation = input("Salutation (e.g., Mr., Ms.): ")
    name = input("First Name: ")
    surname = input("Surname: ")
    
    # Append user inputs into their respective lists
    saluation_list.append(saluation)
    name_list.append(name)
    surname_list.append(surname)

# --- Displaying the Output ---
print("\n" + "="*50)
print("Salutations list:", saluation_list)
print("Names list:      ", name_list)
print("Surnames list:   ", surname_list)
print("="*50)

# Call the function and print the final result
final_result = concat_lists(saluation_list, name_list, surname_list)
print("Concatenated Full Names:")
print(final_result)
print("="*50)
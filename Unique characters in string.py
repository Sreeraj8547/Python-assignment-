input_string = input("Enter a string: ")
cleaned_string = input_string.replace(" ", "").lower()
unique_characters = set(cleaned_string)

print(len(unique_characters) == len(cleaned_string))

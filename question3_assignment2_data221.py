import string  #For punctuation removal

textfile = open("sample-file.txt","r")
textfile_contents = textfile.readlines()
textfile_contents_original = textfile_contents.copy()
textfile.close()

#Changing all elements in the list to lowercase
for line in range(len(textfile_contents)):
    textfile_contents[line] = textfile_contents[line].lower()


# Removing all punctuation and whitespace, by checking each character separately
for line in range(len(textfile_contents)):
    filtered_line = ""
    for characters in textfile_contents[line]:
        if characters not in string.punctuation and not characters.isspace(): #checking punctuation and spaces
            filtered_line += characters
    textfile_contents[line] = filtered_line


#Identifying duplicates, key: normalized lin, value: list of line_number and original_line
duplicated_lines = {}
for line in range(len(textfile_contents)):
    cleaned_line = textfile_contents[line]  #lowercase,no punctuation, no spaces
    original_line = textfile_contents_original[line].rstrip("\n") #original line from the file before it was modified

    # Ignore blank lines so they are not counted as duplicate sets
    if cleaned_line == "":
        continue

    if cleaned_line in duplicated_lines:
        #add this line number and original line to the existing key and value
        duplicated_lines[cleaned_line].append((line + 1, original_line))
    else:
        duplicated_lines[cleaned_line] = [(line + 1, original_line)]  #Create a new key and value for it


set_count = 0

for cleaned_line in duplicated_lines:
    # Only consider keys that form a near-duplicate set
    if len(duplicated_lines[cleaned_line]) > 1:
        set_count += 1
        print(f"\nSet {set_count}:")

        for line_number, original_line in duplicated_lines[cleaned_line]:
            print(f"{line_number}: {original_line}")

        # Stop after printing the first two sets
        if set_count == 2:
            break












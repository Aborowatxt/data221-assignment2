def find_lines_containing(filename, keyword):
    """
    Returns a list of (line_number, line_text) for lines that contain
    keyword (case-insensitive). Line numbers start at 1.
    """

    matching_lines = []
    # List to store matching (line_number, line_text) tuples

    text_file = open(filename, "r")
    file_lines = text_file.readlines()
    text_file.close()
    # Open the file, read all lines into a list, then close the file

    keyword_lowercase = keyword.lower()
    # Convert keyword to lowercase for case-insensitive comparison

    for line_index in range(len(file_lines)):
        current_line_text = file_lines[line_index].rstrip("\n")
        # Remove newline character from the current line

        current_line_lowercase = current_line_text.lower()
        # Convert line text to lowercase 

        if keyword_lowercase in current_line_lowercase:
            # Check if keyword appears in the line
            matching_lines.append((line_index + 1, current_line_text))
            # Store line number (starting at 1) and original line text

    return matching_lines
    # Return all matching lines



# Testing the function

search_results = find_lines_containing("sample-file.txt", "data")

number_of_matches = len(search_results)


print("Number of matching lines found:", number_of_matches)

print("First 3 matching lines:")
for line_number, line_text in search_results[:3]:
    print(f"{line_number}: {line_text}")

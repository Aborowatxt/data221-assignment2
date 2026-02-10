import string  #For punctuation removal

#Read the file
text_file = open("sample-file.txt", "r")
text_file_content = text_file.read()
text_file.close()

#Turn text into tokens
text_file_tokens = text_file_content.split()

#Convert tokens to lowercase
for token in range(len(text_file_tokens)):
    text_file_tokens[token] = text_file_tokens[token].lower()

#remove punctuation using string module
for token in range(len(text_file_tokens)):
    text_file_tokens[token] = text_file_tokens[token].strip(string.punctuation)

# To check for alphabetic characters
sorted_text_file_tokens = []
for token in text_file_tokens:
    alphabet_count = 0
    for character in token:
        if character.isalpha():  #isalpha() checks if a character is an alphabet
            alphabet_count += 1
    if alphabet_count >= 2:
        sorted_text_file_tokens.append(token)  #adds to sorted list


#Count word frequencies
word_counts = {}  #set up a dictionary, key should be the word frequency

for token in sorted_text_file_tokens:
    if token in word_counts:
        word_counts[token] += 1      #adds to the word count
    else:
        word_counts[token] = 1

items = list(word_counts.items()) #converts the dictionary to a list, each index is a tuple of the word and it's frequency
#Sort the list by the count (second value in each pair), highest first.
items.sort(key=lambda pair: pair[1], reverse=True)
top_10 = items[:10]   #First ten 0-9

print(top_10)

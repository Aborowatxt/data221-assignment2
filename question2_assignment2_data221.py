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

#Creating bigrams
bigrams = []

for i in range(len(sorted_text_file_tokens) - 1):
    bigram = (sorted_text_file_tokens[i], sorted_text_file_tokens[i + 1])
    bigrams.append(bigram)


bigram_counts = {}  #Create dictionary and value is the frequency of each bigram

for bigram in bigrams:
    if bigram in bigram_counts:
        bigram_counts[bigram] += 1
    else:
        bigram_counts[bigram] = 1


bigram_frequencies = list(bigram_counts.items()) # Convert dictionary to a list of (bigram, count) pairs
 # Sort the list based on the frequency (count) in descending order
bigram_frequencies.sort(key=lambda pair: pair[1], reverse=True)

for bigram, count in bigram_frequencies[:5]:
    print(f"{bigram[0]} {bigram[1]} -> {count}")
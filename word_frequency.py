import re

# Open the text file that will be analyzed
file = open("sample_text.txt")

# Dictionary to store the count of each word
counts = {}

# Read the file line by line
for line in file:
    
    # Use regex to extract words and convert them to lowercase
    words = re.findall(r'\b[a-zA-Z]+\b', line.lower())
    
    # Count how many times each word appears
    for word in words:
        counts[word] = counts.get(word, 0) + 1

# Sort words by frequency (highest first)
sorted_words = sorted(counts.items(), key=lambda x: x[1], reverse=True)

print("Top words:\n")

# Print the 10 most frequent words
for word, count in sorted_words[:10]:
    print(word, ":", count)
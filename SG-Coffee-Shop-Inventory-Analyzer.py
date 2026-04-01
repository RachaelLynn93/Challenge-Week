# 1. The setup: Our messy inventory log
log_data = "Restock oat milk. Oat milk is low! Espresso beans out of stock. Need more expresso beans, vanilla syrup, and oat milk."

# 2. The Cleanup: Normalize the data. 
# Chain string methods to make it lowercase and strip out punctuation
clean_log = log_data.lower().replace(".", "").replace("!", "").replace(",", "")

# 3. The Split: Turn the string into a list of words
word_list = clean_log.split()

# 4. The Stock Counter: Count the frequencies
item_counts = {}

for word in word_list:
    # If the word is already in our dictionary, add 1 to its count
    if word in item_counts:
        item_counts[word] += 1
    # If it's a brand new word, add it to the dictionary and set the count to 1
    else:
        item_counts[word] = 1
        
# Print the final dictionary to see the results
print(item_counts)

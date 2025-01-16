from collections import Counter

def findSubstring(s, words):
    # If the input string or words list is empty, return an empty list
    if not s or not words:
        return []

    word_len = len(words[0])  # Length of each word
    num_words = len(words)  # Number of words
    total_len = word_len * num_words  # Total length of all words concatenated
    word_count = Counter(words)  # Dictionary to count occurrences of each word in words list

    result = []  # List to store the starting indices of the substrings

    # Iterate over each character in the string up to the length of a word
    for i in range(word_len):
        left = i  # Left pointer
        right = i  # Right pointer
        current_count = Counter()  # Dictionary to count occurrences of words in the current window
        # Slide the window to the right
        while right + word_len <= len(s):
            word = s[right:right + word_len]  # Extract the word from the current position
            right += word_len  # Move the right pointer to the next word
            if word in word_count:
                current_count[word] += 1  # Update the count of the word using Counter
                # If the word count exceeds the expected count, move the left pointer to the right
                while current_count[word] > word_count[word]:
                    current_count[s[left:left + word_len]] -= 1
                    left += word_len
                # If the window size matches the total length of all words, add the starting index to the result
                if right - left == total_len:
                    result.append(left)
            else:
                # If the word is not in the word_count, reset the current_count and move the left pointer to the right
                current_count.clear()
                left = right

    return result

# Example usage:
s = "barfoothefoobarman"
words = ["foo", "bar"]
print(findSubstring(s, words))  # Output: [0, 9]
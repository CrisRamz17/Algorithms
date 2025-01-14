def length_of_longest_substring(s: str) -> int:
    charSet = set()
    left = 0
    result = 0
    for right, char in enumerate(s):
        while char in charSet:
            charSet.remove(s[left])
            left += 1
        charSet.add(char)
        result = max(result, right - left + 1)
    return result
# Example usage
if __name__ == "__main__":
    test_string = "aaaa"
    print(f"The length of the longest substring without repeating characters is: {length_of_longest_substring(test_string)}")
def mergeAlternately(word1: str, word2: str) -> str:
    result = []
    min_length = min(len(word1), len(word2))
    
    # Alternate characters up to the shorter length
    for i in range(min_length):
        result.append(word1[i])
        result.append(word2[i])
    
    # Add the remaining characters from the longer word
    result.append(word1[min_length:])
    result.append(word2[min_length:])
    
    return ''.join(result)

# Example: Calling the function with predefined values
print("Example 1:", mergeAlternately("abc", "pqr"))       # Output: "apbqcr"
print("Example 2:", mergeAlternately("ab", "pqrs"))       # Output: "apbqrs"
print("Example 3:", mergeAlternately("abcd", "pq"))       # Output: "apbqcd"

# Allowing user input to run anywhere
word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

print("Merged Output:", mergeAlternately(word1, word2))

from collections import Counter

def check_permutation(pattern, text):
    pattern_count = Counter(pattern)
    window_count = Counter(text[:len(pattern)])
    
    for i in range(len(pattern), len(text)):
        if pattern_count == window_count:
            return "YES"
        
        window_count[text[i - len(pattern)]] -= 1
        if window_count[text[i - len(pattern)]] == 0:
            del window_count[text[i - len(pattern)]]
        
        window_count[text[i]] += 1
    
    if pattern_count == window_count:
        return "YES"
    
    return "NO"

# Read the number of test cases
T = int(input("Enter the number of test cases: "))

# Iterate over each test case
for _ in range(T):
    pattern = input("Enter the pattern: ")
    text = input("Enter the text string: ")
    result = check_permutation(pattern, text)
    print(result)


# https://leetcode.com/problems/group-anagrams/description/

# TC - O(N * K) SC - O(N * K)
def groupAnagrams(strs):
    # Create a dictionary to store character frequency tuple as key and list of anagrams as value
    ana_dict = {}

    # Iterate through each string
    for s in strs:
        # Create a list of 26 zeros (for each lowercase letter)
        char_count = [0] * 26

        # Count frequency of each character
        for char in s:
            char_count[ord(char) - ord('a')] += 1

        # Convert list to tuple to use as dictionary key
        key = tuple(char_count)

        # Add string to appropriate anagram group
        if key in ana_dict:
            ana_dict[key].append(s)
        else:
            ana_dict[key] = [s]


    # Return all grouped anagrams
    return list(ana_dict.values())

# Test cases
test1 = ["eat","tea","tan","ate","nat","bat"]
test2 = [""]
test3 = ["a"]

print(groupAnagrams(test1))  # [["eat","tea","ate"],["tan","nat"],["bat"]]
print(groupAnagrams(test2))  # [[""]]
print(groupAnagrams(test3))  # [["a"]]
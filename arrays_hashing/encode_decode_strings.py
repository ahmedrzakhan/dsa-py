# https://leetcode.com/problems/encode-and-decode-strings/description/

class Codec:
    # TC - O(N), SC - O(N)
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        Args:
            strs: List[str] - List of strings to encode
        Returns:
            str - The encoded string
        """
        result = ""
        for s in strs:
            # Append the length of the string, a delimiter '#', and then the string itself
            result += str(len(s)) + "#" + s
        return result

    # TC - O(N), SC - O(N)
    def decode(self, s):
        """Decodes a single string to a list of strings.
        Args:
            s: str - The encoded string
        Returns:
            List[str] - The decoded list of strings
        """
        result = []
        i = 0

        while i < len(s):
            # Find the position of the '#' delimiter
            j = i
            while s[j] != '#':
                j += 1

            # Extract the length of the next string
            length = int(s[i:j])

            # Extract the string itself
            start_pos = j + 1
            end_pos = start_pos + length
            result.append(s[start_pos:end_pos])

            # Move to the start of the next length indicator
            i = end_pos

        return result

# Test cases
codec = Codec()

# Example 1
input1 = ["neet", "code", "love", "you"]
encoded1 = codec.encode(input1)
decoded1 = codec.decode(encoded1)
print(f"Example 1 - Input: {input1}")
print(f"Example 1 - Encoded: {encoded1}")
print(f"Example 1 - Decoded: {decoded1}")
print(f"Example 1 - Match: {input1 == decoded1}")

# Example 2
input2 = ["we", "say", ":", "yes"]
encoded2 = codec.encode(input2)
decoded2 = codec.decode(encoded2)
print(f"Example 2 - Input: {input2}")
print(f"Example 2 - Encoded: {encoded2}")
print(f"Example 2 - Decoded: {decoded2}")
print(f"Example 2 - Match: {input2 == decoded2}")
# https://leetcode.com/problems/hand-of-straights/

from collections import Counter
# TC - O(NLogN), SC - O(N)
def isNStraightHand(hand: list[int], groupSize: int) -> bool:
    # Check if hand length is divisible by groupSize
    if len(hand) % groupSize != 0:
        return False

    # Count frequency of each card
    freq = Counter(hand)

    # Sort unique card values
    sorted_cards = sorted(freq.keys())

    # Try to form groups starting from each card
    for card in sorted_cards:
        # If this card is still available
        if freq[card] > 0:
            # Number of groups to form with this card as the start
            count = freq[card]
            # Check if we can form 'count' groups of groupSize consecutive cards
            for i in range(card, card + groupSize):
                if freq.get(i, 0) < count:
                    return False
                freq[i] -= count

    return True

# Example usage
hand1 = [1, 2, 3, 6, 2, 3, 4, 7, 8]
groupSize1 = 3
print(isNStraightHand(hand1, groupSize1))  # Output: True

hand2 = [1, 2, 3, 4, 5]
groupSize2 = 4
print(isNStraightHand(hand2, groupSize2))  # Output: False
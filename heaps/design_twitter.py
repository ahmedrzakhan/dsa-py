import heapq
from collections import defaultdict
from typing import List

class Twitter:
    def __init__(self):
        # Dictionary to store tweets: userId -> list of (timestamp, tweetId)
        self.tweets = defaultdict(list)
        # Dictionary to store followers: followerId -> set of followeeIds
        self.followers = defaultdict(set)
        # Timestamp to order tweets
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Add tweet with current timestamp
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Min heap to store tweets (timestamp, tweetId)
        min_heap = []
        # Include user's own tweets and tweets from followees
        users = self.followers[userId] | {userId}  # Union with user's own ID

        # Collect all tweets from relevant users
        for uid in users:
            for timestamp, tweetId in self.tweets[uid]:
                heapq.heappush(min_heap, (timestamp, tweetId))
                # Keep heap size at most 10
                if len(min_heap) > 10:
                    heapq.heappop(min_heap)

        # Extract tweets in reverse chronological order
        result = []
        while min_heap:
            result.append(heapq.heappop(min_heap)[1])
        return result[::-1]  # Reverse to get most recent first

    def follow(self, followerId: int, followeeId: int) -> None:
        # Prevent self-following
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Prevent self-unfollowing and ensure followee exists
        if followerId != followeeId:
            self.followers[followerId].discard(followeeId)

# Test case from Example 1
twitter = Twitter()
operations = ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
inputs = [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
outputs = []

for op, inp in zip(operations, inputs):
    if op == "Twitter":
        outputs.append(None)
    elif op == "postTweet":
        twitter.postTweet(inp[0], inp[1])
        outputs.append(None)
    elif op == "getNewsFeed":
        outputs.append(twitter.getNewsFeed(inp[0]))
    elif op == "follow":
        twitter.follow(inp[0], inp[1])
        outputs.append(None)
    elif op == "unfollow":
        twitter.unfollow(inp[0], inp[1])
        outputs.append(None)

print("Output:", outputs)

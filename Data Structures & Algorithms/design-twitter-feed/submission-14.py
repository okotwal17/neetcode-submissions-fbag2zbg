class Twitter:

    def __init__(self):
        self.time = 0
        self.followerMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((tweetId, self.time))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        print(self.followerMap, self.tweetMap)
        self.followerMap[userId].add(userId)
        for follower in self.followerMap[userId]:
            if self.tweetMap[follower]:
                index = len(self.tweetMap[follower]) - 1
                tweet, t = self.tweetMap[follower][index]
                heapq.heappush(heap, (t, tweet, follower, index - 1))
        res = []
        while heap and len(res) < 10:
            t, tweet, follower, index = heapq.heappop(heap)
            res.append(tweet)
            if index >= 0:
                tweet, t = self.tweetMap[follower][index]
                heapq.heappush(heap, (t, tweet, follower, index - 1))
        return res
                

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followerMap[followerId]:
            self.followerMap[followerId].remove(followeeId)
        

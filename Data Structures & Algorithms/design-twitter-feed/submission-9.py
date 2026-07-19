class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        self.followMap[userId].add(userId)
        for followerId in self.followMap[userId]:
            if followerId in self.tweetMap:
                index = len(self.tweetMap[followerId]) - 1
                count, tweetId = self.tweetMap[followerId][index]
                heap.append([count, tweetId, followerId, index - 1])

        heapq.heapify(heap)
        res = []
        while heap and len(res) < 10:
            count, tweetId, followerId, index = heapq.heappop(heap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followerId][index]
                heapq.heappush(heap, [count, tweetId, followerId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

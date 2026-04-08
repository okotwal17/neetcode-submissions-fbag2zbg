import heapq
class Twitter:

    def __init__(self):
        self.posts = []
        heapq.heapify(self.posts)
        self.followers = {}
        self.time = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts.append((self.time * -1, userId, tweetId))
        self.time += 1
        print(self.posts)

    def getNewsFeed(self, userId: int) -> List[int]:
        putBack = []
        res = []
        heapq.heapify(self.posts)
        remainingPosts = 10
        while len(self.posts) > 0 and remainingPosts != 0:
            if self.posts[0][1] == userId or (userId in self.followers and self.posts[0][1] in self.followers[userId]):
                temp = self.posts[0]
                res.append(temp[2])
                remainingPosts -= 1
            putBack.append(heapq.heappop(self.posts))
        while putBack:
            self.posts.append(putBack.pop())
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            self.followers[followerId].add(followeeId)
        else:
            self.followers[followerId] = {followeeId}
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].remove(followeeId)

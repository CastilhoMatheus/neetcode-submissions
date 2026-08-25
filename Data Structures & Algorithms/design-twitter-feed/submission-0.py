class Twitter:

    def __init__(self):
        self.count = 1
        self.userFollowers = defaultdict(set)
        self.feed = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feed[userId].append((self.count, tweetId))
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        updatedFeed = []
        heap = []
        allPosts = list(self.feed[userId])

        for p in self.userFollowers[userId]:
            allPosts += self.feed[p]
        
        for time, post in allPosts:
            heapq.heappush(heap, (-time, post))
        
        tenMost = 10

        while tenMost and heap:
            _, postId = heapq.heappop(heap)
            updatedFeed.append(postId)

            tenMost -= 1

        return updatedFeed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userFollowers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.userFollowers[followerId].discard(followeeId)

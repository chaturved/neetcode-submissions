class Twitter:
    def __init__(self):
        self.users = defaultdict(User)
        self.timestamp = 0
        self.k = 10

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users[userId].tweets.append((self.timestamp, tweetId))
        self.timestamp += 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        current_user = self.users[userId]
        heap = []
            
        sources = [current_user] + [self.users[fid] for fid in current_user.following]
        for user in sources:
            if user.tweets:
                i = len(user.tweets) - 1
                t, tweetId = user.tweets[i]
                heap.append((t, tweetId, user.tweets, i))
        
        heapq.heapify_max(heap)
            
        result = []
        while heap and len(result) < self.k:
            t, tweetId, tweets, i = heapq.heappop_max(heap)
            result.append(tweetId)
            if i > 0:
                i -= 1
                t, tweetId = tweets[i]
                heapq.heappush_max(heap, (t, tweetId, tweets, i))

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.users[followerId].following.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].following.discard(followeeId)

class User:
    def __init__(self):
        self.following = set()
        self.tweets = []
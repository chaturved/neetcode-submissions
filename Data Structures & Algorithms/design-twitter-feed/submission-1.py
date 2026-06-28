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
        visible_tweets = []
        
        all_tweets = list(current_user.tweets)
        for followeeId in current_user.following:
            all_tweets.extend(self.users[followeeId].tweets)
        
        for tweet in all_tweets:
            heapq.heappush(visible_tweets, tweet)
            if len(visible_tweets) > self.k:
                heapq.heappop(visible_tweets)
        
        return [tweetId for _, tweetId in sorted(visible_tweets, reverse=True)]

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
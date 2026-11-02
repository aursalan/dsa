import heapq

class Twitter:

    def __init__(self):
        self.post = {}
        self.following = {}
        self.time = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:

        self.time +=1

        if userId not in self.post:
            self.post[userId] = [(self.time, tweetId)]
            return
        
        self.post[userId].append((self.time, tweetId))

        return

    def getNewsFeed(self, userId: int) -> List[int]:
        
        if userId not in self.following and userId not in self.post:
            return []
        
        feed = []

        if userId not in self.following:

            index = -1
            length = len(self.post[userId])

            while len(feed) != 10:

                if index == -(length+1):
                    break

                feed.append(self.post[userId][index][1])
                index -=1
            
            return feed
        
        heap =  []

        if userId in self.post:
            heapq.heappush_max(heap, (self.post[userId][-1][0], userId, -1 ))

        if userId in self.following:
            for user in self.following[userId]:
                heapq.heappush_max(heap, (self.post[user][-1][0], user, -1))

        while len(feed)!=10:
            
            if heap:
                time, user, index = heapq.heappop_max(heap)
                
                feed.append(self.post[user][index][1])

                index -=1

                if index > -(len(self.post[user])+1):

                    time, tweetId = self.post[user][index]

                    heapq.heappush_max(heap, (time, user, index))

            else:
                break

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        
        if not followerId in self.following:
            self.following[followerId] = {followeeId}
            return
        
        self.following[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        
        if followerId in self.following and followeeId in self.following[followerId]:

            self.following[followerId].remove(followeeId)

            if len(self.following[followerId]) == 0:
                del self.following[followerId]


        
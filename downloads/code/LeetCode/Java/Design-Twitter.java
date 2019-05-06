public class Twitter {
    private static int timeStamp = 0;

    // userMap
    // 用来判断user是否存在
    private Map<Integer, User> userMap;
    
    // Class Tweet:
    // All tweets are connected
    private class Tweet{
        public int id;
        public int time;
        public Tweet next;

        public Tweet(int id){
            this.id = id;
            time = timeStamp++;
            next = null;
        }

    }

    // Class User
    private class User{
        public int id;
        // 记录这个user 关注了哪些其他user
        public Set<Integer> followed;
        // 记录和这个user有关的tweet
        public Tweet tweet_head;

        public User(int id){
            this.id = id;
            followed = new HashSet<>();
            // 先关注自己
            follow(id);
            tweet_head = null;
        }

        public void follow(int id){
            followed.add(id);
        }

        public void unfollow(int id){
            followed.remove(id);
        }

        // 最新的tweet是tweet_head
        public void post(int id){
            Tweet t = new Tweet(id);
            t.next = tweet_head;
            tweet_head = t;
        }
    }


    /** Initialize your data structure here. */
    public Twitter() {
        userMap = new HashMap<Integer, User>();
    }
    
    /** Compose a new tweet. */
    public void postTweet(int userId, int tweetId) {
        // 没有userID，就创建一个
        if(!userMap.containsKey(userId)){
            User u = new User(userId);
            userMap.put(userId, u);
        }
        userMap.get(userId).post(tweetId);
    }
    
    /** Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent. */
    public List<Integer> getNewsFeed(int userId) {
        List<Integer> ret = new LinkedList<>();
        if(!userMap.containsKey(userId)) return ret;

        // 和userId有关联的所有人
        Set<Integer> users = userMap.get(userId).followed;
        // 创建最小堆，按tweet时间排序
        PriorityQueue<Tweet> q = new PriorityQueue<Tweet>(users.size(), (a,b)->(b.time-a.time));
        // 把所有users的header放进去
        for(int user: users){
            Tweet head = userMap.get(user).tweet_head;
            if(head!=null)
                q.add(head);
        }

        int n = 0;
        while(!q.isEmpty() && n<10){
            Tweet t = q.poll();
            ret.add(t.id);
            n++;
            if(t.next!=null) q.add(t.next);
        
        }
        return ret;

    }
    
    /** Follower follows a followee. If the operation is invalid, it should be a no-op. */
    public void follow(int followerId, int followeeId) {
        if(!userMap.containsKey(followerId)){
            User u = new User(followerId);
            userMap.put(followerId, u);
        }

        if(!userMap.containsKey(followeeId)){
            User u = new User(followeeId);
            userMap.put(followeeId, u);
        }
        userMap.get(followerId).follow(followeeId);
    }
    
    /** Follower unfollows a followee. If the operation is invalid, it should be a no-op. */
    public void unfollow(int followerId, int followeeId) {
        if(!userMap.containsKey(followerId) || followerId==followeeId)
            return;
        userMap.get(followerId).unfollow(followeeId);
    }
}
/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter obj = new Twitter();
 * obj.postTweet(userId,tweetId);
 * List<Integer> param_2 = obj.getNewsFeed(userId);
 * obj.follow(followerId,followeeId);
 * obj.unfollow(followerId,followeeId);
 */

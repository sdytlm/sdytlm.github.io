---
layout: post
title: "Design Twitter"
date: 2016-09-10
comments: true
categories: LeetCode
tag: LeetCode
---


Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:

* postTweet(userId, tweetId): Compose a new tweet.
* getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
* follow(followerId, followeeId): Follower follows a followee.
* unfollow(followerId, followeeId): Follower unfollows a followee.

<!--more-->
### Solution

[python 实现](https://discuss.leetcode.com/topic/47838/python-solution/2)

{% include_code LeetCode/Python/Design-Twitter.py %}

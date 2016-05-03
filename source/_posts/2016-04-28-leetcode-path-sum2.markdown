---
layout: post
title: "Path Sum II"
date: 2016-04-28
comments: true
categories: LeetCode
tag: LeetCode
---

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

#### Example:
Given the below binary tree and sum = 22,
```
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
```

<!--more-->

### Solution
* DFS search all path (search until the leaf)

{% include_code LeetCode/Python/Path-Sum2.py %}

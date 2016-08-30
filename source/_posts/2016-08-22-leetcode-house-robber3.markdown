---
layout: post
title: "House Robber III"
date: 2016-08-22
comments: true
categories: LeetCode
tag: LeetCode
---


The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

#### Example 1:
```
     3
    / \
   2   3
    \   \ 
     3   1
```
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

#### Example 2:
```
     3
    / \
   4   5
  / \   \ 
 1   3   1
```
Maximum amount of money the thief can rob = 4 + 5 = 9.

<!--more-->
### Solution
* DFS: 返回值为抢劫节点node,和不抢劫node的收益
* 抢劫: 则不能抢劫子节点，return no_rob_L + no_rob_R + node.val
* 不抢劫: 则无法确定是否抢劫左右节点 return max(no_rob_R, rob_R)+max(no_rob_L, rob_L)
{% include_code LeetCode/Python/House-Robber3.py %}

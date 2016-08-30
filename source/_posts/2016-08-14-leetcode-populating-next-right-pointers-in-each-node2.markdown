---
layout: post
title: "Populating Next Right Pointers in Each Node II"
date: 2016-08-14
comments: true
categories: LeetCode
tag: LeetCode
---
What if the given tree could be any binary tree? Would your previous solution still work?

#### Note:

You may only use constant extra space.

#### Example,
Given the following binary tree,
```
         1
       /  \
      2    3
     / \    \
    4   5    7
```
After calling your function, the tree should look like:
```
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
```
<!--more-->
### Solution
* 一个firstnode记录每行第一个节点
* 一行一行遍历，没遍历一行把节点的字节点们都连好
* 一个lastNode记录上次访问节点

{% include_code LeetCode/Python/Populating-next-right-pointers-in-each-node2.py %}

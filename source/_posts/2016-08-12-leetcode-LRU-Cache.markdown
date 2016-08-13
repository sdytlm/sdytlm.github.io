---
layout: post
title: "LRU Cache"
date: 2016-08-12
comments: true
categories: LeetCode
tag: LeetCode
---

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.

set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

<!--more-->
### Solution
* 双链表+hash表
* tail: 指向新节点的位置
* root: 指向要被删除的节点位置
* entryFinder: 哈希表`<key,node>`，记录所有节点

{% include_code LeetCode/Python/LRU-Cache.py %}


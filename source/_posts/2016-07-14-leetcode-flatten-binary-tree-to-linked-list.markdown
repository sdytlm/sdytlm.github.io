---
layout: post
title: "Flatten Binary Tree to Linked List"
date: 2016-07-14
comments: true
categories: LeetCode
tag: LeetCode
---


Given a binary tree, flatten it to a linked list in-place.

#### Example
Given
```
         1
        / \
       2   5
      / \   \
     3   4   6
```
The flattened tree should look like:
```
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
```
#### Hints:
If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.

<!--more-->
### Solution
* Pre-order and put node into a stack.
* change the tree by the nodes in stack.
{% include_code LeetCode/Python/Flatten-Binary-Tree-to-Linked-List.py %}

---
layout: post
title: "Binary Tree Serialization"
date: 2016-03-02
comments: true
categories: LintCode
tag: LintCode 
---


Design an algorithm and write code to serialize and deserialize a binary tree. Writing the tree to a file is called 'serialization' and reading back from the file to reconstruct the exact same binary tree is 'deserialization'.

There is no limit of how you deserialize or serialize a binary tree, you only need to make sure you can serialize a binary tree to a string and deserialize this string to the original structure.

#### Example
An example of testdata: Binary tree {3,9,20,#,#,15,7}, denote the following structure:

```
  3
 / \
9  20
  /  \
 15   7
```
Our data serialization use bfs traversal. This is just for when you got wrong answer and want to debug the input.

You can use other method to do serializaiton and deserialization.

<!--more-->

### Solution
* Time: O(n)
* Use pre-order to implement it
* when you do de-serialization, remember to pop the list.
{% include_code LintCode/Binary-Tree-Serialization.py %}


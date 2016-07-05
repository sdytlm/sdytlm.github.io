---
layout: post
title: "Count Complete Tree Nodes"
date: 2016-07-05
comments: true
categories: LeetCode
tag: LeetCode
---


Given a complete binary tree, count the number of nodes.

`A Complete binary tree: is a binary tree in which all interior nodes have two children and all leaves have the same depth or same level`


In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

<!--more-->
### Solution
* 最后一层可能不满
{% include_code LeetCode/Python/Count-Complete-Tree-Nodes.py %}

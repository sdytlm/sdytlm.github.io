---
layout: post
title: "Implement Trie"
date: 2016-07-26
comments: true
categories: LeetCode
tag: LeetCode
---


Implement a trie with insert, search, and startsWith methods.

#### Note:
You may assume that all inputs are consist of lowercase letters a-z.

<!--more-->

### Solution
* 本题考查字典树数据结构的基础知识。

* Trie使用孩子表示法存储，TrieNode为字典树的节点，包含属性childs和isWord。

* 其中childs为dict，存储当前节点的后代节点；isWord为布尔值，表示当前节点是否存储了一个单词。

{% include_code LeetCode/Python/Implement-Trie.py %}

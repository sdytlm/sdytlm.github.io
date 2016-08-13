---
layout: post
title: "Add and Search Word"
date: 2016-08-09
comments: true
categories: LeetCode
tag: LeetCode
---


Design a data structure that supports the following two operations:

```
void addWord(word)
bool search(word)
```
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

#### For example:
```
addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
```
#### Note:
You may assume that all words are consist of lowercase letters a-z.

<!--more-->
### Solution
* Trie Tree
{% include_code LeetCode/Python/Add-and-Search-Word.py %}

---
layout: post
title: "Generate Parentheses"
date: 2016-07-08
comments: true
categories: LeetCode
tag: LeetCode
---


Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

#### Example 
given n = 3, a solution set is:

```
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
```

<!--more-->
### Solution
* l: len of left parenthese you need to fill
* r: len of right parenthese you need to fill
* r should be always >= l

{% include_code LeetCode/Python/Generate-Parentheses.py %}

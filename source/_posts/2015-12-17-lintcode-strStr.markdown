---
layout: post
title: "strStr"
date: 2015-12-17
comments: true
categories: LintCode
tag: LintCode
---

### strStr
`For a given source string and a target string, you should output the first index(from 0) of target string in source string.`

`If target does not exist in source, just return -1.`

#### Example

If source = "source" and target = "target", return -1.

If source = "abcdabcdefg" and target = "bcd", return 1.


#### Challenge
O(n^2) is acceptable. Can you implement an O(n) algorithm? (hint: KMP)

<!-- more -->

### Solution
Be careful about the corner cases. (e.g. NULL, emptry string)

{% include_code LintCode/strStr.py %} 

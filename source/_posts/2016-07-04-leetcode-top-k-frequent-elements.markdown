---
layout: post
title: "Top K Frequent Elements"
date: 2016-07-04
comments: true
categories: LeetCode
tag: LeetCode
---

Given a non-empty array of integers, return the k most frequent elements.

#### Example:
Given [1,1,1,2,2,3] and k = 2, return [1,2].

#### Note: 
* You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
* Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

<!--more-->
### Solution

#### Java Solution: bucket sort
{% include_code LeetCode/Java/Top-K-Frequent-Elements.java %}

#### Python Solution

* Sort dict by value
```
import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(1))
sorted_x will be a list of tuples sorted by the second element in each tuple. dict(sorted_x) == x.

```
* Sort dict by key
```
import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(0))
```

{% include_code LeetCode/Python/Top-K-Frequent-Elements.py %}

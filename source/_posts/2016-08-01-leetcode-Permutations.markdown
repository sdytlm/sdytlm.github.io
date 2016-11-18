---
layout: post
title: "Permutations"
date: 2016-08-01
comments: true
categories: LeetCode
tag: LeetCode
---

Given a collection of distinct numbers, return all possible permutations.

#### Example:
[1,2,3] have the following permutations:
```
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```

<!--more-->
### Solution
* Java: 构造
```
Then, 2 can be added in front or after 1. So we have to copy the List<Integer> in answer (it's just {1}), add 2 in position 0 of {1}, then copy the original {1} again, and add 2 in position 1. Now we have an answer of {2,1},{1,2}. There are 2 lists in the current answer.

Then we have to add 3. first copy {2,1} and {1,2}, add 3 in position 0; then copy {2,1} and {1,2}, and add 3 into position 1, then do the same thing for position 3.
```
{% include_code LeetCode/Java/Permutations.java %}

* Python: 减枝
{% include_code LeetCode/Python/Permutations.py %}

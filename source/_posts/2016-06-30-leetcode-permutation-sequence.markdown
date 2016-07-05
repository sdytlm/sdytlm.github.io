---
layout: post
title: "Permutation Sequence"
date: 2016-06-30
comments: true
categories: LeetCode
tag: LeetCode
---


The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,

We get the following sequence (ie, for n = 3):

```
"123"
"132"
"213"
"231"
"312"
"321"
```

Given n and k, return the kth permutation sequence.

#### Note
Given n will be between 1 and 9 inclusive.

<!--more-->
### Solution
* The first digit is k/(n-1)!, then let k = k % (n-1)! and remove this digit from num. 
* The second digit is k/(n-2)!, then let k = k % (n-2)! and remove this digit from num and so on.

{% include_code LeetCode/Python/Permutation-Sequence.py %}

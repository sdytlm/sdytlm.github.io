---
layout: post
title: "Shuffle an Array"
date: 2016-08-13
comments: true
categories: LeetCode
tag: LeetCode
---
Shuffle a set of numbers without duplicates.

#### Example:

```
// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
```

<!--more-->
### Solution

* 对于每个index, 在[0,index]中产生随机新的newindex, 然后交换位置这样可保证概率都是1/n

{% include_code LeetCode/Python/Shuffle-an-Array.py %}

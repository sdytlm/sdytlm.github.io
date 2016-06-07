---
layout: post
title: "Next Permutation"
date: 2016-06-02
comments: true
categories: LeetCode
tag: LeetCode
---


Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
```
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
```

<!--more-->
### Solution
* 第一步找出一个k，使得k之后的为递减序列。
* 接下来，我们需要找到一个最大的下标L使得 a[k]<a[L] （就是说递减序列中最小的元素）
* 交换a[k]和a[L]之后，对k+1之后的逆置即可（在纸上试试），这样就变成了升序。
* eg:
1 4 3  2  k=0 L=3  swap-> 2431 逆置-> 2134

{% include_code LeetCode/Python/Next-Permutation.py %}

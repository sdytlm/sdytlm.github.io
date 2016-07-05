---
layout: post
title: "Unique Binary Search Trees"
date: 2016-06-30
comments: true
categories: LeetCode
tag: LeetCode
---

Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

#### Example
Given n = 3, there are a total of 5 unique BST's.

```
   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```

<!--more-->
### Solution
* 对于任意以i为根节点的二叉树，它的左子树的值一定小于i，也就是[0, i - 1]区间，而右子树的值一定大于i，也就是[i + 1, n]。假设左子树有m种排列方式，而右子树有n种，则对于i为根节点的二叉树总的排列方式就是m x n。

* 我们使用dp[i]表示i个节点下面二叉树的排列个数，那么dp方程为:

* dp[i] = sum(dp[k] * dp[i - k -1])

{% include_code LeetCode/Python/Unique-Binary-Search-Trees.py %}

---
layout: post
title: "Three Sum"
date: 2015-12-28
comments: true
categories: LintCode
tag: LintCode
---

### 3Sum

`Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.`

#### Example
For example, given array S = {-1 0 1 2 -1 -4}, A solution set is:

(-1, 0, 1)
(-1, -1, 2)


#### Note
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)

The solution set must not contain duplicate triplets.
<!-- more -->


### Solution
* Time: O(N^2), Space O(N)

```
S = {-1 0 1 2 -1 -4}
排序后：
S = {-4 -1 -1 0 1 2}
      ↑  ↑        ↑
      i  j        k
         →        ←
i每轮只走一步，j和k根据S[i]+S[j]+S[k]=ans和0的关系进行移动，且j只向后走（即S[j]只增大），k只向前走（即S[k]只减小）
如果ans>0说明S[k]过大，k向前移；如果ans<0说明S[j]过小，j向后移；ans==0即为所求。
```
* 注：当找到一组解时，需要移动i,j到下一个非重复位置 

{% include_code LintCode/Three-Sum.py %}

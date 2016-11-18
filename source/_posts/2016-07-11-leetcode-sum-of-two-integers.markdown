---
layout: post
title: "Sum of Two Integers"
date: 2016-07-11
comments: true
categories: LeetCode
tag: LeetCode
---

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

#### Example:
Given a = 1 and b = 2, return 3.

<!--more-->
### Solution

* for negative integers, do it in C++, because `>> 1` in C++ will not fill 1

* Java
{% include_code LeetCode/Java/Sum-of-Two-Integers.java %}


* Python
```
class Solution {
public:
	int getSum(int a, int b) {
		int ans = 0, carry = 0;
		for (int i = 0; i < 32; a >>= 1, b >>= 1, i++) {
			int lower_a = a & 1, lower_b = b & 1;
			ans |= (lower_a ^ lower_b ^ carry) << i;
			carry = (carry & lower_a) | (carry & lower_b) | (lower_a & lower_b);
		}
		return ans;
	}
};

```

---
layout: post
title: "Basic Calculator 2"
date: 2016-06-28
comments: true
categories: LeetCode
tag: LeetCode
---



Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, * , / operators and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.

#### Examples:
```
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
```

#### Note 
Do not use the eval built-in library function.

<!--more-->
### Solution
#### Java
{% include_code LeetCode/Java/Basic-Calculator2.java %}

#### Python
* 若当前运算符为乘除法，则马上对d与下一个运算数执行乘除运算，赋值给d；

* 若当前运算符为加减法，则对total与d执行func（加减）运算，赋值给total，并更新func；

{% include_code LeetCode/Python/Basic-Calculator2.py %}

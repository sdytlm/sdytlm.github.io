---
layout: post
title: "Mini Parser"
date: 2016-09-02
comments: true
categories: LeetCode
tag: LeetCode
---

Given a nested list of integers represented as a string, implement a parser to deserialize it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

#### Note: 
* You may assume that the string is well-formed:
* String is non-empty.
* String does not contain white spaces.
* String contains only digits 0-9, [, - ,, ].

#### Example 1:

Given s = "324",

You should return a NestedInteger object which contains a single integer 324.
#### Example 2:

Given s = "[123,[456,[789]]]",

Return a NestedInteger object containing a nested list with 2 elements:
```
1. An integer containing value 123.
2. A nested list containing two elements:
    i.  An integer containing value 456.
    ii. A nested list with one element:
         a. An integer containing value 789.
```

<!--more-->
### Solution

* 遍历字符串s，记当前字符为c

* 如果c为'-'，则将符号变量negmul置为-1

* 如果c为0-9，则利用变量sigma存储数字的值

* 如果c为'['，则新建一个类型为列表的NestedInteger并压栈

* 如果c为']'或者','：

** 若sigma非空，则将sigma * negmul加入栈顶元素；

** 将栈顶元素弹出记为top；若此时栈非空，将top加入栈顶元素；否则返回top

{% include_code LeetCode/Python/Mini-Parser.py %}

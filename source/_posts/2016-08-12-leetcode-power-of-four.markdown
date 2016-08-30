---
layout: post
title: "Power of Four"
date: 2016-08-12
comments: true
categories: LeetCode
tag: LeetCode
---

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

#### Example:
Given num = 16, return true. Given num = 5, return false.

#### Follow up: 
Could you solve it without loops/recursion?

<!--more-->
### Solution
用 n &(n-1) ==0 来判断是否是2的次方数，这里也先判断一下是否为2的次方数。然后再把不是4的次方数排除掉，比如8.

我们来看看2的次方数的规律：

```
1 => 1
10 => 2
100 => 4
1000 => 8
10000 => 16
100000 => 32
1000000 => 64
10000000 => 128
100000000 => 256
1000000000 => 512
10000000000 => 1024
100000000000 => 2048
1000000000000 => 4096
10000000000000 => 8192
100000000000000 => 16384
```

我们发现，每次不过是将1向左移动一个位置，然后低位补0（这不是废话么= =|||）

那么4的次方数就是将1向左移动两个位置喽 （还是废话（╯－＿－）╯╧╧）

观察一下位置，4的次方中的1只出现在奇数的位置上！就是说，上面的二进制从右往左，第1，3，5，……位置上。

So，如果我们与上一个可以在奇数上面选择位置的数，也就是 0101 0101 ……那么就把不是4次方的排除掉啦

0101 0101 …… 十六进制表示为： 0x55555555

{% include_code LeetCode/Python/Power-of-Four.py %}

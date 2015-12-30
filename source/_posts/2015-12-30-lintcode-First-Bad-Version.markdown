---
layout: post
title: "First Bad Version"
date: 2015-12-30
comments: true
categories: LintCode
tag: LintCode
---

### First Bad Version
The code base version is an integer start from 1 to n. One day, someone committed a bad version in the code case, so it caused this version and the following versions are all failed in the unit tests. Find the first bad version.

You can call isBadVersion to help you determine which version is the first bad one. The details interface can be found in the code's annotation part.

#### Example
```
Given n = 5:

isBadVersion(3) -> false
isBadVersion(5) -> true
isBadVersion(4) -> true
```
Here we are 100% sure that the 4th version is the first bad version.

#### Note
Please read the annotation in code area to get the correct way to call isBadVersion in different language. For example, Java is SVNRepo.isBadVersion(v)

#### Challenge
You should call isBadVersion as few as possible.

<!--more-->

### Solution
* Time: O(log n)
* Binary search [1,n] find the smallest value x (isBadVersion(x) == True)
{% include_code LintCode/First-Bad-Version.py %}

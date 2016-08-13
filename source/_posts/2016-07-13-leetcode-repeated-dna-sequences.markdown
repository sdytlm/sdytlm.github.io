---
layout: post
title: "Repeated DNA Sequences"
date: 2016-07-13
comments: true
categories: LeetCode
tag: LeetCode
---


All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

#### Example

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:

["AAAAACCCCC", "CCCCCAAAAA"].

<!--more-->
### Solution
* use hash map to store the appearance times of each 10-letter substring
* don't use substring as key, use 20bit number, use 2 bit to distinguish (A,C,G,T) 4 letters

{% include_code LeetCode/Python/Repeated-DNA-Sequence.py %}

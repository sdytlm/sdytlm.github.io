---
layout: post
title: "Ransom Note"
date: 2016-08-12
comments: true
categories: LeetCode
tag: LeetCode
---

Given  an  arbitrary  ransom  note  string  and  another  string  containing  letters from  all  the  magazines,  write  a  function  that  will  return  true  if  the  ransom   note  can  be  constructed  from  the  magazines ;  otherwise,  it  will  return  false.   

Each  letter  in  the  magazine  string  can  only  be  used  once  in  your  ransom  note.


Each letter in the magazine string can only be used once in your ransom note.

#### Note:
You may assume that both strings contain only lowercase letters.
```
canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
```

<!--more-->
### Solution

* hash_map: (character, 出现次数)
{% include_code LeetCode/Python/Ransom-Note.py %}


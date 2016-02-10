---
layout: post
title: "QEMU Compile SeaBios"
date: 2016-02-04
comments: true
categories: virtualization
tag: virtualization
---

You must follow the order:
```
in qemu/
make distclean
```
```
in rom/
make bios CONFIG_ROM_SIZE=256
```
```
in qemu/
./configure --target-list=x86_64-softmmu
```
```
in qemu/
make
make install
```


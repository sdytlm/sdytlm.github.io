---
layout: post
title: "Linux Disk Benchmark"
date: 2016-01-15
comments: true
categories: linux
tag: linux
---

For a complete benchmark suit in Linux, I would recommend `lmbench`. 
You will have the benchmark result for CPU, memory, network, disk etc.

### Simple Linux Disk Benchmark

Actually, you can rely on **dd** for simple disk performance evaluation

#### Test Write speed

```
dd if=/dev/zero of=tempfile bs=1M count=1024
```

#### Test Read speed from buffer

```
dd if=tempfile of=/dev/null bs=1M count=1024

```

#### Teest Real Read speed
Just clear the linux cache, then run dd

```
sysctl -w vm/drop_caches=3
dd if=tempfile of=/dev/null bs=1M count=1024
```

#### Test on external hard drive

External HD includes external HDD, USB flash drive, removable device etc.

Replace **tempfile** in the above command by your mount point

```
dd if=/dev/zero of=/media/user/MyUSB/tempfile bs=1M count=1024
```



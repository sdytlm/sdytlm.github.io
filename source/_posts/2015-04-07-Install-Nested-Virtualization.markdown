---
layout: post
title: "Build Nested KVM Virtualization"
date: 2015-04-07
comments: true
categories: virtualization
tag: virtualization
---

### Platform
* Dom0: Opensuse 13.1
* Host/Guest Hypervisor: KVM
* Guest OS: CentOS 


### Enable Nested in Host KVM
1. Check if nested is enabled in host hypervisor

```
cat /sys/module/kvm_intel/parameters/nested
```

if the result is `Y`. Nested virgualization in your host is open. Ohterwise you need to complete the followings

2. Modify /etc/default/grub

> GRUB_CMDLINE_LINX = "kvm-intel.nested=1 "

3. Update grub

```
grub2-mkconfig -o /boot/grub2/grub.cfg
```

4. Reboot and check again
 

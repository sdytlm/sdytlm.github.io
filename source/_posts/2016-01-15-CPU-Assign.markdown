---
layout: post
title: "Linux Cgroup assign dedicated CPUs for a VM"
date: 2016-01-15
comments: true
categories: virtualization
tag: virtualization
---

### Platform 
* Host: Linux-3.10
* Guest: Linux-3.10
* Host CPU#: 8
* Assigned CPUs: CPU #6

### Configure Cgroup


```
# Create another cgroup folder
mkdir /sys/fs/cgroup/cpuset/test

# You will get a bunch of files in test folder  after create the folder
# Assign the CPU 6 or you can replace 6 by "6-7" if you want more cpus assigned to the VM
echo 6 > /sys/fs/cgroup/cpuset/test/cpuset.cpus

# Assign the memory boundary
echo 0 > /sys/fs/cgroup/cpuset/test/cpuset.mems

```
### Modify your VM boot script

Add qemu process# into cgroup.procs

```
# Add the following line at the beginning
echo $$ > /sys/fs/cgroup/cpuset/test/cgroup.procs

# Add "exec" before qemu-system-x86_64 binary
exec qemu-system-x86_64 -enable-kvm -rtc base=utc,clock=vm,driftfix=none -bios bios.bin -device piix3-usb-uhci -soundhw ac97,hda -m 1024 -serial tcp::1223,server,nowait -net nic,macaddr=00:20:18:11:01:23,model=rtl8139,vlan=0 -net tap,vlan=0,script=/data/images/qemu-image/qemu-ifup0.sh -drive file=/data/images/qemu-image/opensuse-50G.raw,if=virtio,boot=on -name 23 -cpu core2duo -monitor stdio -smp sockets=1,cores=1,threads=1 -vnc :23
```

After that, run the boot script, you will see the qemu process number in `/sys/fs/cgroup/cpuset/test/cgroup.procs` and all threads in `/sys/fs/cgroup/cpuset/test/tasks`

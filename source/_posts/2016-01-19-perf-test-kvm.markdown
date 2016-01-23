---
layout: post
title: "Perf Evaluate KVM Performance"
date: 2016-01-19
comments: true
categories: virtualization
tag: virtualization
---


### Platform
* Guest: Opensuse with Linux3.10
* Host: Linux3.10
* virtio enabled?: Yes

### Boot VM
Boot A VM with virtio block
```
qemu-system-x86_64 -enable-kvm -rtc base=utc,clock=vm,driftfix=none -bios bios.bin \
-device piix3-usb-uhci -soundhw ac97,hda -m 1024 -serial tcp::1223,server,nowait \
-net nic,macaddr=00:20:18:11:01:23,model=rtl8139,vlan=0 \
-net tap,vlan=0,script=/data/images/qemu-image/qemu-ifup0.sh \
-drive file=/data/images/qemu-image/opensuse-50G.raw,if=virtio,boot=on \
-name 23 -cpu core2duo -monitor stdio -smp sockets=1,cores=1,threads=1 -vnc :23
```

### Count VMExit for block R/W

Create an empty file (1GB) and count how many VMExits happens.

On host Machine
```
perf kvm stat record -a ssh root@GuestIP "dd if=/dev/zero of=tempfile bs=1MB count=1024"
```
* -a: capture all VCPUs

### Read report
```
perf kvm stat report --event=vmexit
```
* You will get statistics about VMEXIT
* There are three event you can capture **vmexit**,**mmio**,**ioport** 

### Detailed report
* Boot the VM first
* On Host Machine

```
perf kvm record -a ssh root@GuestIP "dd if=/dev/zero of=tempfile bs=1MB count=1024"
```
* After that, You will get a file named **perf.data.guest**
* Run report command to look at it
```
perf kvm report
```

### collect performance data from the host
Add `--host` between `kvm` and `record`
```
perf kvm --host record -a ssh root@GuestIP "dd if=/dev/zero of=tempfile bs=1MB count=1024"
```
You will get a file namedd **perf.data.kvm**
```
perf kvm report --input perf.data.kvm
```


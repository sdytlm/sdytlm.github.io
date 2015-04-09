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

2. `Modify /etc/default/grub

> GRUB_CMDLINE_LINX = "kvm-intel.nested=1 "

3. Update grub

```
grub2-mkconfig -o /boot/grub2/grub.cfg
```

4. Reboot and check again

### Install the guest Hypervisor

I use the raw disk as the VM partition
```
virt-install --name=centos5.6 --os-variant=RHEL5 --ram=1024 --vcpus=1 --disk path=/dev/sda4,format=raw,bus=virtio --accelerate --cdrom /Your DVD / --vnc --vncport=5910 --vnclisten=0.0.0.0 --network bridge=br0,model=virtio --noautoconsole

```



### Virsh Command

* Launch a VM

```
virsh start domain name
```

* Undefine a VM
```
virsh destroy domain name
virsh undefine domain name
```

* Connect a VM
```
virt-viewer -c qemu:///system  domain name
```



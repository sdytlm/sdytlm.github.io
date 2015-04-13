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

<!--more -->

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

### Configure the Guest Hypervisor

* Disable cache on guest disk
In xml file, do
```
<driver name='qemu' type='raw' cache='none'/>
```

* Enable VMX in guest CPU
In xml file, do
```
<cpu match='exact'>
  <model>core2duo</model>
 <feature policy='require' name='vmx'/>
</cpu>
```

* Check guest CPU feature in host
In host OS

```
ps -ef | grep qemu-kvm
```

* Disable SELinux
In SELinux
```
SELINUX=permissive
```

* Configure network

```
service NetworkManager stop
chkconfig NetworkManager off
chkconfig network on
yum install bridge-utils

```
eth0:

```
DEVICE=eth0
TYPE=Ethernet
ONBOOT=yes
NM_CONTROLLED=yes
BRIDGE=br0
```
br0

```
DEVICE=br0
NM_CONTROLLED=yes
ONBOOT=yes
TYPE=Bridge
BOOTPROTO=dhcp
```
reboot your computer


* Compile and Install QEMU

```
./configure
make
make install
```

* Install libvirt and management tool

```
yum install libvirt-client virt-viewer guestfish libguestfs-tools virt-top libvrt python-virtinst 
```
* Launch libvirtd

```
service libvirtd start
chkconfig libvirtd on
```

* Check if libvirtd is turned on

```
virsh list
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

* Delete a VM

```
virsh destroy domain name
virsh undefine domain name
```

* Add VCPU to a VM

```
virsh shutdown domain Name
virsh edit domain name
```
do this
```
edit <vcpu placement='static'>4</vcpu>
virsh create /etc/libvirt/qemu/yourconfig.xml
```

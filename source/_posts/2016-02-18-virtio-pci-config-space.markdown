---
layout: post
title: "virtio-pci device PCI Config space"
date: 2016-02-18
comments: true
categories: virtualization
tag: virtualization
---

### Decode the virtio pci config space

* Device: virtio-serial
* QEMU: 2.5
* Helper: PCI peek program (written by myself)
    * open `/dev/mem`
    * use linux mmap to map the device address to virtual address (address must be page aligned.
    * read the content from the virtual address


#### Virtio pci config space
<img src="{{ root_url }}/images/virtio-pci-space.png"/>

<!--more-->
#### Decode Manually
* Check pci capability list (offset `33h`)
* Get the entry point of capability list: `40h`
* Read offset `40h` and get the first capability id `0x11`
* Google the capability id for pci config and find `0x11` means `MSIX`
* Read the following bits based on the MSIX spec

<img src="{{ root_url }}/images/msix-capability-structure.png"/>

* read MSIX capability structure in offset `40h` 
    * `11 00 01 80` => `80 01 00 11`: MSIX capability ID, table size (2) including one empty entry, MSIX enabled, no next capability
    * `01 00 00 00` => `00 00 00 01`: read MSIX table address in `BAR1` (2nd bar), offset: `00h`
    * `01 08 00 00` => `00 00 08 01`: read MSIX function pending bit array address in `BAR1`, offset: `08h`

* check BAR 1 and find the start address is `0xfebd6000` (device address)
* peek and get the start address (`0xfe00000`) of the first MSIX table
* Note: BAR 0 is used as I/O bar. 

``` 
./peek.o 0xfebd6000 0x0
>> 0xfee00000 
``` 

* peek `0xfebd6000 + 08h` and get the start point of MSIx pending bit array address
* The MSIX table entry struct is as follow

<img src="{{ root_url }}/images/msix-table-entry.png"/>
 

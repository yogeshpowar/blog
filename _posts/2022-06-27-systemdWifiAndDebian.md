---
layout: posts
title: Systemd, wifi and Debian
tags:  Linux Wireless Debian
desc: About configuring WiFi on Debian GNU Linux
---

# Systemd, wifi and Debian

[systemd](https://systemd.io/) gets the control from the Linux kernel on boot
for managing services on the GNU/Linux system.

Configuring Wi-Fi on Debian GNU/Linux system could be tricky.

Following steps worked for my system

* Debian 11

```
$ cat /etc/issue
Debian GNU/Linux 11 \n \l
$
```

* Wireless device name is `wlp4s0`

```
$ iw dev | grep Interface
        Interface wlp4s0
$
```

* `wlp4s0` entry is not configured in `/etc/network/interfaces`

```
$ cat /etc/network/interfaces | grep wlp4s0 | grep -v ^#
$
```

* Create `wlp4s0` entry in system'd network

```
$ pwd
/etc/systemd/network
$ cat wlan.network
[Match]
Name=wlp4s0

[Network]
DHCP=ipv4
$
```

* Confirm if `wpa_supplicant-nl80211@service` is present in systemd

```
$ cat /lib/systemd/system/wpa_supplicant-nl80211@.service
[Unit]
Description=WPA supplicant daemon (interface- and nl80211 driver-specific
version)
Requires=sys-subsystem-net-devices-%i.device
After=sys-subsystem-net-devices-%i.device
Before=network.target
Wants=network.target

# NetworkManager users will probably want the dbus version instead.

[Service]
Type=simple
ExecStart=/sbin/wpa_supplicant
-c/etc/wpa_supplicant/wpa_supplicant-nl80211-%I.conf -Dnl80211 -i%I

[Install]
Alias=multi-user.target.wants/wpa_supplicant-nl80211@%i.service
$
```

* Confirm `wpa_supplicant-nl80211-wlp4s0.conf` file exists

```
$ cat /etc/wpa_supplicant/wpa_supplicant-nl80211-wlp4s0.conf  | grep -v ^#
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
ctrl_interface_group=0
update_config=1
network={
    ssid="FreeVirus"
    scan_ssid=1
    key_mgmt=WPA-PSK
    psk="n0Vacc1ne4Th1s"
}
$
```

* Enable network, resolved and wpa_supplicant services

```
systemct enable systemd-networkd.service
systemctl enable systemd-resolved.service
systemctl enable wpa_supplicant-nl80211@wlp4s0.service
```

* Reboot and get your machine connected to the wifi automatically on bootup.

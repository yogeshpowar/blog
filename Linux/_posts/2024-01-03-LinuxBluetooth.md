---
layout: posts
title: Bluetooth on Debian
tags: GNU/Linux Bluetooth
desc: Running Bluetooth on Debian CLI
---

### Installation

* Install BlueZ and Blueman
```
sudo apt install bluez*
sudo apt install blueman
```

### Configuration

* Enable the service
```
sudo systemctl enable bluetooth.service
```

### Connect

* Use `bluetoothctl` to connect to the daemon
```
bluetoothctl
```
* Powar on
```
bluetoothctl power on
bluetoothctl discoverable on
```
* Connect from other bt device; it will ask some `yes` questions and will also
  show some pin.
* Trust the device (device mac can be seen with `show`)
```
bluetoothctl trust 12:34:44:14:00:FF
```

### Receive file

* Utility is `bt-obex`
* This will download the files in the current directory
```
bt-obex -s .
```
* Start sending the file from the other device (say mobile)
* It will show how much `%` is complete.

### Disconnect

* Finally, just disconnect the bt link
```
bluetoothctl disconnect
```

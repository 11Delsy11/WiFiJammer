# NOTES:


> **This tool only supports linux atm.**

> **Your wireless card must support monitor mode for this to work**

> **This tool relies on airmon-ng and scapy and may not work with some wifi interfaces including Qualcomm Atheros QCA9377**

> **By using this, you agree that you cannot hold the contributors responsible for any misuse**

## Installation

#### For Debian-based GNU/Linux distributions

To use the application, type in the following commands in GNU/Linux terminal.
```shell script
sudo apt install git
git clone https://github.com/11Delsy11/WiFiJammer.git
cd WiFiJammer
bash b.sh
```

## Usage

1. find the name of your wifi interface using `cat /proc/net/wireless | perl -ne '/(\w+):/ && print $1'`
2. put your wifi in monitoring mode using `airmon-ng start <your interface>`
3. scan all the nearby APs with airmon-ng and save them in a csv file ` airodump-ng <your interface> -w <file name> --output-format csv ` 
4. now you can run file with `python3 WiFiJammer.py -a <your csv file address> -NC <your interface>`

* you can use -h argument for more info
 
 


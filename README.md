# Description
just a wifi jammer that use airmon-ng and scapy to jamming on linux

# Setup
* `git clone https://github.com/11Delsy11/WiFiJammer.git`

# Use
1. first run this command `airmon-ng start <your interface>`
2. you need to make an airmon-ng csv file with ` airodump-ng <your interface> -w <file name> --output-format csv ` 
3. now you can run file with `python3 WiFiJammer.py -a <your csv file address> -NC <your interface>`
* you can use -h to see other arguments
 



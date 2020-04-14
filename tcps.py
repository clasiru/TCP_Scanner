#!/usr/bin/env python

#Simple Port Scanner v1.0
#Author: Chandika Lasiru
#Blog: https://clasiru.blogspot.com

import socket
import sys
import urllib.request
import time
import argparse

print ()
print ("████████╗ ██████╗██████╗ ███████╗");
print ("╚══██╔══╝██╔════╝██╔══██╗██╔════╝");
print ("   ██║   ██║     ██████╔╝███████╗");
print ("   ██║   ██║     ██╔═══╝ ╚════██║");
print ("   ██║   ╚██████╗██║     ███████║");
print ("   ╚═╝    ╚═════╝╚═╝     ╚══════╝");
print ("                      TCP Scanner");
print ("                   by Area Master");
print ()

def google_ok():
    try:
        urllib.request.urlopen('https://www.google.com', timeout=10);
        return True
    except: 
        return False
    return True

def yahoo_ok():
    try:
        urllib.request.urlopen('https://www.yahoo.com', timeout=10);
        return True
    except: 
        return False
    return True

def target_ok():
    try:
        urllib.request.urlopen('http://'+ip, timeout=10);
        return True
    except: 
        return False
    return True

def is_valid_host():
    try:
        socket.gethostbyname(arghost)
        return True
    except:
        return False

def is_valid_minport():
    try:
        int(argsport)
        return True
    except ValueError:
        return False

def is_valid_maxport():
    try:
        int(argeport)
        return True
    except ValueError:
        return False

def scan_tcp_range():
    print ()
    print ('[*] Scanning range: ', int(argsport), 'to', int(argeport))
    print ()
    print ('[*]  PORT     STATE    SERVICE')
    for tcprange in range(int(argsport), int(argeport)+1):
        stcprange = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
        contcprange = stcprange.connect_ex((ip, tcprange))
        try:
            service = socket.getservbyport(tcprange)
        except socket.error:
            service = ''
            pass
        if(contcprange == 0) :
            print ('[+] %d /TCP  OPEN' % (tcprange),'   ', service)
        else:
            print ('[ ] %d /TCP  CLOSE' % (tcprange))
        stcprange.close()

def scan_tcp_list():
    print ()
    print ('[*] Scanning Port List: ', argportlist)
    print ()
    print ('[*]  PORT     STATE    SERVICE')
    for tcplist in list(map(int,argportlist)):
        stcplist = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
        contcplist = stcplist.connect_ex((ip, tcplist))
        try:
            service = socket.getservbyport(tcplist)
        except socket.error:
            service = ''
            pass
        if(contcplist == 0) :
            print ('[+] %d /TCP  OPEN' % (tcplist),'   ', service)
        else:
            print ('[ ] %d /TCP  CLOSE' % (tcplist))
        stcplist.close()

def scan_tcp_default():
    print ()
    print ('[*] Scanning Default Port List: ', argdefault)
    print ()
    print ('[*]  PORT     STATE    SERVICE')
    for tcpdef in list(map(int,argdefault)):
        stcpdef = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
        contcpdef = stcpdef.connect_ex((ip, tcpdef))
        try:
            service = socket.getservbyport(tcpdef)
        except socket.error:
            service = ''
            pass
        if(contcpdef == 0) :
            print ('[+] %d /TCP  OPEN' % (tcpdef),'   ', service)
        else:
            print ('[ ] %d /TCP  CLOSE' % (tcpdef))
        stcpdef.close()
        
parser = argparse.ArgumentParser('python3 tcps.py', description='Simple Port Scanner for scanning TCP ports in target hosts')

parser.add_argument('--host', default='127.0.0.1', help="Enter IP address or Hostname", type=str)
parser.add_argument('--default', help="Use default port range (21, 22, 23, 80, 443)", action="store_true")
parser.add_argument('--list', help="Enable port(s) list scanning", action="store_true")
parser.add_argument('--pL', default=[21, 22, 23, 80, 443],  help='Ports for port list scanning (Eg: --pL 21 22 80)', nargs='+')
parser.add_argument('--range', help="Enable port range scanning", action="store_true")
parser.add_argument('--sP', default='1', help='Starting port number for port range scanning (between 1 and 65534)', type=int)
parser.add_argument('--eP', default='65534', help='Ending port number for port range scanning (between 1 and 65534)', type=int)

args = parser.parse_args()

arghost = args.host
argportlist = args.pL
argsport = args.sP
argeport = args.eP
    
ip = socket.gethostbyname(arghost)

localtime = time.asctime(time.localtime(time.time()))

if len(sys.argv)==1:
    parser.print_help();
    sys.exit(0)

if is_valid_host():  
    print ('[*] Scanning started at', localtime)
    if google_ok() or yahoo_ok():
        print ('[*] Internet Status: Online')
    else:
        print ('[*] Internet: Offline')
    print ('[*] Target Host: ', ip)
    if target_ok():
        print ('[*] Target Status: Appears Online')
    else:
        print ('[*] Target Status: Appears Offline')
    if args.list: 
        scan_tcp_list()
    elif args.range:
        scan_tcp_range()
    elif args.default:
        argdefault = [21, 22, 23, 80, 443]
        scan_tcp_default()
    else:
        print ()
        print ('[*] Nothing to scan. Options are wrong !')
    print ()
    print ('[*] Scanning finished at', localtime)
    print ('[*] Have a nice day !')
    
else:
    print ('[*] Host: ', arghost, 'is invalid')

sys.exit(0)

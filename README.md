# TCP Scanner (TCPS)
##Simple Port Scanner for scanning TCP ports in target hosts

This is a straightforward program created by using Python version Three. You can perform TCP port scanning against any host within Intranet, Extranet & Internet by this tool. This tool can scan according to a given port range or a custom port(s) list or a default port range.

How to use this tool
-


1. Usage:
```
usage: python3 tcps.py [-h] [--host HOST] [--default] [--list] [--pL PL [PL ...]] [--range] [--sP SP] [--eP EP]

optional arguments:
  -h, --help        show this help message and exit
  --host HOST       Enter IP address or Hostname
  --default         Use default port range (21, 22, 23, 80, 443)
  --list            Enable port list scanning
  --pL PL [PL ...]  Ports for port list scanning (Eg: --pL 21 22 80)
  --range           Enable port range scanning
  --sP SP           Starting port number for port range scanning (between 1 and 65534)
  --eP EP           Ending port number for port range scanning (between 1 and 65534)
```

2. Perform default ports scan:
```
python3 tcps.py --host <target-host> --default
```

3. Perform port(s) list scan:
```
python3 tcps.py --host <target-host> --list --pL 21 22 80 443
```

4. Perform port range scan:
```
python3 tcps.py --host <target-host> --range --sP 79 --eP 81
```

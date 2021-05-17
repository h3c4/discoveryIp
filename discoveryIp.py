#!/usr/bin/python3
#coding: utf-8

import socket as s
import os, sys
import time

#Author:H3C4

def error():
    if len(sys.argv) != 2:
        print("\n[!] Use: python3 " + sys.argv[0] + " <domain name>\n")
        sys.exit(1)
    else :
        print("\n\t[x] Sorry, we can't find the ip address")


if __name__ == '__main__':

    try:
        url = str(sys.argv[1])
        print('\n[!] Decrypting host...')
        time.sleep(2)
        print(f'\n\t[*] The ip address of < {url} > is  {s.gethostbyname(url)}')

    except :
        error()

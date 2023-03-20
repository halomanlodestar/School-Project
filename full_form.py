import csv
from io import TextIOWrapper
import math
import random

def askFullFormNoFile():
   
   data = [['NIU', 'Network Interface Unit'], ['MAC', 'Media Access Control'], ['TCP', 'Transmission Control Protocol'], ['IP', 'Internet Protocol'], ['PAN', 'Personal Area Network'], ['LAN', 'Local Area Network'], ['MAN', 'Metropolitan Area Network'], ['WAN', 'Wide Area Network'], ['UTP', 'Unshielded Twisted Pair'], ['STP', 'Shielded Twisted Pair'], ['Mbps', 'Mega bits per sec'], ['EMI', 'Electro Magnetic Interference'], ['RJ', 'Registered Jack'], ['Wi-Fi', 'Wireless Fidelity'], ['VPN', 'Virtual Private Network'], ['NIC', 'Network Interface Card'], ['DNS', 'Domain Name System'], ['ISP', 'Internet Service Provider'], ['URL', 'Uniform Resource Locator'], ['HTTP', 'Hyper Text Transfer Protocol'], ['FTP', 'File Transfer Protocol'], ['TDMA', 'Time division Multiple Access'], ['CDMA', 'Code Division Multiple Access'], ['SIM', 'Subscriber Identity Module'], ['EDGE', 'Enhanced Data rates for GSM Evolution'], ['UMTS', 'Universal Mobile Telecommunications System'], ['LTE', 'Long Term Evolution'], ['GPRS', 'General Packet Radio Service'], ['ICMP', 'Internet Control Message Protocol'], ['SMTP', 'Simple Mail Transfer Protocol'], ['VoIP', 'Voice Over Internet Protocol'], ['SIP', 'Session Initiation Protocol'], ['POP', 'Post Office Protocol'], ['IMAP', 'Internet Mail Access Protocol'], ['SSH', 'Secure Shell'], ['NFC', 'Near-Field Communication'], ['SLIP', 'Serial Line Internet Protocol'], ['PPP', 'Point to Point Protocol'], ['SNMP', 'Simple Network Management Protocol']]

   while (data):
        [Q, A] = data.pop(math.floor(random.random() * len(data)))
        Input = str(input(f"{Q}: "))
        if Input.lower() != A.lower():
          print(f"Wrong Answer!! Correct one is '{A}'")
          data.append([Q, A])
          continue

        print("Correct Answer")

askFullFormNoFile()

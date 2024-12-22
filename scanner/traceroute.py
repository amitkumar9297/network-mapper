from scapy.all import IP, ICMP, sr1

def traceroute(target, max_hops=30):
    for ttl in range(1, max_hops + 1):
        pkt = IP(dst=target, ttl=ttl) / ICMP()
        reply = sr1(pkt, timeout=1, verbose=0)
        if reply is None:
            print(f"{ttl}: * * *")
        else:
            print(f"{ttl}: {reply.src}")
            if reply.src == target:
                break

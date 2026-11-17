from scapy.all import rdpcap, Ether, IP, TCP, UDP

# Read packets captured by Wireshark
packets = rdpcap("capture.pcapng")

for i, packet in enumerate(packets, 1):

    print("\n" + "=" * 60)
    print(f"Packet {i}")
    print("=" * 60)

    # 1. Ethernet Header
    if Ether in packet:
        eth = packet[Ether]

        print("\n--- Ethernet Header ---")
        print("Source MAC      :", eth.src)
        print("Destination MAC :", eth.dst)
        print("EtherType       :", hex(eth.type))

    # 2. IP Header
    if IP in packet:
        ip = packet[IP]

        print("\n--- IP Header ---")
        print("Source IP       :", ip.src)
        print("Destination IP  :", ip.dst)
        print("Version         :", ip.version)
        print("Header Length   :", ip.ihl)
        print("TTL             :", ip.ttl)
        print("Protocol        :", ip.proto)

    # 3. TCP Header
    if TCP in packet:
        tcp = packet[TCP]

        print("\n--- TCP Header ---")
        print("Source Port     :", tcp.sport)
        print("Destination Port:", tcp.dport)
        print("Sequence Number :", tcp.seq)
        print("Acknowledgment   :", tcp.ack)
        print("Flags           :", tcp.flags)
        print("Window Size     :", tcp.window)

    # 4. UDP Header
    if UDP in packet:
        udp = packet[UDP]

        print("\n--- UDP Header ---")
        print("Source Port     :", udp.sport)
        print("Destination Port:", udp.dport)
        print("Length          :", udp.len)
        print("Checksum        :", udp.chksum)
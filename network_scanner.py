import scapy.all as scapy
import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--target', dest='target', help='Target IP Address/Addresses')
    options = parser.parse_args()

    # Quit if arg is missing
    if not options.target:
        parser.error("[-] Please specify an IP Address or Addresses, use --help for more info.")
    return options

def scan(ip):
    """
    In this function, we’ll have to do the following things to be able to scan the network:
        Create an ARP Request.
        Create an Ethernet Frame.
        Place the ARP Request inside the Ethernet Frame.
        Send the combined frame and receive responses.
        Parse the responses and print the results.
    """
    arp_req_frame = scapy.ARP(pdst = ip)
    """
    useful extra tricks
    breakpoint()

    print(scapy.ls(scapy.ARP()))
    print(arp_req_frame.summary())
    print(arp_req_frame.show())
    """

    """
    The ARP Request is supposed to be broadcasted (transmitted to every IP Address in a network). 
    Therefore, to broadcast the ARP Request we set the Destination Address field of Ethernet field to 
    ‘ff:ff:ff:ff:ff:ff’ as this is a broadcast MAC Address. 
    """
    broadcast_ether_frame = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")

    """
    The next step is to combine the ARP Request and the Ethernet Frame. We did this using scapy
    because it allows a very convenient way to combine frames. The code below creates a new frame 
    by combining the ARP Request and Ethernet Frame using the ‘/’ sign. This is because scapy 
    allows us to combine frames using this.
    """
    broadcast_ether_arp_req_frame = broadcast_ether_frame / arp_req_frame
    """
    Now if we call the show() function we can see that the final combined frame consists of both
    Ethernet and ARP Request.
    """

    (answered_list, unanswered_list) = scapy.srp(broadcast_ether_arp_req_frame, timeout=1, verbose=False)
    breakpoint()
    result = []

    for i in range(0,len(answered_list)):
        client_dict = {"ip": answered_list[i][1].psrc, "mac": answered_list[i][1].hwsrc}
        result.append(client_dict)
    
    return result

options = get_args()
scanned_output = scan(options.target)


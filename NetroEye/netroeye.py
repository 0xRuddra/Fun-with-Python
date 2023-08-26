# Importing necessary modules
import sys
import socket
import argparse
from mac_vendor_lookup import MacLookup
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import scapy.all as scapy
import ipaddress
from tqdm import tqdm
import requests

# A dictionary to store alive hosts
alive = {}

# Define a class NetroEye for the network scanning
class NetroEye:
    def __init__(self, target):
        self.host = target
        self.packet()

    # Create an Ethernet frame and ARP request frame
    def packet(self):
        ethernet_frame = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
        arp_req_frame = scapy.ARP(pdst=self.host)
        packet = ethernet_frame / arp_req_frame
        self.packet = packet
        self.broadcast()

    # Send ARP packets and collect responses
    def broadcast(self):
        answered, unanswered = scapy.srp(self.packet, timeout=1, verbose=False)
        if answered:
            self.answered = answered
            self.alivehost()
        else:
            pass

    # Extract alive hosts from responses
    def alivehost(self):
        for sent, recv in self.answered:
            alive[recv.psrc] = recv.hwsrc

# Calculate the IP range based on network CIDR notation
def calculate_ip_range(network_cidr):
    try:
        network = ipaddress.ip_network(network_cidr, strict=False)
        start_ip = network.network_address + 1
        last_ip = network.broadcast_address - 1
        return str(start_ip), str(last_ip)
    except ValueError as e:
        print("[-] Invalid input ", file=sys.stderr)
        sys.exit(1)

# Parse command-line arguments
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-t',
        '--target',
        dest='target',
        help='Target IP Address.\n exp: NetroEye.py -t 192.168.0.101')
    arg = parser.parse_args()
    if len(sys.argv) == 1:
        target_range = f"{socket.gethostbyname(socket.gethostname())}/24"
        return calculate_ip_range(target_range)
    else:
        return calculate_ip_range(arg.target)

# Display scan results
def display():
    print(Fore.RED + "IP Address\t\t\t\tMAC Address\t\t\t\tVendor")
    print(Fore.BLACK + "---------\t\t\t\t-----------\t\t\t\t-----\n\n")
    for ip, mac in alive.items():
        try:
            print(f"{Fore.GREEN}{ip}\t\t\t{mac}\t\t\t{MacLookup().lookup(mac)}")

            # if mac_vendor_lookup  not found  in your device . you can simply run this lines of code.
            # vendor = requests.get('http://api.macvendors.com/' + mac).text
            # print(f"{Fore.GREEN}{ip}\t\t\t{mac}\t\t\t{vendor}")
        except:
            print(f"{Fore.GREEN}{ip}\t\t\t{mac}\t\t\tUNKNOWN")

# Main function
if __name__ == '__main__':
    # Print banner
    print(Fore.YELLOW + Style.BRIGHT + '''
                    _   __     __             ______
                   / | / /__  / /__________  / ____/_  _____
                  /  |/ / _ \/ __/ ___/ __ \/ __/ / / / / _ \/
                 / /|  /  __/ /_/ /  / /_/ / /___/ /_/ /  __/
                /_/ |_/\___/\__/_/   \____/_____/\__, /\___/
                                                /____/

                                           By @CY83RN4UT
                                           --------------------
    ''')

    # Get IP range from command-line arguments
    start_ip, last_ip = get_args()
    starting_point = int(start_ip.split('.')[-1])
    ending_point = int(last_ip.split('.')[-1])

    # Extract first three octets of the starting IP
    a, b, c = start_ip.split('.')[-4:-1]
    x = a + "." + b + "." + c + "."

    # Loop through IP addresses in the specified range
    for last_digit in tqdm(range(starting_point, ending_point+1)):
        ip = f"{x}{last_digit}"
        # Initialize NetroEye object for each IP
        NetroEye(ip)


    # Display the results
    display()

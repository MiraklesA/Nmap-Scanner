import subprocess
import sys


def check_open_ports(target_address):
    p = subprocess.Popen(["nmap", "-Pn", target_address], stdout=subprocess.PIPE)
    output, err = p.communicate()
    print(output)

def check_operating_system(target_address):
    p = subprocess.Popen(["nmap", "-Pn", "-A", target_address], stdout=subprocess.PIPE)
    output, err = p.communicate()
    print(output)

if len(sys.argv) == 1: 
    print("IP Address wasn't supplied!")
    sys.exit() 

target_address = ip_address
target_address = str(sys.argv[1])


p = subprocess.Popen(["nmap", "-Pn", "-sn", target_address], stdout=subprocess.PIPE)
output, err = p.communicate()
print("*** Running nmap -sn" + target_address + " ***\n", output)

host_status = str(output).find("Host seems down!")

if host_status == -1:
    print(output)
    check_open_ports(target_address)
    check_operating_system(target_address)
else: 
    print("Host Seems to be down")

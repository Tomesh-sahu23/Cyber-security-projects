# network and port scanning tool

import argparse
import nmap 
from nmap import PortScanner
def argument_parser():
    parser = argparse.ArgumentParser(
        description="TCP port scanner. accept a hostname/IP address and list of port to scan. Attempts to identify the service running on a port. "
    )
    parser.add_argument("-o", "--host", nargs="?", help="Host IP address")
    parser.add_argument("-p", "--ports", nargs="?", help="comma separation port list, such as '25,80,8000'")
    var_args = vars(parser.parse_args())
    return var_args

def nmap_scan(host_id,port_num):
    nm_scan = nmap.PortScanner()
    nm_scan.scan(host_id,port_num)
    state = nm_scan[host_id]['tcp'][int(port_num)]['state']
    result = f"[*] {host} tcp/{port} {state}"
    return result

if __name__ == '__main__':
    try:
        users_args = argument_parser()
        host = users_args["host"]
        ports = users_args["ports"].split(",")
        for port in ports:
            print(port)
            print(nmap_scan(host,port.strip()))
    except AttributeError as e:
        print(f"Error, please provide the command_line_argument before running. \n {e}")

            
  


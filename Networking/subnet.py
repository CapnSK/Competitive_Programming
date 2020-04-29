from array import array
from netaddr import *
 
def subnet_calculator():
    class_A = ('10.0.0.1')
    class_B = ('172.16.0.1')
    class_C = ('192.168.0.1')
 
 
    print("CLASS A = 10.0.0.1")
    print("CLASS B = 172.16.0.1")
    print("CLASS C = 192.168.0.1")
    print("---------------------")
    user_input_1 = input("Select a Class: ")
    hostsPerSubnet = int(input("How many Hosts per subnet: "))
    user_input_2 = input(("Enter starting IP address: "))
    Intarr=array('f',[])
 
#Creating a power 2 table (Decimals = 511 - 1023 - 2047 - 4095)
    for loop_2 in range(36):
        totalHosts = 2**loop_2
        Intarr.append(totalHosts)
     #Comparing the number of hosts entered with the array elements above.
     #Once the first instance of comparison where totalHosts < Decimals, it will use that to calculate hosts.
     #Example: Num of hosts entered: 8000. So, 8000 is less than 8,191. 8,191 Will be used to calculate the hosts.
        if hostsPerSubnet < totalHosts:
            maskBits = loop_2
            numHostsADJ = totalHosts -2
            netBlocks = totalHosts/256
            borrowedbits = netBlocks - maskBits
            #Calculating the Netmask
            netmas_pre = ("%s / %s") % (user_input_2, borrowedbits)
            netmas_post = IPNetwork(netmas_pre)
            netmask_final = netmas_post.netmask
 
 
            print("Total Hosts Minus Broadcast and Network: %s" % numHostsADJ)
            print("Total Hosts Included Broadcast and Network: %s" % totalHosts)
            print ("Mask Bits: %s" % maskBits)
            print ("Network Blocks: %s " % netBlocks)
            print ("Borrowed Network bits: %s " % borrowedbits)
            print ("Starting IP Address is: %s  " % user_input_2)
            print ("Netmask is: %s " % netmask_final)
            exit()
 
 
subnet_calculator()
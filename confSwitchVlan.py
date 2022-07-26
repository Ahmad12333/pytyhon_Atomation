import telnetlib
import sys
import getpass
HOST = "192.168.1.253"
user = input("Enter your account name: ")
password = getpass.getpass()
# the below commands for establishing telnet connection
tn = telnetlib.Telnet(HOST)
tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
# end of establishing telnet connection 

#Writing our command to the device (Router or Switch)
#tn.write("enable" + "\n")
#tn.write("cisco" + "\n")
#tn.write("conf t" + "\n")
#tn.write("vlan 2" + "\n")
#tn.write("exit" + "\n")
#tn.write("int fa 0/1" + "\n")
#tn.write("switchport mode access" + "\n")
#tn.write("switchport access vlan2" + "\n")
tn.write("enable" + "/n")
tn.write("cisco" + "/n")
tn.write("conf t" + "/n")
i = 0
for i in range(9):
    tn.write("valn" + str(i) + "/n")
    tn.write("name python_vlan" + str(i) + "\n")
# multiple Vlans Multiple Switches
user_s = input("Enter remote Username")
passwords = getpass.getpass() 
for n in range(1, 11):
    HOST_s = "192.168.1." + str(n)
    sn = telnetlib.Telnet(HOST_s)
    sn.read_until(b"Username: ")
    sn.write(user_s.encode('ascii') + b"\n")
    if passwords:
        sn.read_until(b"Password: ")
        sn.write(password.encode('ascii') + b"\n")
    tn.write("enable" + "/n")
    tn.write("cisco" + "/n")
    tn.write("conf t" + "/n")
    for j in range(2, 10):
        sn.write("vlan" + str(j) + "\n")
        tn.write("name python_vlan" + str(j) + "\n")
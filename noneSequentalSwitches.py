import telnetlib
import getpass
import sys

#We create a file to specify our devices ip addresse inside it 
f = open("my_Switches.txt")
user = input("Enter you remote Username: ")
password = getpass.getpass()

for line in f:
    HOST = line.strip()## strip function to eliminate spaces 
    tn = telnetlib.Telnet(HOST)
    print("Configureing switch " + line)
    tn.read_until(b"Username: ")
    tn.write(user.encode("ascii") + "\n")


    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode("ascii") + "\n  ")

    
    tn.write("enable\n")
    tn.write("cisco\n")
    tn.write("terminal length 0\n")##to show all output in a single window
    tn.write("conf t\n")## there is no neeed to the conf mode if we want to save backup into a file
    for n in range(2, 11):
        tn.write("vlan" + str(n) + "\n")
        tn.write("name vlan_python" + str(n) + "\n")
        # to save switch confs into a file in the enable mode
        read_conf = tn.read_all()
        save_output = open("Switch_conf" + HOST, "w")
        save_output.write(read_conf)
        save_output.close
    tn.write("end\n")
    tn.write("wr\n")
    tn.write("exit\n")
    print(tn.read_all())



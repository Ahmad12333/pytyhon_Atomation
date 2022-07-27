import paramiko
import time
######## Establishing ssh connection ##############
ip = '192.168.1.254' #### ip of router interface or switch vlan
username = 'ahmad'
password = 'cisco'
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip, username=username,password=password)
print("successful connection " + ip)
remote_connection = ssh_client.invoke_shell()
############### TO configure ospf on a router ################
remote_connection.send("conf t\n")
remote_connection.send("interface loop 0\n")
remote_connection.send("ip add 1.1.1.1 255.255.255.255\n")
remote_connection.send("no shut\n")
remote_connection.send("router ospf 1\n")
remote_connection.send("network 0.0.0.0 255.255.255.255 area 0")
remote_connection.send("end\n")
################ To conf Vlans on a switch ###############
remote_connection.send("conf t\n")
for n in range(2,10):
    remote_connection.send("vlan" + str(n) +"\n")
    remote_connection.send("name python_vlan" + str(n) + "\n")
    time.sleep(0.5)
remote_connection.send("end\n")
time.sleep(1)
output = remote_connection.recv(65535)
print(output)    
    

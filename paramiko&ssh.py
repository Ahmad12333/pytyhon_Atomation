import paramiko
import time
ip = '192.168.1.254'
username = 'ahmad'
password = 'cisco'
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip, username=username,password=password)
print("successful connection " + ip)
remote_connection = ssh_client.invoke_shell()

import paramiko

dssh = paramiko.SSHClient()
dssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
dssh.connect('cwhpc.lge.com', username='jaeyoung.choi', password='1111')
import os
stdin, stdout, stderr = dssh.exec_command('. /etc/profile;. ~/.bash_profile;. ~/.bashrc; lsdyna -short i=/nas/users/HA/jaeyoung.choi/scratch/2.k')
dd = stdout.readlines()
# d=((stdout.read()).decode())
# print(stdout.read())
dssh.close()
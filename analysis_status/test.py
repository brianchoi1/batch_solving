import paramiko, time, sys

ssh = paramiko.SSHClient()                                
hpc_path_default = '/nas/users/HA'                         
path = './'                                               
ip = 'hpc.lge.com'                                          
id = 'jaeyoung.choi'
pw = '1111'
cmd1 = '. /etc/profile;. ~/.bash_profile;. ~/.bashrc; '  
ncpu = 4

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())       
login_validation = ssh.connect(ip, 22, id, pw)               

cmd1 = '. /etc/profile;. ~/.bash_profile;. ~/.bashrc; '

stdin, stdout, stderr = ssh.exec_command('cat ' + hpc_path_default + '/' + id + '/scratch/Fluent_bm/' + 'cortexerror.log')
# d = stdout.read().splitlines()
for line in stdout.read().splitlines():
    log = str(line).split(' ')
    print(log)
	
print('dd')
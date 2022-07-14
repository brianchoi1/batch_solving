import paramiko, time, sys

ssh = paramiko.SSHClient()                                  #paramiko 셋업
hpc_path_default = '/nas/users/HA'                          #hpc기본주소세팅
path = './'                                                 #경로 접미사
ip = 'hpc.lge.com'                                          #hpc주소
id = 'jaeyoung.choi'
pw = '1111'
cmd1 = '. /etc/profile;. ~/.bash_profile;. ~/.bashrc; '   #hpc 기본명령어 
ncpu = 4

def byte_count(xfer, to_be_xfer):
    print(" transferred: {0:.0f} %".format((xfer / to_be_xfer) * 100))
    # time.sleep(3)
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())       
login_validation = ssh.connect(ip, 22, id, pw)                  
sftp = paramiko.SFTPClient.from_transport(ssh.get_transport())
time.sleep(5)
def print_hpc(transferred, toBeTransferred):
    print("Transferred: {0}\tOut of: {1}".format(transferred, toBeTransferred))
d = sftp.put('4g_25t_pp_best.sdy', hpc_path_default + '/' + id + '/scratch/Fluent_bm/' + '4g_25t_pp_best.sdy', callback = byte_count)



sftp.get(hpc_path_default + '/' + id + '/scratch/Fluent_bm/' + 'mesh_poly_bc_19.5.cas', 'mesh_poly_bc_19.5.cas', callback = byte_count)
sftp.close
# # sftp.get(hpc_path_default + '/' + id + '/scratch/Fluent_bm/' + 'mesh_poly_bc_19.5.cas', 'mesh_poly_bc_19.5.cas')
# time.sleep(5)
# sftp.put('mesh_poly_bc_19.5.cas', hpc_path_default + '/' + id + '/scratch/Fluent_bm/' + 'mesh_poly_bc_19.5.cas')


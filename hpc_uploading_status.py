import paramiko
import os, time

def check():
    dssh = paramiko.SSHClient()
    dssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    dssh.connect('hpc.lge.com', username='jaeyoung.choi', password='1111')
    import os
    stdin, stdout, stderr = dssh.exec_command('cd scratch/GDOR_CLAMP; ls -l')
    dd = stdout.readlines()
    # d=((stdout.read()).decode())
    print(stdout.read())
    dssh.close()

    # for i, rr in enumerate(dd):
    #     if 'mesh_poly_bc_1.cas' in rr:
    #         # print(i)
    #         item = int(rr.split()[4])

    # import os
    # file_size = os.path.getsize(r'mesh_poly_bc_1.cas') 
    # # print('File Size:', file_size, 'bytes')
    # ratio = item / file_size
    # print("%.2f%%" % (ratio * 100))
    # time.sleep(10)
    # return ratio

ssh = paramiko.SSHClient()           
default_cmd = '. /etc/profile;. ~/.bash_profile;. ~/.bashrc; aspera '                                              
hpc_path_default = '/nas/users/HA'       #에어솔루션 제외하고                
ip1 = 'cwhpc.lge.com'
id = 'jaeyoung.choi'
pw = '1111'
c_dir = 'D:\workothers\moldflow_solving'
fname = '3d_3g_25s.sdy'

import threading
import subprocess

class MyClass(threading.Thread):
    def __init__(self):
        self.stdout = None
        self.stderr = None
        threading.Thread.__init__(self)

    def run(self):
        cmd = "psftp.exe"
        p = subprocess.Popen([cmd, ip1, '-l', id, '-pw', pw, '-b', 'upload_cmd'], stdin=subprocess.PIPE, stdout=subprocess.PIPE) 


# myclass = MyClass()
# myclass.start()
# myclass.join()
# time.sleep(10)

i = 10
while i > 1:
    thr = threading.Thread(target=check)
    thr.start()
    check()
    time.sleep(2)
    print('done')
    i -= 1


# file_size = os.path.getsize(r'mesh_poly_bc_1.cas') 
# dd = 'mesh_poly_bc_1.cas'
# file_size2 = os.path.getsize(r"{}".format(dd)) 
print('dd')
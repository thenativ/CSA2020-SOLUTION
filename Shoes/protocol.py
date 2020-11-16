#/usr/env/python3
import socket

target_ip = "52.28.255.56"
target_port = 1080
xor_key = bytes.fromhex('5aa400435341bdc30871')
socks_connect = bytes.fromhex('5a01fedd749c2e')
socks_request = bytes.fromhex('5a010001c0a8ad140050624a3063')
http_get = "GET /Flag.jpg HTTP/1.1\r\nHost: www.tutorialspoint.com\r\n\r\n".encode()
buff_size = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect((target_ip, target_port)) # TCP HANDSHAKE
    s.send(socks_connect) # SOCKS

    # CHALLENGE REQ/RESP
    challenge = s.recv(buff_size)
    challenge_response = bytes([_a^_b for _a,_b in zip(challenge, xor_key)][1::])
    s.send(challenge_response)
    s.send(socks_request)
    s.recv(buff_size)

    # HTTP REQUEST FLAG.JPG
    s.send(http_get)
    raw_data = ""
    while response := s.recv(buff_size):
        raw_data += response.decode('latin-1')
    data = raw_data.split('\r\n\r\n')[1].encode('latin-1')
    
    # WRITE TO FILE
    with open("Flag.jpg", "wb") as f:
        f.write(data)

    s.close()


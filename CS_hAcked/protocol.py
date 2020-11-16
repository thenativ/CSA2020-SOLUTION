#!/usr/env/python3
import itertools
import socket
from arc4 import ARC4

target_ip = "3.126.154.76"
target_port = 80
buffer_size = 1024
rc4_key = "csa-mitm-key"
word_lengths = [13, 15, 2, 3, 2, 14, 6, 7, 8, 10]

# Get all words of dictionary
dictionary = []
with open("dictionary.txt", "r") as f:
    for line in f:
        dictionary.append(line)

# Get all possible words for each length
lengths_dictionary = []
for length in word_lengths:
    words = []
    for word in dictionary:
        if len(word) == length:
            words.append(word)
    lengths_dictionary.append(words)

# Get all possible word combinations
attack_dictionary = list(itertools.product(*lengths_dictionary))

# Dictionary Attack
for payload in attack_dictionary:
    _rc4 = ARC4(rc4_key) # Re-initialize key for each iteration
    target_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    target_socket.connect((target_ip, target_port))
    print(target_socket.recv(buffer_size))
    print(_rc4.decrypt(target_socket.recv(buffer_size)))
    for word in payload:
        byte = _rc4.encrypt(word)
        target_socket.send(byte)
        print(byte.encode('hex')) # Print the bytes we're sending
    result = _rc4.decrypt(target_socket.recv(buffer_size))
    print(result)
    if "CSA{" in result:
        break

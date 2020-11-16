#!/usr/env/python3
import socket, time
import random

target_ip = "tricky-guess.csa-challenge.com"
target_port = 2222
buff_size = 1024
encoding = "utf-8"
words_file = "words.txt"
guess_max = 15

with open(words_file, "r") as f:
    words_list = [line.strip('\n') for line in f]

while True:
    target_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    target_socket.connect((target_ip, target_port))
    print(target_socket.recv(buff_size).decode(encoding))
    print("AMOUNT OF WORDS IN DICTIONARY: " + str(len(words_list)))
    time.sleep(5) # CAT
    print(target_socket.recv(buff_size).decode(encoding))
    
    for try_num in range(0, guess_max):
    
        guess = words_list[random.randint(0, len(words_list)-1)]
        target_socket.send(guess.encode(encoding))
        correct_count = int(target_socket.recv(buff_size).decode(encoding))
        
        freq_list_guess = [0] * (ord('Z') - ord('A') + 1)
        for char in guess:
            freq_list_guess[ord(char) - ord('a') - 1] += 1
       
        for word in words_list:
            freq_list_word = [0] * (ord('Z') - ord('A') + 1)
            for char in word:
                freq_list_word[ord(char) - ord('a') - 1] += 1
    
            count = 0
            for i in range(len(freq_list_guess)):
                count += min(freq_list_guess[i], freq_list_word[i])
            
            if count != correct_count:
                words_list.pop(words_list.index(word))
        
        print(str(try_num+1) + "# GUESS: " + guess + "\nWORDS LIST: " 
                + str(len(words_list)) + "\nRESULT: " + str(correct_count))



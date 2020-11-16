#!/usr/env/python3
import socket, math
from sympy import symbols, Eq, solve

# Connection Information
target_ip = "maze.csa-challenge.com"
target_port = 80
buff_size = 1024
encoding = 'latin-1'

# Move mapping
moves = ['l', 'r', 'u', 'd']
compass = ['u', 'r', 'd', 'l']

# Automate command handling
def send_cmd(s, cmd):
    s.send(cmd.encode(encoding))

def recv_line(s):
    return s.recv(buff_size).decode(encoding)

def recv_all(s):
    while "?" not in (r := recv_line(s)):
        print(r)

def handle_cmd(s, cmd):
    send_cmd(s, cmd)
    result = recv_line(s)
    if "?" not in result:
        recv_all(s)
    return result
###

# Split 'i' command output to list of integers
def parse_move_info(i):
    return [int(n) for n in i if n.isdigit()]

# Convert distance to integer
def parse_distance_int(dist):
    return int("".join(c for c in dist if c.isdigit()))

# Convert coord to x,y integers
def parse_coord_xy(coord):
    c = coord.split(',')
    x = int("".join(c for c in c[0] if c.isdigit()))
    y = int("".join(c for c in c[1] if c.isdigit()))
    return x, y

# Maze right hand rule algorithm
def check_move(data_index, i):
    if data_index[moves.index(compass[(i+1)%len(moves)])] == 1:
        i += 1
    elif data_index[moves.index(compass[i%len(moves)])] == 1:
        pass # Don't change i
    elif data_index[moves.index(compass[(i-1)%len(moves)])] == 1:
        i -= 1
    else:
        i += 2

    i = i % len(moves)
    return compass[i], i

# Main
def solve_maze(s):
    result = ""
    last_move_index = 0
    last_x, last_y = None, None
    last_distance = None
    last_eq = None
    x, y = symbols('x y')
    while True:
        distance = handle_cmd(s, 'g')
        if "far far away" not in distance:
            curr_distance = parse_distance_int(distance)
            curr_x, curr_y = parse_coord_xy(handle_cmd(s, 'c'))
            curr_eq = Eq((x - curr_x)**2 + (y - curr_y)**2 - curr_distance, 0)
            if last_eq is not None:
                solution = solve((curr_eq, last_eq))
                print(solution)
                if len(solution) == 1:
                    send_cmd(s, 's')
                    print(recv_line(s))
                    send_cmd(s, ("({x},{y})".format(x=solution[0][x],y=solution[0][y])))
                    result = recv_line(s)
                    print(result)
                    input() # LAZY PAUSE PROGRAM

            last_x = curr_x
            last_y = curr_y
            last_distance = curr_distance
            last_eq = curr_eq

        info_moves = parse_move_info(handle_cmd(s, 'i'))
        move, last_move_index = check_move(info_moves, last_move_index)
        result = handle_cmd(s, move)
        print(info_moves)
###

target_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
target_socket.connect((target_ip, target_port))
recv_all(target_socket) # Intro story
solve_maze(target_socket)


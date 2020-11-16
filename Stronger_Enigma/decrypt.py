#!/usr/bin/python
import re

with open('log.txt', 'r') as f:
    encryption = f.read()
regex = re.compile('[^A-Z]')
encryption = regex.sub('', encryption)

with open('flag.txt', 'r') as f:
    flag = f.read().strip('\n')

data = "HELLOFIELDAGENTCOMMANDSSENDSECRETDATAGETSECRETDATAGOODBYE"
special_chars = ['{','}','_']
abc_size = ord('Z') - ord('A') + 1
result = ['?']*len(flag)

result_index = 0
rot = 13 # Found by counting output rotations and some calculations
for flag_c in flag:
    if flag_c not in special_chars:
        for i in range(rot, len(encryption), abc_size):
            if flag_c is encryption[i]:
                result[result_index] = data[i % len(data)]
                break
        rot = (rot + 1) % abc_size
    else:
        result[result_index] = flag_c
    result_index += 1


print(''.join(c for c in result))

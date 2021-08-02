from bitcoin import privkey_to_address
import csv
import random
from colorama import Fore, Style

with open('base_pub_key.txt', 'r') as i:
    file = [i.rstrip('\n') for i in i]

maxi = 115792089237316195423570985008687907852837564279074904382605163141518161494336 // 128

while True:
    number = random.randint(1, maxi)
    for i in range(128):
        adr = privkey_to_address(number)
        print(number, ' ', adr)
        if adr in file:
            print(f'{Fore.GREEN}{number}  {adr}  FOUND{Style.RESET_ALL}')
            print('-' * 70)
            with open("01_FOUND.csv", 'a') as f:
                writer = csv.writer(f)
                writer.writerow((number, ' ', adr))
        number += 1

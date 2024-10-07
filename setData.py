

file_path = 'ethsn.txt'  
file_path_save ='sethadder.bit'
counts = 0
runTrue = True
holdersapps = []
with open(file_path, 'r') as file:
    for line in file:
        temp = line[:-1].upper()[2:]
        if len(temp) == 40:
                newtemp = temp[4:]
                newtemp08 = newtemp[-8:]
                news8_16 =temp[8:16]
                news16_24 =temp[16:24]
                news24_32 =temp[24:32]
                jisuans = (int(news8_16,16) + int(news16_24,16) + int(news24_32,16)) & 0xffffffff
                newsd = f"{temp[:8]}{hex(jisuans)[2:].upper().rjust(8,'0')}{temp[-8:]}"
                holdersapps.append(newsd.lower())
                counts = counts +1
                if counts % 50000 == 0:
                    print("count",counts)
print(counts)
with open(file_path_save, 'w') as file:
        for item in holdersapps:
            file.write(f"{item}\n")
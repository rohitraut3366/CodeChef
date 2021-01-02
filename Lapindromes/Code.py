# cook your dish here
t = int(input())
for i in range(t):
    string = input()
    flag = True
    if len(string) % 2 == 0:
        part1 = list(string[:len(string)//2])
        part2 = list(string[len(string)//2:])
        
        for item in part1:
            if item in part2:
                part2.remove(item)
            else:
                flag = False
                break
        if flag:
            print('YES')
        else:
            print('NO')
                
    else:
        part1 = list(string[:len(string)//2])
        part2 = list(string[len(string)//2+1:])
        for item in part1:
            if item in part2:
                part2.remove(item)
            else:
                flag = False
                break
        if flag:
            print('YES')
        else:
            print('NO')

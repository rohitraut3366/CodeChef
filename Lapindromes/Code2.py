
   


def lapin(part1,part2):
    dict = {}
    for item in part1:
        if item in dict:
            dict[item] += 1
        else:
            dict[item] = 1
    for item in part2:
        if item in dict:
            dict[item] -= 1
        else:
            break
            return False
    for v in dict.values():
        if v != 0:
            return False
    return True
            
        

t = int(input())
for i in range(t):
    string = input()
    flag = True
    l = len(string)
    if len(string) % 2 == 0:
        part1 = list(string[:l//2])
        part2 = list(string[l//2:])    
        print("YES" if lapin(part1,part2) else "NO")
    else:
        part1 = list(string[:l//2])
        part2 = list(string[l//2+1:])    
        print("YES" if lapin(part1,part2) else "NO")

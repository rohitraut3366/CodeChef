# cook your dish here
coustomer = int(input())
coustomer_budgets = []
for i in range(coustomer):
    budget = int(input())
    coustomer_budgets.append(budget)

coustomer_budgets.sort(reverse=True)
ans = 0
for i in range(len(coustomer_budgets)):
    if ans < (i+1)*coustomer_budgets[i]:
        ans = (i+1)*coustomer_budgets[i]
        
print(ans)

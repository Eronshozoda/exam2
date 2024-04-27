data = str(input())
x = len(data)
i = 0
x = x - 1
k = 0
while x - i >= i:
    if data[x - i] == data[i]:
        i += 1
    else:
        k = 1
        break
if k == 1:
  print("no")
else:
  print("yes")
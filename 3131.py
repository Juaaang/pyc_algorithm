result = []
i = 2
while i <= 10:
    for j in range(2, i+1):
        if i % j != 0 and i != j:
            result.append(i)

    i+=1
    print(result)
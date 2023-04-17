A = ["eat", "tea", "tan", "ate", "nat", "bat"]
dic = {}
for word in A:
    newA = "".join(sorted(list(word)))
    print(newA)
    if newA not in dic:
        dic[newA] = [word]
    else:
        dic[newA].append(word)

print(list(dic.values()))


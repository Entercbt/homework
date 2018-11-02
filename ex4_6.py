import random
a = ['羊1','羊2','汽车']
times = 100000*100000
first,change = 0, 0
for i in range(times):
    x = random.choice(a)
    y = random.choice(a)
    if x == y:
        first += 1
    else:
        change += 1
print("坚持初心获得胜利的概率:{:.2f}%".format(first/times*100))
print("改变初心获得胜利的概率:{:.2f}%".format(change/times*100))

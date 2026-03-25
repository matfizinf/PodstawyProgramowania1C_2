#a)

plecak = [
("książka", 1.2),
("zeszyt", 0.5),
("laptop", 2.5),
("piórnik", 0.3),
("butelka z wodą", 1.0),
("strój sportowy", 1.8)
]

rzeczy = []

for i in range(len(plecak)):
    waga = plecak[i][1]
    if waga < 1:
        rzecz = plecak[i][0]
        rzeczy.append(rzecz)
print(rzeczy)

for w in plecak:
    waga = w[1]
    if waga < 1:
        rzecz = w[0]
        rzeczy.append(rzecz)
print(rzeczy)

#b)
wagi = ['{}'.format(round(1.1 * x[1], 2)) for x in plecak]
print(wagi)
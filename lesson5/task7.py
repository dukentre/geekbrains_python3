handle = open('task7.txt', "r")

companies = [{}, {}]
summ = 0
count = 0
for line in handle:

    words = line.split(" ")
    profit = int(words[2]) - int(words[3])
    if (profit):
        count += 1;
        summ += profit
    companies[0][words[0]] = profit

companies[1]['average_profit'] = summ / count
handle.close()

print(companies)

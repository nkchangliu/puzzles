import bisect
def most_profit_work(difficulties, profits, workers):
    diff_pro = zip(difficulties, profits)
    diff_pro = sorted(diff_pro)
    i, total, max_profit = 0, 0, 0
    workers = sorted(workers)
    for work in workers:
        while i in range(len(diff_pro)) and diff_pro[i][0] <= work:
            max_profit = max(max_profit, diff_pro[i][1])
            i += 1
        total += max_profit
    return total

print(most_profit_work([5,50,92,21,24,70,17,63,30,53],[68,100,3,99,56,43,26,93,55,25],[96,3,55,30,11,58,68,36,26,1]))

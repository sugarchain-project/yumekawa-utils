#!/usr/bin/python
# Code from https://github.com/bitcoinbook/bitcoinbook/blob/develop/code/max_money.py

# float128 and int64
import numpy as np # https://pypi.org/project/numpy/

# print to file
import sys # https://stackoverflow.com/questions/34926517/stop-sys-stdout-from-writing-to-a-text-file/34926590

# open - print to file
orig_stdout = sys.stdout
sys.stdout=open("max_moneyBTC.csv", "w")

# setup
current_reward = np.int64(50 * 10**8) # 50 BTC = 50 0000 0000 Satoshis
reward_interval = np.int64(210000) # 210000 is around every 4 years with a 10 minute block interval
total = np.int64(0)
halving_count = np.int64(0)

# print header
print "Count\tSupply\t\t\tReward"
print "%d\t" % halving_count,
print "%d\t\t\t" % total, # current supply is 0
print "%d" % current_reward

# main loop
while current_reward > 0: # bigger than one satoshi
    halving_count += 1
    print "%d\t" % halving_count,
    total += reward_interval * current_reward
    print "%d\t" % total, # current supply is going bigger to max_money
    current_reward /= 2
    print "%d" % current_reward

# close - print to file
sys.stdout.close()
sys.stdout=orig_stdout

# print total
print "Total BTC to ever be created: %d" % total, "Satoshis"
print "Total BTC to ever be created: %d" % round(round(total)/10**8), "BTC (rounded)"


# output example - BTC
"""
$ ./max_moneyBTC.py && cat max_moneyBTC.csv && gnuplot max_moneyBTC.plot
Total BTC to ever be created: 2099999997690000 Satoshis
Total BTC to ever be created: 21000000 BTC (rounded)
Count	Supply			Reward
0	0			5000000000
1	1050000000000000	2500000000
2	1575000000000000	1250000000
3	1837500000000000	625000000
4	1968750000000000	312500000
5	2034375000000000	156250000
6	2067187500000000	78125000
7	2083593750000000	39062500
8	2091796875000000	19531250
9	2095898437500000	9765625
10	2097949218750000	4882812
11	2098974609270000	2441406
12	2099487304530000	1220703
13	2099743652160000	610351
14	2099871825870000	305175
15	2099935912620000	152587
16	2099967955890000	76293
17	2099983977420000	38146
18	2099991988080000	19073
19	2099995993410000	9536
20	2099997995970000	4768
21	2099998997250000	2384
22	2099999497890000	1192
23	2099999748210000	596
24	2099999873370000	298
25	2099999935950000	149
26	2099999967240000	74
27	2099999982780000	37
28	2099999990550000	18
29	2099999994330000	9
30	2099999996220000	4
31	2099999997060000	2
32	2099999997480000	1
33	2099999997690000	0
"""

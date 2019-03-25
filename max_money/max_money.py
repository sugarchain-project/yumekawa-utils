#!/usr/bin/python
# Code from https://github.com/bitcoinbook/bitcoinbook/blob/develop/code/max_money.py

# float128 and int64
import numpy as np # https://pypi.org/project/numpy/

# print to file
import sys # https://stackoverflow.com/questions/34926517/stop-sys-stdout-from-writing-to-a-text-file/34926590

# open - print to file
orig_stdout = sys.stdout
sys.stdout=open("max_money.csv", "w")

# note - BTC original halving is `3.9954337899543378996`
"""
>>> interval=np.float128(210000.0)
>>> interval*600/3600/24/365
3.9954337899543378996
"""

# setup

halving_count = np.int64(0)
total = np.float128(0)

# current_reward = np.float128(50 * 10**8) # BTC float128
current_reward = np.int64(50 * 10**8) # BTC int64
# current_reward = np.float128(4294967296) # 2^32 = 42 9496 7296 Satoshis

reward_interval = np.int64(210000 * 1) # BTC
# reward_interval = np.int64(210000 * 120) # 210000*120 = 25200000 is around every 4 years with a 5 seconds block interval
# reward_interval = np.int64(105120*2) # 3600*24/600*365*4 = 210240 is around every 4 years with a 5 seconds block interval

# blocktime = np.int64(5) # 5 seconds for sugarchain
blocktime = np.int64(600) # BTC 10 minutes

# print header
print "Count\tSupply\t\t\tReward"
print "%d\t" % halving_count,
print "%d\t\t\t" % total, # current supply is 0
print "%d" % current_reward

# main loop
while current_reward > 0 and halving_count < 64: # BTC
# while current_reward > 1 and halving_count < 35: # TEST SUGAR
    halving_count += 1
    print "%d\t" % halving_count,
    total += reward_interval * current_reward
    print "%d\t" % total, # current supply is going bigger to max_money
    current_reward /= 2
    print "%.32g" % current_reward

# close - print to file
sys.stdout.close()
sys.stdout=orig_stdout

# print result
print ""
print "  Halving Interval:\t%d" % reward_interval, "Blocks"
print "  * in Years:\t\t  %.16g" % (np.float128(reward_interval) * blocktime / 3600 / 24 / 365), "Years"
print "  * in Days:\t\t  %.16g" % (np.float128(reward_interval) * blocktime / 3600 / 24), "Days"
print "  * in Hours:\t\t  %.16g" % (np.float128(reward_interval) * blocktime / 3600), "Hours"
print "  * in Minutes:\t\t  %.16g" % (np.float128(reward_interval) * blocktime / 60), "Minutes"
print "  * in Seconds:\t\t  %.16g" % (np.float128(reward_interval) * blocktime), "Seconds"
print "  Total SUGAR:\t\t%d" % total, "Satoshis"
print "  Total SUGAR:\t\t%.8f" % (total/1e+8), "SUGAR"
print ""

# output example - SUGAR
"""
$ ./max_money.py && cat max_money.csv
Total SUGAR to ever be created: 251999999722800000 Satoshis
Total SUGAR to ever be created: 2519999997 SUGAR (rounded)
Count	Supply			Reward
0	0			5000000000
1	126000000000000000	2500000000
2	189000000000000000	1250000000
3	220500000000000000	625000000
4	236250000000000000	312500000
5	244125000000000000	156250000
6	248062500000000000	78125000
7	250031250000000000	39062500
8	251015625000000000	19531250
9	251507812500000000	9765625
10	251753906250000000	4882812
11	251876953112400000	2441406
12	251938476543600000	1220703
13	251969238259200000	610351
14	251984619104400000	305175
15	251992309514400000	152587
16	251996154706800000	76293
17	251998077290400000	38146
18	251999038569600000	19073
19	251999519209200000	9536
20	251999759516400000	4768
21	251999879670000000	2384
22	251999939746800000	1192
23	251999969785200000	596
24	251999984804400000	298
25	251999992314000000	149
26	251999996068800000	74
27	251999997933600000	37
28	251999998866000000	18
29	251999999319600000	9
30	251999999546400000	4
31	251999999647200000	2
32	251999999697600000	1
33	251999999722800000	0
"""

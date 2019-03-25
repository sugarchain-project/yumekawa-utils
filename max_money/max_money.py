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

# note - There are a maximum of 2,099,999,997,690,000 Bitcoin in Satoshis
# Total BTC is 2099999997690000 Satoshis
# https://en.bitcoin.it/wiki/Bitcoin

# setup

halving_count = np.int64(0)
total = np.float128(0)

# current_reward = np.float128(50 * 10**8) # BTC float128
current_reward = np.int64(50 * 10**8) # BTC int64
# current_reward = np.float128(4294967296) # 2^32 = 42 9496 7296 Satoshis

reward_interval = np.int64(210000) # BTC about 4 years
# reward_interval = np.int64(210240) # BTC exactly 4 years: 3600*24/600*365*4 = 210240
# reward_interval = np.int64(210000 * 120) # 210000*120 = 25200000 is around every 4 years with a 5 seconds block interval

# blocktime = np.int64(5) # 5 seconds for sugarchain
blocktime = np.int64(600) # BTC 10 minutes

# print header
print "Count\tSupply\t\t\tReward"
print "%d\t" % halving_count,
print "%d\t\t\t" % total, # current supply is 0
print "%d" % current_reward

# main loop
# while current_reward > 0 and halving_count < 64: # BTC
while current_reward > 0 and halving_count < 35: # TEST SUGAR
    halving_count += 1
    print "%d\t" % halving_count,
    total += reward_interval * current_reward
    print "%d\t" % total, # current supply is going bigger to max_money

    # correction for float128: it makes 1 to 0 satoshi.
    if current_reward <= 1.0:
        current_reward = 0
    else:
        current_reward /= 2

    print "%.32g" % current_reward

# close - print to file
sys.stdout.close()
sys.stdout=orig_stdout

# print result
print ""
# blocktime
print "  Block Time:\t\t%d" % blocktime, "Seconds"
# reward_interval
print "  Halving Interval:\t%d" % reward_interval, "Blocks"
print "  * in Years:\t\t  %.16g" % (np.float128(reward_interval) * blocktime / 3600 / 24 / 365), "Years"
print "  * in Days:\t\t  %.16g" % (np.float128(reward_interval) * blocktime / 3600 / 24), "Days"
print "  * in Hours:\t\t  %.16g" % (np.float128(reward_interval) * blocktime / 3600), "Hours"
print "  * in Minutes:\t\t  %.16g" % (np.float128(reward_interval) * blocktime / 60), "Minutes"
print "  * in Seconds:\t\t  %.16g" % (np.float128(reward_interval) * blocktime), "Seconds"
# halving_count
print "  Total Halving Count:\t%d" % halving_count, "Times"
print "  * in Years:\t\t  %.16g" % ( halving_count * (np.float128(reward_interval) * blocktime / 3600 / 24 / 365) ), "Years"
print "  * in Days:\t\t  %.16g" % ( halving_count * (np.float128(reward_interval) * blocktime / 3600 / 24) ), "Days"
print "  * in Hours:\t\t  %.16g" % ( halving_count * (np.float128(reward_interval) * blocktime / 3600) ), "Hours"
print "  * in Minutes:\t\t  %.16g" % ( halving_count * (np.float128(reward_interval) * blocktime / 60) ), "Minutes"
print "  * in Seconds:\t\t  %.16g" % ( halving_count * (np.float128(reward_interval) * blocktime) ), "Seconds"
# total
print "  Total Satoshis:\t%d" % total, "Satoshis"
print "  Total COINs:\t\t%.8f" % (total/1e+8), "BTC"
print ""

# output example - SUGAR
"""
yumekawa-utils$ cd max_money && ./max_money.py && cat ./max_money.csv && gnuplot ./max_money.plot; cd ..

  Block Time:		600 Seconds
  Halving Interval:	210000 Blocks
  * in Years:		  3.995433789954338 Years
  * in Days:		  1458.333333333333 Days
  * in Hours:		  35000 Hours
  * in Minutes:		  2100000 Minutes
  * in Seconds:		  126000000 Seconds
  Total Halving Count:	33 Times
  * in Years:		  131.8493150684932 Years
  * in Days:		  48125 Days
  * in Hours:		  1155000 Hours
  * in Minutes:		  69300000 Minutes
  * in Seconds:		  4158000000 Seconds
  Total Satoshis:	2099999997690000 Satoshis
  Total COINs:		20999999.97690000 BTC

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

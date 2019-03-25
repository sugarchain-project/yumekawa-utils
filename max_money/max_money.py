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
total = np.int64(0)

# current_reward = np.float128(50 * 10**8) # BTC float128 # NOT CORRECT!!
# current_reward = np.int64(50 * 10**8) # BTC int64
current_reward = np.float128(4294967296) # 2^32 = 42 9496 7296 Satoshis
init_reward_printer = current_reward # store it for print after

# reward_interval = np.int64(210000) # BTC about 4 years
# reward_interval = np.int64(210240) # BTC exactly 4 years: 3600*24/600*365*4 = 210240
# reward_interval = np.int64(210000 * 120) # 210000*120 = 25200000 is around about 4 years with a 5 seconds block interval
# reward_interval = np.int64(210240 * 120) # 210240*120 = 25228800 is around exactly 4 years with a 5 seconds block interval
reward_interval = np.int64(210240 / 2 * 120) # 210240/2*120 = 12614400 is around exactly 2 years with a 5 seconds block interval

# blocktime = np.int64(600) # BTC 10 minutes
blocktime = np.int64(5) # 5 seconds for sugarchain

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
# reward
print "  Initial Block Reward:\t%d" % (np.float128(init_reward_printer)), "Satoshis"
print "  Initial Block Reward:\t%.8f" % (np.float128(init_reward_printer)/1e+8), "COINs"
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
print "  Total COINs:\t\t%f" % (total/1e+8), "COINs" # %.6f but it works. because %.8f NOT WOKRED!
print ""

# output example
"""
yumekawa-utils$ cd max_money && ./max_money.py && cat ./max_money.csv && gnuplot ./max_money.plot; cd ..

  Block Time:		5 Seconds
  Initial Block Reward:	4294967296 Satoshis
  Initial Block Reward:	42.94967296 COINs
  Halving Interval:	12614400 Blocks
  * in Years:		  2 Years
  * in Days:		  730 Days
  * in Hours:		  17520 Hours
  * in Minutes:		  1051200 Minutes
  * in Seconds:		  63072000 Seconds
  Total Halving Count:	33 Times
  * in Years:		  66 Years
  * in Days:		  24090 Days
  * in Hours:		  578160 Hours
  * in Minutes:		  34689600 Minutes
  * in Seconds:		  2081376000 Seconds
  Total Satoshis:	108356870904710400 Satoshis
  Total COINs:		1083568709.047104 COINs

Count	Supply			Reward
0	0			4294967296
1	54178435458662400	2147483648
2	81267653187993600	1073741824
3	94812262052659200	536870912
4	101584566484992000	268435456
5	104970718701158400	134217728
6	106663794809241600	67108864
7	107510332863283200	33554432
8	107933601890304000	16777216
9	108145236403814400	8388608
10	108251053660569600	4194304
11	108303962288947200	2097152
12	108330416603136000	1048576
13	108343643760230400	524288
14	108350257338777600	262144
15	108353564128051200	131072
16	108355217522688000	65536
17	108356044220006400	32768
18	108356457568665600	16384
19	108356664242995200	8192
20	108356767580160000	4096
21	108356819248742400	2048
22	108356845083033600	1024
23	108356858000179200	512
24	108356864458752000	256
25	108356867688038400	128
26	108356869302681600	64
27	108356870110003200	32
28	108356870513664000	16
29	108356870715494400	8
30	108356870816409600	4
31	108356870866867200	2
32	108356870892096000	1
33	108356870904710400	0
"""

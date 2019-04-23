#!/usr/bin/python
# Code from https://github.com/bitcoinbook/bitcoinbook/blob/develop/code/max_money.py

# precisions for int and float
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

# note - There are a maximum of 2,099,999,997,690,000 Bitcoin in Sat
# Total BTC is 2099999997690000 Sat
# https://en.bitcoin.it/wiki/Bitcoin

# SUGARCHAIN
# blockreward = pow(2,32) = 4294967296
# halving_interval = pow(5,8)*32 = 12500000
# TOTAL SUPPLY = 1073741824.00000000 SUGAR (in theory)
# TOTAL SUPPLY = 1073741823.87500000 SUGAR (in actual)

# setup
halving_count = np.int64(0)

total = np.int64(0)

# current_reward = np.float128(4294967296) # float128 - 2^32 = 42 9496 7296 Sat
current_reward = np.int64(4294967296) # int64 - 2^32 = 42 9496 7296 Sat
init_reward_printer = current_reward # store it for print after

# reward_interval = np.int64(210000) # BTC about 4 years
# reward_interval = np.int64(210240) # BTC exactly 4 years: 3600*24/600*365*4 = 210240
# reward_interval = np.int64(210240 / 2 * 120) # 210240/2*120 = 12614400 is exactly 2 years with a 5 seconds block interval
reward_interval = np.int64(pow(5,8)*32) # 210240/2*120 = 12614400 is exactly 2 years with a 5 seconds block interval

# blocktime = np.int64(600) # BTC 10 minutes
blocktime = np.int64(5) # 5 seconds for sugarchain

# print header
print "Count\tSupply\t\t\tPow\tReward"
print "%d\t" % halving_count,
print "%d\t\t\t" % total, # current supply is 0
print "2^{%.64g}\t" % np.log2(current_reward),
print "%d" % current_reward

# main loop
while current_reward > 0 and halving_count < 64-1: # 64: 0..63
# while current_reward > 0 and halving_count < 33: # TEST
    # halving
    halving_count += 1
    print "%d\t" % halving_count,
    
    # total
    total += reward_interval * current_reward
    print "%d\t" % total, # current supply is going bigger to max_money

    # statement - current reward - correction for float128: it makes 1 to 0 Sat.
    if current_reward <= 1.0:
        # current_reward = 0
        current_reward /= 2 # do same
    else:
        current_reward /= 2

    # print - "2^n" and "current reward"
    # print "2^{%.64g}\t" % np.log2(current_reward),
    print "2^{%.0f}\t" % np.log2(current_reward),
    print "%.64g\t" % current_reward

    # store first halving for later
    if halving_count == 1:
        first_halving = total
    
# close - print to file
sys.stdout.close()
sys.stdout=orig_stdout

# print result
print ""
# blocktime
print "  Block Time:\t\t%d" % blocktime, "Seconds"
# reward
print "  Initial Block Reward:\t%d" % (np.float128(init_reward_printer)), "Sat"
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
print "  Total Sat:\t\t%d" % total, "Sat"
print "  Total COINs:\t\t%.8f" % (total/1e+8), "COINs" # %.6f but it works. because %.8f NOT WOKRED!
print ""

# check range - int64
if np.iinfo('int64').max <= halving_count:
    print "  error: the range of 'halving_count' is too big (int64)"
elif np.iinfo('int64').max <= total:
    print "  error: the range of 'total' is too big (int64)"
elif np.iinfo('int64').max < reward_interval:
    print "  error: the range of 'reward_interval' is too big (int64)"
elif np.iinfo('int64').max < blocktime:
    print "  error: the range of 'blocktime' is too big (int64)"
# check range - float128
elif np.finfo('float128').max < init_reward_printer:
    print "  error: the range of 'init_reward_printer' is too big (float128)"
elif np.finfo('float64').max < init_reward_printer:
    print "  error: the range of 'init_reward_printer' is too big (float64)"
elif np.finfo('float32').max < init_reward_printer:
    print "  error: the range of 'init_reward_printer' is too big (float32)"
# double check - init_reward_printer
elif np.iinfo('int64').max < np.int64(init_reward_printer):
    print "  error: the range of 'init_reward_printer' is too big (int64)"
else:
    print "  [ OK ]: checking range is finished"
# print footer
print ""

# check first halving amount
"""
BTC difference is -1155000
>>> (2099999997690000/2)-1050000000000000
-1155000
"""
if total/2 != first_halving:
    print "  # WARNING: the total supply is not exactly!"
    print "  Total Supply (in actual):\t\t%d Sat" % (total)
    print "  Total Supply (in theory):\t\t%d Sat" % (first_halving * 2)
    print "  Difference:\t\t\t\t%d Sat" % (total - (first_halving * 2))
else:
    print "  [ OK ]: first halving is exactly half of the total supply"
print ""

# Output Example
"""
./max_money.py:74: RuntimeWarning: divide by zero encountered in log2
  print "2^{%.0f}\t" % np.log2(current_reward),

  Block Time:		5 Seconds
  Initial Block Reward:	4294967296 Sat
  Initial Block Reward:	42.94967296 COINs
  Halving Interval:	12500000 Blocks
  * in Years:		  1.981861998985287 Years
  * in Days:		  723.3796296296297 Days
  * in Hours:		  17361.11111111111 Hours
  * in Minutes:		  1041666.666666667 Minutes
  * in Seconds:		  62500000 Seconds
  Total Halving Count:	33 Times
  * in Years:		  65.40144596651446 Years
  * in Days:		  23871.52777777778 Days
  * in Hours:		  572916.6666666666 Hours
  * in Minutes:		  34375000 Minutes
  * in Seconds:		  2062500000 Seconds
  Total Sat:		107374182387500000 Sat
  Total COINs:		1073741823.87500000 COINs

  [ OK ]: checking range is finished

  # WARNING: the total supply is not exactly!
  Total Supply (in actual):		107374182387500000 Sat
  Total Supply (in theory):		107374182400000000 Sat
  Difference:				-12500000 Sat

Count	Supply			Pow	Reward
0	0			2^{32}	4294967296
1	53687091200000000	2^{31}	2147483648	
2	80530636800000000	2^{30}	1073741824	
3	93952409600000000	2^{29}	536870912	
4	100663296000000000	2^{28}	268435456	
5	104018739200000000	2^{27}	134217728	
6	105696460800000000	2^{26}	67108864	
7	106535321600000000	2^{25}	33554432	
8	106954752000000000	2^{24}	16777216	
9	107164467200000000	2^{23}	8388608	
10	107269324800000000	2^{22}	4194304	
11	107321753600000000	2^{21}	2097152	
12	107347968000000000	2^{20}	1048576	
13	107361075200000000	2^{19}	524288	
14	107367628800000000	2^{18}	262144	
15	107370905600000000	2^{17}	131072	
16	107372544000000000	2^{16}	65536	
17	107373363200000000	2^{15}	32768	
18	107373772800000000	2^{14}	16384	
19	107373977600000000	2^{13}	8192	
20	107374080000000000	2^{12}	4096	
21	107374131200000000	2^{11}	2048	
22	107374156800000000	2^{10}	1024	
23	107374169600000000	2^{9}	512	
24	107374176000000000	2^{8}	256	
25	107374179200000000	2^{7}	128	
26	107374180800000000	2^{6}	64	
27	107374181600000000	2^{5}	32	
28	107374182000000000	2^{4}	16	
29	107374182200000000	2^{3}	8	
30	107374182300000000	2^{2}	4	
31	107374182350000000	2^{1}	2	
32	107374182375000000	2^{0}	1	
33	107374182387500000	2^{-inf}	0
"""
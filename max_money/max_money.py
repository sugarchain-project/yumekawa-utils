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
# total = np.int32(0) # check int32
# total = np.float128(0) # check float128
# total = np.float64(0) # check float64
# total = np.float32(0) # check float32
# total = np.float16(0) # check float16

# current_reward = np.float128(50 * 10**8) # BTC float128 # NOT CORRECT!!
# current_reward = np.int64(50 * 10**8) # BTC int64
current_reward = np.float128(4294967296) # 2^32 = 42 9496 7296 Satoshis
init_reward_printer = current_reward # store it for print after

# reward_interval = np.int64(210000) # BTC about 4 years
# reward_interval = np.int64(210240) # BTC exactly 4 years: 3600*24/600*365*4 = 210240
# reward_interval = np.int64(210000 * 120) # 210000*120 = 25200000 is around about 4 years with a 5 seconds block interval
# reward_interval = np.int64(210240 * 120) # 210240*120 = 25228800 is exactly 4 years with a 5 seconds block interval
reward_interval = np.int64(210240 / 2 * 120) # 210240/2*120 = 12614400 is exactly 2 years with a 5 seconds block interval

# blocktime = np.int64(600) # BTC 10 minutes
blocktime = np.int64(5) # 5 seconds for sugarchain

# print header
print "Count\tSupply\t\t\tReward"
print "%d\t" % halving_count,
print "%d\t\t\t" % total, # current supply is 0
print "%d" % current_reward

# main loop
# while current_reward > 0 and halving_count < 64: # BTC
while current_reward > 0 and halving_count < 64: # TEST SUGAR "2^6=64"
    halving_count += 1
    print "%d\t" % halving_count,
    total += reward_interval * current_reward
    print "%d\t" % total, # current supply is going bigger to max_money

    # correction for float128: it makes 1 to 0 satoshi.
    if current_reward <= 1.0:
        # current_reward = 0
        current_reward /= 2 # do same
    else:
        current_reward /= 2

    print "%.32g" % current_reward

    # store first halving
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

# check range - int64
if np.iinfo('int64').max < total:
    print "error: the range of 'total' is too big (int64)"
# if np.iinfo('int32').max < total:
    # print "# WARNING: the range of 'total' is too big (int32)" # bypass - typedef int64_t CAmount;
elif np.iinfo('int64').max < halving_count:
    print "error: the range of 'halving_count' is too big (int64)"
elif np.iinfo('int64').max < reward_interval:
    print "error: the range of 'reward_interval' is too big (int64)"
elif np.iinfo('int64').max < blocktime:
    print "error: the range of 'blocktime' is too big (int64)"
# check range - float128
elif np.finfo('float128').max < init_reward_printer:
    print "error: the range of 'init_reward_printer' is too big (float128)"
elif np.finfo('float64').max < init_reward_printer:
    print "error: the range of 'init_reward_printer' is too big (float64)"
elif np.finfo('float32').max < init_reward_printer:
    print "error: the range of 'init_reward_printer' is too big (float32)"
# double check - init_reward_printer
elif np.iinfo('int64').max < np.int64(init_reward_printer):
    print "error: the range of 'init_reward_printer' is too big (int64)"
# elif np.iinfo('int32').max < np.int64(init_reward_printer):
#     print "# WARNING: the range of 'init_reward_printer' is too big (int32)" # bypass - already smaller than BTC
else:
    print "  [ OK ]: all range check is finished"
# print footer
print ""

# check first halving amount
"""
BTC difference is -1155000
>>> (2099999997690000/2)-1050000000000000
-1155000
"""
if total/2 != first_halving:
    print "  # WARNING: the first halving is NOT half of the total supply!"
    print "  Total Supply:\t\t%d" % (total)
    print "  Half of Total Supply:\t%d" % np.int64(total/2)
    print "  First Halving:\t%d" % np.int64(first_halving)
    print "  Difference:\t\t%d" % (np.int64(total/2)-np.int64(first_halving)), "Satoshis"
else:
    print "  [ OK ]: first halving is half of the total supply"
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
  Total Halving Count:	64 Times
  * in Years:		  128 Years
  * in Days:		  46720 Days
  * in Hours:		  1121280 Hours
  * in Minutes:		  67276800 Minutes
  * in Seconds:		  4036608000 Seconds
  Total Satoshis:	108356870917324799 Satoshis
  Total COINs:		1083568709.173248 COINs

  [ OK ]: all range check is finished

  # WARNING: the first halving is NOT half of the total supply!
  Total Supply:		108356870917324799
  Half of Total Supply:	54178435458662399
  First Halving:	54178435458662400
  Difference:		-1 Satoshis

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
33	108356870904710400	0.5
34	108356870911017600	0.25
35	108356870914171200	0.125
36	108356870915748000	0.0625
37	108356870916536400	0.03125
38	108356870916930600	0.015625
39	108356870917127700	0.0078125
40	108356870917226250	0.00390625
41	108356870917275525	0.001953125
42	108356870917300162	0.0009765625
43	108356870917312481	0.00048828125
44	108356870917318640	0.000244140625
45	108356870917321720	0.0001220703125
46	108356870917323260	6.103515625e-05
47	108356870917324030	3.0517578125e-05
48	108356870917324415	1.52587890625e-05
49	108356870917324607	7.62939453125e-06
50	108356870917324703	3.814697265625e-06
51	108356870917324751	1.9073486328125e-06
52	108356870917324775	9.5367431640625e-07
53	108356870917324787	4.76837158203125e-07
54	108356870917324793	2.384185791015625e-07
55	108356870917324796	1.1920928955078125e-07
56	108356870917324798	5.9604644775390625e-08
57	108356870917324799	2.98023223876953125e-08
58	108356870917324799	1.490116119384765625e-08
59	108356870917324799	7.450580596923828125e-09
60	108356870917324799	3.7252902984619140625e-09
61	108356870917324799	1.86264514923095703125e-09
62	108356870917324799	9.31322574615478515625e-10
63	108356870917324799	4.656612873077392578125e-10
64	108356870917324799	2.3283064365386962890625e-10
"""

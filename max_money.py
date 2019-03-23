#!/usr/bin/python
# Code from https://github.com/bitcoinbook/bitcoinbook/blob/develop/code/max_money.py

# float128 and int64
import numpy as np # https://pypi.org/project/numpy/

# print to file
import sys # https://stackoverflow.com/questions/34926517/stop-sys-stdout-from-writing-to-a-text-file/34926590

# open - print to file
orig_stdout = sys.stdout
sys.stdout=open("max_money.csv", "w")

# setup
current_reward = np.float128(50.0 * 10**8) # 50 BTC = 50 0000 0000 Satoshis
reward_interval = np.int64(210000) # 210000 is around every 4 years with a 10 minute block interval
total = np.float128(0.0)
halving_count = np.int64(0)

# print header
print "Count\tSupply\t\t\tReward"
print "%d\t" % halving_count,
print "%.2f\t\t\t" % total, # current supply is 0
print "%.24g" % (current_reward / 1)

# main loop
while current_reward > 1: # bigger than one satoshi
    halving_count += 1
    print "%d\t" % halving_count,
    total += reward_interval * current_reward
    print "%.2f\t" % (total / 1), # current supply is going bigger to max_money
    current_reward /= 2
    print "%.24g" % (current_reward / 1)

# close - print to file
sys.stdout.close()
sys.stdout=orig_stdout

# print total
print "Total BTC to ever be created: %.2f" % total, "Satoshis"
print "Total BTC to ever be created: %.0f" % round(total / 10**8), "BTC (rounded)"


# output example - BTC
"""
$ ./max_money.py 
Count	Supply			Reward
0	0.00			5000000000
1	1050000000000000.00	2500000000
2	1575000000000000.00	1250000000
3	1837500000000000.00	625000000
4	1968750000000000.00	312500000
5	2034375000000000.00	156250000
6	2067187500000000.00	78125000
7	2083593750000000.00	39062500
8	2091796875000000.00	19531250
9	2095898437500000.00	9765625
10	2097949218750000.00	4882812.5
11	2098974609375000.00	2441406.25
12	2099487304687500.00	1220703.125
13	2099743652343750.00	610351.5625
14	2099871826171875.00	305175.78125
15	2099935913085937.50	152587.890625
16	2099967956542968.75	76293.9453125
17	2099983978271484.50	38146.97265625
18	2099991989135742.25	19073.486328125
19	2099995994567871.00	9536.7431640625
20	2099997997283935.50	4768.37158203125
21	2099998998641967.75	2384.185791015625
22	2099999499320984.00	1192.0928955078125
23	2099999749660492.00	596.04644775390625
24	2099999874830246.00	298.023223876953125
25	2099999937415123.00	149.0116119384765625
26	2099999968707561.50	74.50580596923828125
27	2099999984353780.75	37.252902984619140625
28	2099999992176890.25	18.6264514923095703125
29	2099999996088445.25	9.31322574615478515625
30	2099999998044222.50	4.656612873077392578125
31	2099999999022111.25	2.3283064365386962890625
32	2099999999511055.75	1.16415321826934814453125
33	2099999999755527.75	0.582076609134674072265625
Total BTC to ever be created: 2099999999755527.75 Satoshis
Total BTC to ever be created: 21000000 BTC (rounded)
"""

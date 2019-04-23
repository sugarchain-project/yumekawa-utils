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

# note - There are a maximum of 2,099,999,997,690,000 Bitcoin in Satoshis
# Total BTC is 2099999997690000 Satoshis
# https://en.bitcoin.it/wiki/Bitcoin

# setup
halving_count = np.int64(0)

total = np.int64(0)

# current_reward = np.float128(4294967296) # float128 - 2^32 = 42 9496 7296 Satoshis
current_reward = np.int64(4294967296) # int64 - 2^32 = 42 9496 7296 Satoshis
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
while current_reward > 0 and halving_count < 64:
# while current_reward > 0 and halving_count < 33: # TEST
    # halving
    halving_count += 1
    print "%d\t" % halving_count,
    
    # total
    total += reward_interval * current_reward
    print "%d\t" % total, # current supply is going bigger to max_money

    # statement - current reward - correction for float128: it makes 1 to 0 satoshi.
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
    print "  # WARNING: the first halving is NOT exactly half of the total supply!"
    print "  Total Supply:\t\t%d" % (total)
    print "  Half of Total Supply:\t%d" % np.float128(total/2)
    print "  First Halving:\t%d" % np.int64(first_halving)
    print "  Difference:\t\t%d" % (np.int64(total/2)-np.int64(first_halving)), "Satoshi(s)"
else:
    print "  [ OK ]: first halving is exactly half of the total supply"
print ""

# note - deterministic
if 108356870917324799+1 == 108356870904710400+(63072000/10*2):
    print "  # INFO:"
    print "  total supply '108356870917324799+1' is 108356870904710400+(63072000/10*2)'"
    print "  '+1' is correction by virtual halving under 1 satoshi"
    print "  108356870904710400 is 33th halving with 0 reward"
    print "  63072000 is the halving interval in seconds"
else:
    print "  error: CRITICAL!! total supply is wrong"
print ""
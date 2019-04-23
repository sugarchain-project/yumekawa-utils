# yumekawa-utils
Blockchain Utility Collection for Sugarchain

## Contents
 - `max_money`: check the schedule of total supply and draw graph

## Comming Soon
 - `difficulty`: check historical difficulty with blocktime and draw graph
 - `nonce`: check historical nonces and draw graph
 - `blockchain_size`: check historical total blockchain size and draw graph
 - `blocktime_RT`: check current blocktime in realtime
 - `hash_attack`: simulate hash attack
 - `getFullBlockchain`: dump all blockchain data as plain text

-----

### max_money
![](https://github.com/sugarchain-project/yumekawa-utils/blob/master/max_money/max_money.png)

![](https://github.com/sugarchain-project/yumekawa-utils/blob/master/max_money/excel.png)

 - depends
```bash
sudo apt-get install gnuplot && \
pip install numpy
```

 - run python
```bash
cd max_money && \
./max_money.py && \
cat ./max_money.csv && \
gnuplot ./max_money.plot; \
cd ..
```

- ~~run C++ `outdated`~~
```bash
cd max_money && \
g++ max_money.cpp -std=c++11 -o max_money; \
./max_money; \
cd ..
```

- run java
```bash
sudo apt-get install default-jre
```
```bash
cd max_money && \
javac max_money.java && \
java max_money ; \
cd ..
```

 - data: sugarchain
```bash
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

Count	Supply(COIN)	Pow	Reward(COIN)
0	0		2^{32}	42.94967296
1	536870912	2^{31}	21.47483648	
2	805306368	2^{30}	10.73741824	
3	939524096	2^{29}	5.36870912	
4	1006632960	2^{28}	2.68435456	
5	1040187392	2^{27}	1.34217728	
6	1056964608	2^{26}	0.67108864	
7	1065353216	2^{25}	0.33554432	
8	1069547520	2^{24}	0.16777216	
9	1071644672	2^{23}	0.08388608	
10	1072693248	2^{22}	0.04194304	
11	1073217536	2^{21}	0.02097152	
12	1073479680	2^{20}	0.01048576	
13	1073610752	2^{19}	0.00524288	
14	1073676288	2^{18}	0.00262144	
15	1073709056	2^{17}	0.00131072	
16	1073725440	2^{16}	0.00065536	
17	1073733632	2^{15}	0.00032768	
18	1073737728	2^{14}	0.00016384	
19	1073739776	2^{13}	0.00008192	
20	1073740800	2^{12}	0.00004096	
21	1073741312	2^{11}	0.00002048	
22	1073741568	2^{10}	0.00001024	
23	1073741696	2^{9}	0.00000512	
24	1073741760	2^{8}	0.00000256	
25	1073741792	2^{7}	0.00000128	
26	1073741808	2^{6}	0.00000064	
27	1073741816	2^{5}	0.00000032	
28	1073741820	2^{4}	0.00000016	
29	1073741822	2^{3}	0.00000008	
30	1073741823	2^{2}	0.00000004	
31	1073741823.5	2^{1}	0.00000002	
32	1073741823.75	2^{0}	0.00000001	
33	1073741823.875	2^{-inf}	0.00000000
```

### max_moneyBTC (optional)
<!-- ![](https://github.com/sugarchain-project/yumekawa-utils/blob/master/max_moneyBTC/max_moneyBTC.png) -->

 - data BTC
```
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
```
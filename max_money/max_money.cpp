#include <iostream> // printf
#include <cstdint>  // uint64_t
#include <math.h>   //log2

// original: https://github.com/bitcoinbook/bitcoinbook/blob/develop/code/max_money.py
// max_money: https://github.com/sugarchain-project/yumekawa-utils/blob/master/max_money/max_money.py

// const int reward_interval = 210000; // BTC
const uint64_t reward_interval = 12614400; // 210240/2*120 = 12614400 is exactly 2 years with a 5 seconds block interval

// uint64_t current_reward = 5000000000; // BTC: 50 * 100000000 (in Satoshis)
// uint64_t current_reward = 4294967296; // SUGAR: 2^32 (in Satoshis)
// long double current_reward = 4294967296; // float - SUGAR: 2^32 = 4294967296 (in Satoshis)
long double current_reward = pow(2,32); // float - SUGAR: 2^32 = 4294967296 (in Satoshis)

uint64_t total = 0;
int halving_count = 0;
uint64_t first_halving;

int main() {
  // print header
  printf("\n");
  printf("Count\tSupply\t\t\tPow\tReward\n");
  // printf("%d\t%lu\t\t\t2^{%.f}\t%lu\n", halving_count, total, log2(current_reward), current_reward);
  printf("%d\t%lu\t\t\t2^{%.f}\t%.64Lg\n", halving_count, total, log2(current_reward), current_reward);

  // main loop
  while ( (current_reward > 0) && (halving_count < 64) ) {
  // while ( (current_reward > 0) ) {
    // halving
    halving_count++;
    printf("%d\t", halving_count);

    // total
    total += reward_interval * current_reward;
    printf("%lu\t", total);
    current_reward /= 2;

    // current reward
    printf("2^{%.f}\t", log2(current_reward));
    // printf("%lu\n", current_reward);
    // printf("%.64Lg\n", current_reward);
    if (current_reward > 0.01) {
      printf("%.64Lg\n", current_reward);
    } else {
      // printf("%.4Le\n", current_reward);
      printf("%.64Lg\n", current_reward);
    }
    
    // store first halving
    if (halving_count == 1) {
      first_halving = total;
    }
  }

  // print first halving and guess
  printf("\n");
  printf("First Halving in Satoshis:\t%lu\n", first_halving);
  printf("Guess Supply in Satoshis:\t%lu\n", first_halving*2);

  // print result
  printf("\n");
  printf("Total Supply in Satoshis:\t%lu\n", total);
  long double total_float = uint64_t(total);
  printf("Total Supply in COINs:\t\t%.8LF\n", total_float/100000000);

  // TEST
  /*
  >>> 0.00048828125*12614400+108356870917312480
  1.0835687091731864e+17
  */
  const long double test44thHalving = (long double)0.00048828125*(uint64_t)12614400+(uint64_t)108356870917312480;
  printf("test44thHalving %.8LF\n", test44thHalving);
  // test44thHalving 108356870917318639.37500000
}

// Output Example
/*
$ cd max_money && g++ max_money.cpp -std=c++11 -o max_money; ./max_money; cd ..

Count	Supply			Pow	Reward
0	0			2^{32}	4294967296
1	54178435458662400	2^{31}	2147483648
2	81267653187993600	2^{30}	1073741824
3	94812262052659200	2^{29}	536870912
4	101584566484992000	2^{28}	268435456
5	104970718701158400	2^{27}	134217728
6	106663794809241600	2^{26}	67108864
7	107510332863283200	2^{25}	33554432
8	107933601890304000	2^{24}	16777216
9	108145236403814400	2^{23}	8388608
10	108251053660569600	2^{22}	4194304
11	108303962288947200	2^{21}	2097152
12	108330416603136000	2^{20}	1048576
13	108343643760230400	2^{19}	524288
14	108350257338777600	2^{18}	262144
15	108353564128051200	2^{17}	131072
16	108355217522688000	2^{16}	65536
17	108356044220006400	2^{15}	32768
18	108356457568665600	2^{14}	16384
19	108356664242995200	2^{13}	8192
20	108356767580160000	2^{12}	4096
21	108356819248742400	2^{11}	2048
22	108356845083033600	2^{10}	1024
23	108356858000179200	2^{9}	512
24	108356864458752000	2^{8}	256
25	108356867688038400	2^{7}	128
26	108356869302681600	2^{6}	64
27	108356870110003200	2^{5}	32
28	108356870513664000	2^{4}	16
29	108356870715494400	2^{3}	8
30	108356870816409600	2^{2}	4
31	108356870866867200	2^{1}	2
32	108356870892096000	2^{0}	1
33	108356870904710400	2^{-1}	0.5
34	108356870911017600	2^{-2}	0.25
35	108356870914171200	2^{-3}	0.125
36	108356870915748000	2^{-4}	0.0625
37	108356870916536400	2^{-5}	0.03125
38	108356870916930600	2^{-6}	0.015625
39	108356870917127700	2^{-7}	7.8125e-03
40	108356870917226250	2^{-8}	3.9062e-03
41	108356870917275525	2^{-9}	1.9531e-03
42	108356870917300162	2^{-10}	9.7656e-04
43	108356870917312480	2^{-11}	4.8828e-04
44	108356870917318639	2^{-12}	2.4414e-04
45	108356870917321718	2^{-13}	1.2207e-04
46	108356870917323257	2^{-14}	6.1035e-05
47	108356870917324026	2^{-15}	3.0518e-05
48	108356870917324410	2^{-16}	1.5259e-05
49	108356870917324602	2^{-17}	7.6294e-06
50	108356870917324698	2^{-18}	3.8147e-06
51	108356870917324746	2^{-19}	1.9073e-06
52	108356870917324770	2^{-20}	9.5367e-07
53	108356870917324782	2^{-21}	4.7684e-07
54	108356870917324788	2^{-22}	2.3842e-07
55	108356870917324791	2^{-23}	1.1921e-07
56	108356870917324792	2^{-24}	5.9605e-08
57	108356870917324792	2^{-25}	2.9802e-08
58	108356870917324792	2^{-26}	1.4901e-08
59	108356870917324792	2^{-27}	7.4506e-09
60	108356870917324792	2^{-28}	3.7253e-09
61	108356870917324792	2^{-29}	1.8626e-09
62	108356870917324792	2^{-30}	9.3132e-10
63	108356870917324792	2^{-31}	4.6566e-10
64	108356870917324792	2^{-32}	2.3283e-10

Total Supply in Satoshis:	108356870917324792
Total Supply in COINs:		1083568709.17324792
*/
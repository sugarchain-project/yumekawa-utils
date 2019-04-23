// code by okoto-xyz
// run by "$ cd max_money && javac max_money.java && java max_money && cd .."

// SUGARCHAIN
// blockreward = pow(2,32) = 4294967296
// halving_interval = pow(5,8)*32 = 12500000
// TOTAL SUPPLY = 1073741824.00 SUGAR (in theory)

import java.math.BigDecimal;

public class max_money {
    public static void main(String[] args) throws Exception {
        final long reward_interval = 12500000;
		BigDecimal current_reward = new BigDecimal(Math.pow(2, 32)); // float - SUGAR: 2^32 (in Satoshis)
		BigDecimal total = BigDecimal.ZERO;
    BigDecimal actual_supply = total; // 33rd toal
		int halving_count = 0;
		long first_halving = 0;

		System.out.printf("\n");
		System.out.printf("JAVA\n");
		System.out.printf("Count\tSupply\t\t\tPow\tReward\n");
		System.out.printf("%d\t%s\t\t\t2^{%.0f}\t%s\n", halving_count, total.toString(),
				Math.log10(current_reward.doubleValue()) / Math.log10(2), current_reward.toEngineeringString());

		// main loop
		while ((current_reward.compareTo(BigDecimal.ZERO) > 0) && (halving_count < 64-1)) {
			// halving
			halving_count++;
			System.out.printf("%d\t", halving_count);

			// total
			// System.out.printf("%s\t",
			// 		new BigDecimal(reward_interval).multiply(current_reward).stripTrailingZeros().toPlainString());
			total = total.add(new BigDecimal(reward_interval).multiply(current_reward));
			System.out.printf("%s\t", total.stripTrailingZeros().toPlainString());
			current_reward = current_reward.divide(new BigDecimal(2));

			// current reward
			System.out.printf("2^{%.0f}\t", Math.log10(current_reward.doubleValue()) / Math.log10(2));
			System.out.printf("%s\n", current_reward.stripTrailingZeros().toPlainString());

			// store first halving
			if (halving_count == 1) {
				first_halving = total.longValue();
			}

      // break loop when current reward under 1
      if (current_reward.subtract(new BigDecimal(0.5)).compareTo(BigDecimal.ZERO) == 0) { // if current_reward == 0.5
        System.out.printf("FINISHED\n");
        actual_supply = total;
      }
		}

    // print result
    System.out.printf("\n");
    System.out.printf("  Total Supply in Satoshis:\t%s\n", total.stripTrailingZeros().toPlainString());

    // print guess and actual
    System.out.printf("\n");
		System.out.printf("  Guess Supply in Satoshis:\t\t%d\n", first_halving * 2);
		System.out.printf("  Actual Supply in Satoshis (33rd):\t%s\n", actual_supply.stripTrailingZeros().toPlainString());


    // print in COIN
    System.out.printf("\n");
		// System.out.printf("  Total Supply in COINs:\t\t%s\n",
		// 		total.divide(new BigDecimal(100000000)).stripTrailingZeros().toPlainString());
    System.out.printf("  Total Supply in COINs (in theory):\t%d\n", first_halving * 2 / 100000000);
    System.out.printf("  Total Supply in COINs (rounded):\t%.0f\n", total.divide(new BigDecimal(100000000)));
    System.out.printf("  Total Supply in COINs (in actual):\t%.8f\n", actual_supply.divide(new BigDecimal(100000000)));
    }
}

// Output Example
/*
$ cd max_money && javac max_money.java && java max_money ; cd ..

JAVA
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
33	107374182387500000	2^{-1}	0.5
FINISHED
34	107374182393750000	2^{-2}	0.25
35	107374182396875000	2^{-3}	0.125
36	107374182398437500	2^{-4}	0.0625
37	107374182399218750	2^{-5}	0.03125
38	107374182399609375	2^{-6}	0.015625
39	107374182399804687.5	2^{-7}	0.0078125
40	107374182399902343.75	2^{-8}	0.00390625
41	107374182399951171.875	2^{-9}	0.001953125
42	107374182399975585.9375	2^{-10}	0.0009765625
43	107374182399987792.96875	2^{-11}	0.00048828125
44	107374182399993896.484375	2^{-12}	0.000244140625
45	107374182399996948.2421875	2^{-13}	0.0001220703125
46	107374182399998474.12109375	2^{-14}	0.00006103515625
47	107374182399999237.060546875	2^{-15}	0.000030517578125
48	107374182399999618.5302734375	2^{-16}	0.0000152587890625
49	107374182399999809.26513671875	2^{-17}	0.00000762939453125
50	107374182399999904.632568359375	2^{-18}	0.000003814697265625
51	107374182399999952.3162841796875	2^{-19}	0.0000019073486328125
52	107374182399999976.15814208984375	2^{-20}	0.00000095367431640625
53	107374182399999988.079071044921875	2^{-21}	0.000000476837158203125
54	107374182399999994.0395355224609375	2^{-22}	0.0000002384185791015625
55	107374182399999997.01976776123046875	2^{-23}	0.00000011920928955078125
56	107374182399999998.509883880615234375	2^{-24}	0.000000059604644775390625
57	107374182399999999.2549419403076171875	2^{-25}	0.0000000298023223876953125
58	107374182399999999.62747097015380859375	2^{-26}	0.00000001490116119384765625
59	107374182399999999.813735485076904296875	2^{-27}	0.000000007450580596923828125
60	107374182399999999.9068677425384521484375	2^{-28}	0.0000000037252902984619140625
61	107374182399999999.95343387126922607421875	2^{-29}	0.00000000186264514923095703125
62	107374182399999999.976716935634613037109375	2^{-30}	0.000000000931322574615478515625
63	107374182399999999.9883584678173065185546875	2^{-31}	0.0000000004656612873077392578125

  Total Supply in Satoshis:	107374182399999999.9883584678173065185546875

  Guess Supply in Satoshis:		107374182400000000
  Actual Supply in Satoshis (33rd):	107374182387500000

  Total Supply in COINs (in theory):	1073741824
  Total Supply in COINs (rounded):	1073741824
  Total Supply in COINs (in actual):	1073741823.87500000
*/
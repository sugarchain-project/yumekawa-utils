// code by okoto-xyz
// run by "$ cd max_money && javac max_money.java && java max_money && cd .."

// SUGARCHAIN
// blockreward = pow(2,32) = 4294967296
// halving_interval = pow(5,8)*32 = 12500000
// TOTAL SUPPLY = 1073741824.00000000 SUGAR (in theory)
// TOTAL SUPPLY = 1073741823.87500000 SUGAR (in actual)

import java.math.BigDecimal;

public class max_money {
    public static void main(String[] args) throws Exception {
        final long reward_interval = 12500000;
		BigDecimal current_reward = new BigDecimal(Math.pow(2, 32)); // float - SUGAR: 2^32 (in Sat)
		BigDecimal total = BigDecimal.ZERO;
    BigDecimal actual_supply = total; // 33rd toal
		int halving_count = 0;
		long first_halving = 0;

		System.out.printf("\n");
		System.out.printf("JAVA\n");
		System.out.printf("Count\tSupply\t\tPow\tReward\n");
		System.out.printf("%d\t%s\t\t2^{%.0f}\t%s\n", halving_count, total.toString(),
				Math.log10(current_reward.doubleValue()) / Math.log10(2), current_reward.divide(new BigDecimal(100000000)).toEngineeringString());

		// main loop
		while ((current_reward.compareTo(BigDecimal.ZERO) > 0) && (halving_count < 64-1)) {
			// halving
			halving_count++;
			System.out.printf("%d\t", halving_count);

			total = total.add(new BigDecimal(reward_interval).multiply(current_reward));
			System.out.printf("%s\t", total.divide(new BigDecimal(100000000)).stripTrailingZeros().toPlainString());
			current_reward = current_reward.divide(new BigDecimal(2));

			// current reward
			System.out.printf("2^{%.0f}\t", Math.log10(current_reward.doubleValue()) / Math.log10(2));
			System.out.printf("%s\n", current_reward.divide(new BigDecimal(100000000)).stripTrailingZeros().toPlainString());

			// store first halving
			if (halving_count == 1) {
				first_halving = total.longValue();
			}

      // break loop when current reward under 1
      if (current_reward.subtract(new BigDecimal(0.5)).compareTo(BigDecimal.ZERO) == 0) { // if current_reward == 0.5
        // System.out.printf("FINISHED\n");
        actual_supply = total;
      }
		}

    // print result
    System.out.printf("\n");
    System.out.printf("  Total Supply in Sat (63rd):\t%s\n", total.stripTrailingZeros().toPlainString());

    // print guess and actual
    System.out.printf("\n");
		System.out.printf("  Guess Supply in Sat:\t\t%d\n", first_halving * 2);
		System.out.printf("  Actual Supply in Sat (33rd):\t%s\n", actual_supply.stripTrailingZeros().toPlainString());


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
$ cd max_money && javac max_money.java && java max_money && cd ..

JAVA
Count	Supply		Pow	Reward
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
33	1073741823.875	2^{-1}	0.000000005
34	1073741823.9375	2^{-2}	0.0000000025
35	1073741823.96875	2^{-3}	0.00000000125
36	1073741823.984375	2^{-4}	0.000000000625
37	1073741823.9921875	2^{-5}	0.0000000003125
38	1073741823.99609375	2^{-6}	0.00000000015625
39	1073741823.998046875	2^{-7}	0.000000000078125
40	1073741823.9990234375	2^{-8}	0.0000000000390625
41	1073741823.99951171875	2^{-9}	0.00000000001953125
42	1073741823.999755859375	2^{-10}	0.000000000009765625
43	1073741823.9998779296875	2^{-11}	0.0000000000048828125
44	1073741823.99993896484375	2^{-12}	0.00000000000244140625
45	1073741823.999969482421875	2^{-13}	0.000000000001220703125
46	1073741823.9999847412109375	2^{-14}	0.0000000000006103515625
47	1073741823.99999237060546875	2^{-15}	0.00000000000030517578125
48	1073741823.999996185302734375	2^{-16}	0.000000000000152587890625
49	1073741823.9999980926513671875	2^{-17}	0.0000000000000762939453125
50	1073741823.99999904632568359375	2^{-18}	0.00000000000003814697265625
51	1073741823.999999523162841796875	2^{-19}	0.000000000000019073486328125
52	1073741823.9999997615814208984375	2^{-20}	0.0000000000000095367431640625
53	1073741823.99999988079071044921875	2^{-21}	0.00000000000000476837158203125
54	1073741823.999999940395355224609375	2^{-22}	0.000000000000002384185791015625
55	1073741823.9999999701976776123046875	2^{-23}	0.0000000000000011920928955078125
56	1073741823.99999998509883880615234375	2^{-24}	0.00000000000000059604644775390625
57	1073741823.999999992549419403076171875	2^{-25}	0.000000000000000298023223876953125
58	1073741823.9999999962747097015380859375	2^{-26}	0.0000000000000001490116119384765625
59	1073741823.99999999813735485076904296875	2^{-27}	0.00000000000000007450580596923828125
60	1073741823.999999999068677425384521484375	2^{-28}	0.000000000000000037252902984619140625
61	1073741823.9999999995343387126922607421875	2^{-29}	0.0000000000000000186264514923095703125
62	1073741823.99999999976716935634613037109375	2^{-30}	0.00000000000000000931322574615478515625
63	1073741823.999999999883584678173065185546875	2^{-31}	0.000000000000000004656612873077392578125

  Total Supply in Sat (63rd):	107374182399999999.9883584678173065185546875

  Guess Supply in Sat:		107374182400000000
  Actual Supply in Sat (33rd):	107374182387500000

  Total Supply in COINs (in theory):	1073741824
  Total Supply in COINs (rounded):	1073741824
  Total Supply in COINs (in actual):	1073741823.87500000
*/
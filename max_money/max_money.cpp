#include <iostream>
#include <cstdint>

// original: https://github.com/bitcoinbook/bitcoinbook/blob/develop/code/max_money.py
// max_money: https://github.com/sugarchain-project/yumekawa-utils/blob/master/max_money/max_money.py

const int reward_interval = 210000;

uint64_t current_reward = 5000000000; // 50 * 100000000 (in Satoshis)
uint64_t total = 0;

int main() {
  while (current_reward > 0) {
    total += reward_interval * current_reward;
    current_reward /= 2;
  }
  printf("Total Supply in Satoshis:\t%lu\n", total);
  long double total_float = uint64_t(total);
  printf("Total Supply in BTC:\t\t%.8LF\n", total_float/100000000);
}


// Output Example
/*
$ cd max_money && g++ max_money.cpp -std=c++11 -o max_money; ./max_money; cd ..
Total Supply in Satoshis:	2099999997690000
Total Supply in BTC:		20999999.97690000
*/
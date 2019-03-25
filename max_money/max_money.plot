#!/usr/bin/gnuplot 

# QT
set terminal qt size 1200,600;

# PNG
# set term png size 1200, 600;
# set output 'max_money.png';

set title "Max Money SUGAR\n \
    {/*0.75\
    Block Reward = 2^{32} = 4294967296 Satoshis\
    Halving Interval = 210000*120 = 25200000 (4years)\
    }" font ",15";
set key center right box;

HALVING_COUNT="9";
set xrange [0:HALVING_COUNT];
set xtics 0, 1;
set xlabel "Halving Count" tc rgb "black" offset 0;

# MAX_MONEY="2520000000e+8"; # 252000000000000000
set lmargin at screen 0.15;
set yrange [0:*];
# set ytics 0, 1260000000e+8; # 126000000000000000
# set ytics add (1890000000e+8) (2205000000e+8) (2362500000e+8) (2441250000e+8);
set format y "%.0f";
set ylabel "Total Supply (in Satoshis)" tc rgb "red" offset -3;
set ytics nomirror;

# BLOCK_REWARD="5e+9"; # 5000000000
set rmargin at screen 0.89;
set y2range [0:*];
# set y2tics 0, BLOCK_REWARD/2; 
set y2tics 0, 1e+9; 
# set y2tics add (BLOCK_REWARD/4) (BLOCK_REWARD/8) (BLOCK_REWARD/16) (BLOCK_REWARD/32);
set format y2 "%.0f";
set y2label "Block Reward (in Satoshis)" tc rgb "blue" offset 2.5;

set grid xtics ytics y2tics;

set style line 1 \
    linecolor rgb 'red' \
    linetype 1 linewidth 2 \
    pointtype 4 pointsize 1.5

set style line 2 \
    linecolor rgb 'blue' \
    linetype 1 linewidth 2 \
    pointtype 2 pointsize 1.5

# set offset 1,1,1,1;

plot \
    'max_money.csv' using 1:2 axis x1y1 with linespoints linestyle 1 title "Total Supply", \
    ''              using 1:3 axis x1y2 with steps linestyle 2 title "Block Reward", \
    ''              using 1:3 axis x1y2 with points linestyle 2 notitle, \
    ''              using 1:2:(sprintf("%0.f", $2)) with labels rotate by 315 left offset 1.2,-0.5 tc rgb '#990000' notitle, \
    ''              using 1:3:(sprintf("%0.f", $3)) axis x1y2 with labels rotate by 0 left offset 2,0.75 tc rgb '#000099' notitle, \

set yrange [GPVAL_DATA_Y_MIN:GPVAL_DATA_Y_MAX]
set y2range [GPVAL_DATA_Y2_MIN:GPVAL_DATA_Y2_MAX]
replot
    
pause -1

#!/usr/bin/gnuplot 

# do QT size
set terminal qt size 1200,600;

# do PNG
# set term png size 1200, 600;
# set output 'max_money.png';

#test
# set label 1 "Block Time = 5 Seconds"
# set label 1 at graph 0.4, 0.55 tc lt 2
# set label 2 "Initial Block Reward = 2^{32} = 4294967296 Satoshis"
# set label 2 at graph 0.4, 0.5 tc lt 2
# set label 3 "Halving Interval = 210240/2*120 = 12614400 (2 Years)"
# set label 3 at graph 0.4, 0.45 tc lt 2

# specs as label
set label 1 "{/:Bold Halving Parameters}\n\
  Block Time:		5 Seconds\n\
  Initial Block Reward:	{2^{32}} = 4294967296 Satoshis\n\
  Initial Block Reward:	42.94967296 COINs\n\
  \n\
  Halving Interval:	12614400 Blocks\n\
  * in Years:		  2 Years\n\
  * in Days:		  730 Days\n\
  * in Hours:		  17520 Hours\n\
  * in Minutes:	  1051200 Minutes\n\
  * in Seconds:	  63072000 Seconds\n\
  \n\
  Total Halving Count:	64 Times\n\
  * in Years:		  128 Years\n\
  * in Days:		  46720 Days\n\
  * in Hours:		  1121280 Hours\n\
  * in Minutes:	  67276800 Minutes\n\
  * in Seconds:	  4036608000 Seconds\n\
  \n\
  Total Satoshis:	108356870917324799 Satoshis\n\
  Total COINs:	1083568709.173248 COINs (+1 satoshi correction)\n"
set label 1 at graph 0.42, 0.71 tc rgb "black";

set title "Sugarchain Halving Schedule" font ",15" offset 0;
set key center right box;

set xrange [0:*];
set xtics 0, 1 rotate by 45 right;;
set xlabel "Halving Count" tc rgb "black" offset 0;

set lmargin at screen 0.15;
set yrange [0:*];
set format y "%.0f";
set ylabel "Total Supply (in Satoshis)" tc rgb "red" offset -3;
set ytics nomirror;

set rmargin at screen 0.89;
set y2range [0:*];
set y2tics 0, 1e+9; 
set format y2 "%.0f";
set y2label "Block Reward (in Satoshis)" tc rgb "blue" offset 2.5;

set grid xtics ytics y2tics lc rgb "#888888" lw 1 lt 0;

set style line 1 \
    linecolor rgb 'red' \
    linetype 1 linewidth 2 \
    pointtype 4 pointsize 1.5

set style line 2 \
    linecolor rgb 'blue' \
    linetype 1 linewidth 2 \
    pointtype 2 pointsize 1.5

plot \
    'max_money.csv' using 1:2 axis x1y1 with linespoints linestyle 1 title "Total Supply", \
    ''              using 1:3 axis x1y2 with steps linestyle 2 title "Block Reward", \
    ''              using 1:3 axis x1y2 with points linestyle 2 notitle, \
    ''              using 1:2:(sprintf("%0.f", $2)) with labels rotate by 315 left offset 1.2,-0.5 tc rgb '#990000' notitle, \
    ''              using 1:3:(sprintf("%0.f", $3)) axis x1y2 with labels rotate by 10 left offset 2,0.75 tc rgb '#000099' notitle, \

# do setting min max range
set yrange [GPVAL_DATA_Y_MIN:GPVAL_DATA_Y_MAX];
set ytics 0, GPVAL_DATA_Y_MAX/2; # half of max_money
set y2range [GPVAL_DATA_Y2_MIN:GPVAL_DATA_Y2_MAX];
set y2tics 0, GPVAL_DATA_Y2_MAX/2; # half of init reward

# do resetting x-axis
set xrange [0:16];

# do tics
set tics scale 2.5, 1;
set mxtics 2;
set mytics 2;
set my2tics 2;

# do re-plot'ing
replot;
    
pause -1;

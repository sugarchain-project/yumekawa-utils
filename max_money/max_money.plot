#!/usr/bin/gnuplot 

# SUGARCHAIN
# blockreward = pow(2,32) = 4294967296
# halving_interval = pow(5,8)*32 = 12500000
# TOTAL SUPPLY = 1073741824.00000000 SUGAR (in theory)
# TOTAL SUPPLY = 1073741823.87500000 SUGAR (in actual)

# do QT size
screen_x=1280;
screen_y=640;
set terminal qt size screen_x,screen_y;

# do PNG
# set term png size 1200, 600;
# set output 'max_money.png';

# notations
# set label 1 "(+1 correction)" at first -2.2, graph 0.97 tc rgb "black";
# set label 2 "(exactly half)" at first 2.1, graph 0.455 tc rgb "#990000" rotate by 330 left offset 0,0;

set title "Sugarchain Halving Schedule\n\
{/*0.75\
Block Reward =  {2^{32}} = 4294967296 Satoshis,\n\
{/*0.75\
Block Time = 5 sec,\t\
Interval = 12614400 blocks (2 years)\
}" font ",15" offset 0,0;

set key center right box;

set xrange [0:*];
set xtics 0, 1 rotate by 45 right;
set xlabel "Halving Count" tc rgb "black" offset 0;

set lmargin at screen 0.12;
set yrange [0:*];
set format y "%.0f";
set ylabel "Total Supply (in Satoshis)" tc rgb "red" offset 0.0;
set ytics nomirror;

set rmargin at screen 0.88;
set y2range [0:*];
set y2tics 0, 1e+9; 
set format y2 "%.0f";
set y2label "Block Reward (in Satoshis)" tc rgb "blue" offset 0.0;

set grid xtics lc rgb "#888888" lw 1 lt 0;
set grid ytics lc rgb "#888888" lw 1 lt 0;
# set grid y2tics lc rgb "#888888" lw 1 lt 0; # disabled by logscale

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
    ''              using 1:4 axis x1y2 with steps linestyle 2 title "Block Reward", \
    ''              using 1:4 axis x1y2 with points linestyle 2 notitle, \
    ''              using 1:2:(sprintf("%.0f", $2)) with labels rotate by 330 left offset 1.2,-0.5 tc rgb '#990000' notitle, \
    ''              using 1:4:(sprintf("{%s}=%.0f", stringcolumn(3), $4)) axis x1y2 with labels rotate by 30 left offset 2,0.75 tc rgb '#000099' notitle, \

# do setting min max range
set yrange [GPVAL_DATA_Y_MIN:GPVAL_DATA_Y_MAX];
set ytics 0, GPVAL_DATA_Y_MAX/2 rotate by -30 right offset 0,0; # half of max_money
set y2range [GPVAL_DATA_Y2_MIN:GPVAL_DATA_Y2_MAX];
set y2tics 0, GPVAL_DATA_Y2_MAX/2 rotate by 30 left offset 0,0; # half of init reward

# do resetting x-axis
set xrange [0:34];

# do tics
set tics scale 1, 1;
set mxtics 1;
set mytics 1;
set my2tics 1;

# do log scale y
# set yrange [GPVAL_DATA_Y_MIN+1e+08:GPVAL_DATA_Y_MAX];
# set nonlinear y via sqrt(GPVAL_DATA_Y_MAX-y) inverse y**10

# do log scale - y2
# set y2range [GPVAL_DATA_Y2_MIN+0.49999999:GPVAL_DATA_Y2_MAX]; # +0.499.. is a workaround that none 0(zero) in logscale
# set logscale y2 2; # do this
# set nonlinear y2 via log10(y) inverse y**10 # right way, but error

# do re-plot'ing
set terminal qt size screen_x,screen_y; # duplicated, but a workaround
replot;
replot;
    
pause -1;

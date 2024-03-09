set terminal png size 1280, 941 crop
set  output 'linear.png'
set xrange [1:100000]
set xlabel 'Elementos'
set ylabel 'Operações'


plot f(x) = 6(x)-1

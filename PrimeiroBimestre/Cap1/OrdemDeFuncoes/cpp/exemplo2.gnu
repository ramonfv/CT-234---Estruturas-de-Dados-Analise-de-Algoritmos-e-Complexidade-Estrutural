set terminal png size 1280, 941 crop
set output 'exemplo2.png'
set title "Taxa de crescimento de funções"
set logscale xy
set size square

f(x) = 3*x**2 + x - 2
bigOx2(x) = 4*x**2

linear(x) = x


plot f(x) title "f(n)", \
     bigOx2(x) title "4*O(n^2)", \
        linear(x) title "O(n)"


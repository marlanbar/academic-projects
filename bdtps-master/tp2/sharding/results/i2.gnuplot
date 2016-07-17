set terminal png size 1000,480
set output 'i2.png'

set key Left invert reverse outside

set yrange [0:102]

set xlabel "Cantidad de registros ingresados (miles)"
set ylabel "Porcentaje de carga de registros"

set style data histogram
set style histogram rowstacked
set style fill solid border -1

plot 'i2.dat' using 2:xtic(1) title 'shard 1', '' using 3 title 'shard 2'

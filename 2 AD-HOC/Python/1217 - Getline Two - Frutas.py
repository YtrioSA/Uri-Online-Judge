n=gets.chomp.to_i
consumo=0
frutas=""
kgs=0
for x in (1..n) do
    preco=gets.chomp.to_f
    frutas=gets.chomp.split
    consumo+=preco
    kgs+=frutas.length
    puts "day #{x}: #{frutas.length} kg"
end
total=kgs/(n.to_f)
puts "%0.2f kg by day" % [total]
puts "R$ %0.2f by day" % [consumo/n]

package main

import (
	"fmt"
	"math"
	"sort"
)

func sortedMatrix (x [][2] int) [][2] int {
	var aux [2] int
	consumption := make([]int, len(x))
	for i:=0; i<len(x); i++ {
		consumption[i]=int(x[i][1]/x[i][0])
		x[i][1]=consumption[i]
	}
	sort.Ints(consumption)
	for j:=0; j<len(x); j++ {
		for k:=0; k<len(x); k++ {
			if consumption[j] == x[k][1] && k != j {
				aux  = x[k]
				x[k] = x[j]
				x[j] = aux
				break
			}

		}
	}
	return x
}

func agroup(x [][2] int) [][2] int {
	con := make([][2]int, len(x))
	f   := 0
	for j:=0; j<len(x); j++ {
		if j < len(x)-1 {
			if x[j][1] == x[j+1][1] {
				x[j+1][0] = x[j][0]+x[j+1][0]
			} else {
				con[f] = x[j]
				f+=1
			}
		} else {
			con[f] = x[j]
		}
	}
	return con
}

func output (n int,x [][2] int, media float64) {
	fmt.Printf("Cidade# %d:\n", n)
	for k:=0; k<len(x); k++ {
		if x[k][0] == 0 && x[k][1] == 0 { continue }
		fmt.Printf("%d-%d ", x[k][0], x[k][1])
	}
	fmt.Println()
	fmt.Printf("Consumo medio: %0.2f m3.", math.Floor(media*100)/100)
}

func main() {
	var n, x, y int
	var s1, s2, media float64
	var si [][2] int
	count := 0
	for  {
		fmt.Scanln(&n)
		if n == 0 {
			break
		} else {
			si = make([][2] int, n)
		}
		for i:=0; i<n; i++ {
			fmt.Scanln(&x, &y)
			si[i][0] = x
			si[i][1] = y
			s1 += float64(si[i][0])
			s2 += float64(si[i][1])
		}
		media=s2/s1
		count=count+1
		output(count, agroup(sortedMatrix(si)), media)
		s1,s2 = 0,0
	}
}




package main

import "fmt"

type Vendedor struct {
	Nome   string
	Fixo   float64
	Vendas float64
}

func (v Vendedor) SalarioBonus (fixo float64, vendas float64) float64 {
	bonus := 0.15 * vendas
	total := fixo + bonus
	return total
}

func main() {

	v := Vendedor {}
	fmt.Scanln (&v.Nome)
	fmt.Scanln (&v.Fixo)
	fmt.Scanln (&v.Vendas)

	fmt.Printf("TOTAL = R$ %.2f\n", v.SalarioBonus (v.Fixo, v.Vendas))

}

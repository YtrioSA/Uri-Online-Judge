package main

import "fmt"

type Funcionario struct {
	numero  int
	horas   int
	recebeu float32
}

func (F Funcionario) salario (horas int, recebeu float32) float32 {
	salario := float32 (horas) * recebeu
	return salario
}

func main() {
	f := Funcionario{}
	fmt.Scanln(&f.numero)
	fmt.Scanln(&f.horas)
	fmt.Scanln(&f.recebeu)
	fmt.Printf("NUMBER = %d\nSALARY = U$ %.2f\n", f.numero, f.salario(f.horas, f.recebeu))
}

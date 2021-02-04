package main

import "fmt"

type Jogo struct {
	HoraInicial int
	HoraFinal   int
}

func (J Jogo) Jogo (Hi int, Hf int) int {
	var tempo int
	if Hi > Hf {
		tempo = (24 + (Hf - Hi))
	} else if (Hi == Hf) {
		tempo = (24 + (Hf - Hi))
	} else {
		tempo = (Hf - Hi)
	}
	return tempo
}

func main() {
	j := Jogo{}
	fmt.Scanln(&j.HoraInicial, &j.HoraFinal)
	fmt.Printf("O JOGO DUROU %d HORA(S)\n", j.Jogo(j.HoraInicial, j.HoraFinal))
}
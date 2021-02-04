package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func reverse ( msg  string ) ([] byte, [] string) {
	k := 0
	m := make ( [] byte,   len ( msg ) )
	f := make ( [] string, len ( msg ) )
	for i := len ( msg ) - 1; i >= 0; i -- {
		m[k] = msg [i]
		f[k] = string( msg [i] )
		k++
	}
	return m,f
}

func alphabeto ( char string ) bool {
	if ( char >= "a" && char <= "z" ) ||
		( char >= "A" && char <= "Z" ) {
		return true
	} else {
		return false
	}
}
func codificar ( msg  string ) string {

	mssg   := ""
	msg_   := make ( [] rune,   len(msg))
	msg__  := make ( [] string, len(msg))

	for i, v := range msg {
		msg_[i]  = v
		msg__[i] = string(v)
		if alphabeto ( msg__[i] ) {
			msg_[i]  = msg_[i] + 3
			msg__[i] = string(msg_[i])
		}
		mssg += msg__[i]
	}
	kk,jj := reverse(mssg)
	for i := len(kk)/2; i < len(mssg); i++ {
		kk[i] = kk[i] - 1
		jj[i] = string(kk[i])
	}
	gopskg := ""
	for kkk := 0; kkk < len(jj); kkk++ {
		gopskg += jj[kkk]
	}

	return gopskg
}

func main() {
	var n int
	fmt.Scanln(&n)
	reader := bufio.NewReader(os.Stdin)
	for i:=0; i<n; i++ {
		text, _ := reader.ReadString('\n')
		text = strings.Replace(text, "\n", "", -1)
		fmt.Printf("%s\n",codificar(text))
	}
}

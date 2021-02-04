
package main
import (
	"fmt"
	"strconv"
	"strings"
)
func contrato ( d int, n string ) string {
	text  := n
	find  := strconv.Itoa (d)
	value := strings.Replace(text, find, "", -1)
	if value == "" { value="0" }
	if string(value[0]) == "0" {
		i,_   := strconv.ParseInt(value, 10, 64)
		value  = strconv.FormatInt(i, 10)
	}
	return value
}

func main() {
	var d int
	var n string
	for  {
		fmt.Scanln(&d, &n)
		if (d == 0) && (n == "0") { break }
		fmt.Printf("%s\n", contrato (d,  n))
	}
}

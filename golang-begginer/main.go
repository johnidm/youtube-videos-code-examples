package main

import "fmt"
import "golang-begginer/greeting"

func sum(a, b int) (int, bool) {
	return a + b, true
}

// Control Flow (if, for, switch)
// Arrays (fixed-size) and Slices (dynamic-size)

type Person struct {
	Name string
	Age int
}

type Speaker interface {
	Speak() string
}

func (p Person) Speak() string {
	return "Hello, my name is " + p.Name
}

func greet(name string, ch chan string) {
	ch <- "Hello, " + name
}

func main() {

	greeting.SayHello("John")

	ch := make(chan string)
	go greet("Alice", ch)
	message := <-ch 

	fmt.Println(message)

	fmt.Println("Hi, I am Johni!")
	result, ok := sum(1, 2)
	fmt.Println(result, ok)

	for i := 0; i <= 5; i++ {
		fmt.Println(i)
	}

	day := 2

	switch day {
	case 1:
		fmt.Println("Monday")
	case 2:
		fmt.Println("Tuesday")
	case 3:
		fmt.Println("Wednesday")
	case 4:
		fmt.Println("Thursday")
	case 5:
		fmt.Println("Friday")
	case 6:
		fmt.Println("Saturday")
	case 7:
		fmt.Println("Sunday")
	}

	var arr [3]int = [3]int {1, 2, 3}
	fmt.Println(arr)

	var slice []int = []int {1, 2, 3, 4, 5}
	fmt.Println(slice)

	fmt.Println(slice[1:4]) // Slicing from index 1 to 3 (4 is exclusive)

	// Maps (key - value pairs)

	//lists := make(map[string]int)

	names := map[string]int {
		"Joh": 30, 
		"Ana": 34,
		"Bob": 21,
	}

	// add a new itemn
	names["Alice"] = 34

	// Update
	names["Jon"] = 89

	// Get
	age, exists := names["Jon"]

	if exists {
		fmt.Println("Age: ", age)
	}

	// Remove
	delete(names, "Alice")

	for name, age := range names {
		fmt.Println(name, age)
	}

	person := Person{Name : "John", Age : 30}
	fmt.Println(person)

	var s Speaker = person
	fmt.Println(s.Speak())

	// Pointer holds the menory addresss of another variáble

	var x int = 58
	var p *int = &x // pointer to x

	fmt.Println("Values of x", x, "values of p", p)

}


// add_test.go
package main

import "testing"

// TestAdd tests the Add function
func TestAdd(t *testing.T) {
	result := Add(2, 3)
	expected := 5

	if result != expected {
		t.Errorf("Expected %d but got %d", expected, result)
	}
}

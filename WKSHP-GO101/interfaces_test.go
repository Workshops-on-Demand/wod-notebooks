package main

import (
	"math"
	"testing"
)

func TestRectArea(t *testing.T) {
	r := rect{width: 3, height: 4}
	expected := 12.0
	result := r.area()

	if result != expected {
		t.Errorf("Expected area %f but got %f", expected, result)
	}
}

func TestRectPerim(t *testing.T) {
	r := rect{width: 3, height: 4}
	expected := 14.0
	result := r.perim()

	if result != expected {
		t.Errorf("Expected perimeter %f but got %f", expected, result)
	}
}

func TestCircleArea(t *testing.T) {
	c := circle{radius: 5}
	expected := math.Pi * 25
	result := c.area()

	if result != expected {
		t.Errorf("Expected area %f but got %f", expected, result)
	}
}

func TestCirclePerim(t *testing.T) {
	c := circle{radius: 5}
	expected := 2 * math.Pi * 5
	result := c.perim()

	if result != expected {
		t.Errorf("Expected perimeter %f but got %f", expected, result)
	}
}

func TestMeasure(t *testing.T) {
	r := rect{width: 3, height: 4}
	c := circle{radius: 5}

	measureTests := []struct {
		g             geometry
		expectedArea  float64
		expectedPerim float64
	}{
		{r, 12.0, 14.0},
		{c, math.Pi * 25, 2 * math.Pi * 5},
	}

	for _, tt := range measureTests {
		if tt.g.area() != tt.expectedArea {
			t.Errorf("Expected area %f but got %f", tt.expectedArea, tt.g.area())
		}
		if tt.g.perim() != tt.expectedPerim {
			t.Errorf("Expected perimeter %f but got %f", tt.expectedPerim, tt.g.perim())
		}
	}
}

func TestMain(t *testing.T) {
	main()
}

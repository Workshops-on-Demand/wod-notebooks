// main.go
package main

import (
	"github.com/google/uuid"
)

// GenerateUUID generates a new UUID and returns it as a string.
func GenerateUUID() string {
	id := uuid.New().String()
	return id
}

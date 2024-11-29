// main_test.go
package main

import (
	"testing"

	"github.com/google/uuid"
)

func TestGenerateUUID(t *testing.T) {
	id := GenerateUUID()
	if _, err := uuid.Parse(id); err != nil {
		t.Errorf("Generated UUID is invalid: %s", id)
	}
}

package main

import (
	"fmt"
	"os"
	"os/exec"
	"strings"
)

// getEnv retrieves the value of the environment variable named by the key.
// If the variable is empty or not set, it returns the defaultValue.
func getEnv(key, defaultValue string) string {
	if value, exists := os.LookupEnv(key); exists && strings.TrimSpace(value) != "" {
		return value
	}
	return defaultValue
}

// getContainerID retrieves the Container ID of the most recently run container with the specified image.
func getContainerID(image string) (string, error) {
	// Execute 'docker ps -q -f ancestor=image -n 1'
	cmd := exec.Command("docker", "ps", "-q", "-f", fmt.Sprintf("ancestor=%s", image), "-n", "1")
	output, err := cmd.Output()
	if err != nil {
		return "", fmt.Errorf("error executing docker ps: %v", err)
	}

	containerID := strings.TrimSpace(string(output))
	if containerID == "" {
		return "", fmt.Errorf("no running container found for image %s", image)
	}

	return containerID, nil
}

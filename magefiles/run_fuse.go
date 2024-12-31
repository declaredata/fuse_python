package main

import (
	"fmt"

	"github.com/charmbracelet/log"
)

func RunFuse() {
	// Set default values for environment variables
	followLogs := getEnv("FUSE_FOLLOW_LOGS", "false")
	platform := getEnv("FUSE_PLATFORM", "linux/amd64")

	cfg, err := readConfig("bench/bench_config.toml")
	if err != nil {
		log.Fatalf("Error reading config: %v", err)
	}

	image := getFullImage(cfg)
	fmt.Printf("Running Fuse server: %s with platform %s\n", image, platform)

	volumeMounts, err := getVolumeMounts(cfg)
	if err != nil {
		log.Fatalf("couldn't get volume mounts (%s)", err)
	}

	dockerRunArgs := []string{
		"run",
		"-d",
		"-p", "8080:8080",
		"--platform", platform,
	}
	dockerRunArgs = append(dockerRunArgs, volumeMounts...)
	dockerRunArgs = append(dockerRunArgs, image)

	if err := executeCmd(
		"docker",
		dockerRunArgs,
		newCmdOptions(true, true, true, "."),
	); err != nil {
		log.Fatalf("Error running Docker container: %v", err)
	}

	// Retrieve the Container ID
	containerID, err := getContainerID(image)
	if err != nil {
		log.Fatalf("Error retrieving Container ID: %v", err)
	}

	if followLogs == "true" {
		fmt.Printf("Container %s started. Following logs...\n", containerID)
		dockerLogsArgs := []string{"logs", "-f", containerID}
		if err := executeCmd(
			"docker",
			dockerLogsArgs,
			newCmdOptions(true, true, true, "."),
		); err != nil {
			log.Fatalf("Error following Docker logs: %v", err)
		}
	} else {
		fmt.Printf("Container %s started. Not following logs.\n", containerID)
		dockerLogsArgs := []string{"logs", containerID}
		if err := executeCmd(
			"docker",
			dockerLogsArgs,
			newCmdOptions(true, true, true, "."),
		); err != nil {
			log.Fatalf("Error retrieving Docker logs: %v", err)
		}
	}
}

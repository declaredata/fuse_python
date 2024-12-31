package main

import "github.com/charmbracelet/log"

func PullFuse() {
	cfg, err := readConfig("bench/bench_config.toml")
	if err != nil {
		log.Fatalf("Error reading config: %v", err)
	}
	image := getFullImage(cfg)
	platform := "linux/amd64"
	log.Infof("pulling Fuse server image: %s", image)
	if err := executeCmd("docker", []string{
		"pull",
		"--platform",
		platform,
		image,
	}, false); err != nil {
		log.Fatal(err)
	}
}

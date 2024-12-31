package main

import "log"

func PullFuse() {
	cfg, err := readConfig("bench/bench_config.toml")
	if err != nil {
		log.Fatalf("Error reading config: %v", err)
	}
	image := getFullImage(cfg)
	platform := "linux/amd64"
	log.Printf("pulling Fuse server image: %s", image)
	if err := executeCmd("docker", []string{
		"pull",
		"--platform",
		platform,
		image,
	}, true); err != nil {
		log.Fatal(err)
	}
}

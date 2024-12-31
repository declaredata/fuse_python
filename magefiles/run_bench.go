package main

import "github.com/charmbracelet/log"

func RunBench() {
	log.Info("running homegrown benchmarks")
	if err := executeCmdInDir(
		"uv",
		[]string{
			"run",
			"python",
			"src/bench/main.py",
		},
		true,
		"bench",
	); err != nil {
		log.Fatal(err)
	}
	log.Info("running pytest benchmarks")
	if err := executeCmdInDir(
		"uv",
		[]string{"run", "pytest"},
		true,
		"bench",
	); err != nil {
		log.Fatal(err)
	}

}

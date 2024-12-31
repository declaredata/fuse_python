package main

import "github.com/charmbracelet/log"

func RunBench() {
	log.Info("running homegrown benchmarks")
	if err := executeCmd(
		"uv",
		[]string{
			"run",
			"python",
			"src/bench/main.py",
		},
		newCmdOptions(true, true, true, "bench"),
	); err != nil {
		log.Fatal(err)
	}
	log.Info("running pytest benchmarks")
	if err := executeCmd(
		"uv",
		[]string{"run", "pytest"},
		newCmdOptions(true, true, true, "bench"),
	); err != nil {
		log.Fatal(err)
	}

}

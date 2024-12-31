package main

import (
	"log"

	"github.com/spf13/cobra"
)

func runBench(_ *cobra.Command, _ []string) {
	log.Println("running homegrown benchmarks")
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
	log.Println("running pytest benchmarks")
	if err := executeCmdInDir(
		"uv",
		[]string{"run", "pytest"},
		true,
		"bench",
	); err != nil {
		log.Fatal(err)
	}

}

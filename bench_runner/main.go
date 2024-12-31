package main

import (
	"log"

	"github.com/spf13/cobra"
)

func main() {
	var rootCmd = &cobra.Command{
		Use:   "mycli",
		Short: "MyCLI is a tool with start-fuse and run-bench commands",
		Long:  `A simple CLI application to manage running benchmarks against a running Fuse server`,
	}

	// start-fuse subcommand
	var runFuseCmd = &cobra.Command{
		Use:   "run-fuse",
		Short: "Start the Fuse server",
		Long:  `Starts the Fuse server`,
		Run:   runFuse,
	}

	// run-bench subcommand
	var runBenchCmd = &cobra.Command{
		Use:   "run-bench",
		Short: "Run Benchmark",
		Long:  `Executes benchmark tests to evaluate performance.`,
		Run:   runBench,
	}

	var pullFuseCmd = &cobra.Command{
		Use:   "pull-fuse",
		Short: "pull a specified version of the Fuse server container",
		Long:  "",
		Run:   pullFuse,
	}

	rootCmd.AddCommand(runFuseCmd)
	rootCmd.AddCommand(runBenchCmd)
	rootCmd.AddCommand(pullFuseCmd)

	if err := rootCmd.Execute(); err != nil {
		log.Fatal(err)
	}
}

package main

import (
	"os"
	"os/exec"
	"strings"

	"github.com/charmbracelet/log"
)

func executeCmd(cmd string, args []string, logCmd bool) error {
	return executeCmdInDir(cmd, args, logCmd, ".")
}

func executeCmdInDir(cmd string, args []string, logCmd bool, dir string) error {
	if logCmd {
		log.Printf("%s %v", cmd, strings.Join(args, " "))
	}
	runCmd := exec.Command(cmd, args...)
	runCmd.Dir = dir

	runCmd.Stdout = os.Stdout
	runCmd.Stderr = os.Stderr
	if err := runCmd.Run(); err != nil {
		return err
	}
	return nil
}

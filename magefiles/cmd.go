package main

import (
	"io"
	"os"
	"os/exec"
	"strings"

	"github.com/charmbracelet/log"
)

type executeCmdOptions struct {
	// whether to log the command to stdout, prior to executing it
	logCmd bool
	// whether to send the command's stdout to os.Stdout, or /dev/null
	stdout bool
	// whether to send the command's stderr to os.Stderr, or /dev/null
	stderr bool
	// the current working directory that should be used. if this is set to
	// the empty string, defaults to "."
	directory string
}

func newCmdOptions(logCmd, stdout, stderr bool, directory string) *executeCmdOptions {
	return &executeCmdOptions{
		logCmd:    logCmd,
		stdout:    stdout,
		stderr:    stderr,
		directory: directory,
	}
}

func executeCmd(cmd string, args []string, opts *executeCmdOptions) error {
	if opts.logCmd {
		log.Infof("%s %v", cmd, strings.Join(args, " "))
	}
	runCmd := exec.Command(cmd, args...)
	if opts.directory != "" {
		runCmd.Dir = opts.directory
	}

	if opts.stdout {
		runCmd.Stdout = os.Stdout
	} else {
		runCmd.Stdout = io.Discard
	}
	if opts.stderr {
		runCmd.Stderr = os.Stderr
	} else {
		runCmd.Stderr = io.Discard
	}
	if err := runCmd.Run(); err != nil {
		return err
	}
	return nil
}

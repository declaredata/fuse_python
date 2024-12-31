package main

import (
	"errors"
	"fmt"
	"log"
	"path/filepath"

	"github.com/pelletier/go-toml"
)

type Config struct {
	MountDirectories map[string]string `toml:"mount_directories"`
	FuseTag          string            `toml:"fuse_tag"`
	Files            map[string]string `toml:"files"`
}

// readTagFromFile reads the TAG value from the specified file.
// It trims any whitespace and returns the TAG string.
func readConfig(filePath string) (*Config, error) {
	absPath, err := filepath.Abs(filePath)
	if err != nil {
		return nil, fmt.Errorf("unable to determine absolute path: %v", err)
	}
	log.Printf("reading config file from %s", absPath)

	tree, err := toml.LoadFile(absPath)
	if err != nil {
		return nil, err
	}

	var config Config
	if err := tree.Unmarshal(&config); err != nil {
		return nil, err
	}
	if len(config.FuseTag) == 0 {
		return nil, errors.New("fuse tag is missing")
	}
	return &config, nil
}

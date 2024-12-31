package main

import (
	"fmt"
	"path/filepath"
)

func getVolumeMounts(cfg *Config) ([]string, error) {
	mounts := []string{}
	for localDir, containerDir := range cfg.MountDirectories {
		absLocalPath, err := filepath.Abs(localDir)
		if err != nil {
			return nil, fmt.Errorf("couldn't find absolute path for local dir %s (%s)", localDir, err)
		}
		mounts = append(mounts, "-v")
		mounts = append(mounts, fmt.Sprintf(`%s:%s`, absLocalPath, containerDir))
	}
	return mounts, nil
}

func getFullImage(cfg *Config) string {
	tag := cfg.FuseTag
	return fmt.Sprintf("ghcr.io/declaredata/fuse:%s", tag)
}

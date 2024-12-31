import tomllib


def get_files() -> list[str]:
    with open("bench_config.toml", "rb") as f:
        data = tomllib.load(f)
        kvps = data["files"]
        return list(kvps.values())

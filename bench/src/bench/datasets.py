import tomllib

def get_files() -> list[str]:
    with open("bench/bench_config.toml", "rb") as f:
        data = tomllib.load(f)
        kvps = data["benchmark"]["files"]
        return kvps.values()


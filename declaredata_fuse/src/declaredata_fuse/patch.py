import os
import sys
import importlib
from types import ModuleType


class _FuseModuleRedirector:
    def __init__(self, target_base: str) -> None:
        self.target_base = target_base
        self.loaded_submodules: dict[str, ModuleType] = {}

    def __getattr__(self, name: str) -> ModuleType:
        if name not in self.loaded_submodules:
            target_name = f"{self.target_base}.{name}"
            module = importlib.import_module(target_name)
            self.loaded_submodules[name] = module
            sys.modules[f"pyspark.{name}"] = module
        return self.loaded_submodules[name]


def toggle_dd_fuse_patcher(*, enabled: bool):
    """
    When `enabled` is set to `True`, patch `sys.modules` so that all `import`s
    that start with `pyspark...` will instead import DeclareData's Fuse python
    client library.

    If you intend to use this function, make sure to do so at the _top_ of your
    program's entrypoint. For example:

    ```python
    #####
    # for best results, make sure this is the top line of your Python
    # program's entrypoint, and no code executes before it
    #####
    from fuse import toggle_dd_fuse_patcher
    #####
    # this line will patch all subsequent `pyspark...` imports to use
    # DeclareData's client library.
    #
    # pass `enabled=False` if you want this function to be a no-op
    #####
    toggle_dd_fuse_patcher(enabled=True)
    ```

    For more information, see https://github.com/declaredata/fuse_python
    """
    if enabled:
        sys.modules["pyspark"] = _FuseModuleRedirector("declaredata_fuse")


def toggle_dd_fuse_patcher_from_env() -> None:
    """
    This function is equivalent to calling `toggle_dd_fuse_patcher`, except
    it determines whether the patcher should be enabled by looking for an
    environment variable called `DD_FUSE_PATCH`.

    If you set the value of that environment variable to a "truthy" value
    (see below), this function will in turn call
    `toggle_dd_fuse_patcher(enabled=True). Otherwise, it will call
    `toggle_dd_fuse_patcher(enabled=False)`

    The list of "truthy" values is as follows:

    - "true"
    - "True"
    - "on"
    - "1"

    Before using this function, please read the rules about where to call this
    function in the doc for the above `toggle_dd_fuse_patcher` function.
    """
    env_raw = os.getenv("DD_FUSE_PATCH", "false")
    truthy_vals = {"true", "True", "on", "1"}
    env_set = env_raw in truthy_vals
    toggle_dd_fuse_patcher(enabled=env_set)

import os


def assert_env(name: str) -> str:
    env = os.environ.get(name)
    assert env
    return env

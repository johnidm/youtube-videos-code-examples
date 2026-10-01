
## Create a project

```
curl -LsSf https://astral.sh/uv/install.sh | sh

uv init my-app --no-package cd my-app

uv python list | grep 3.15

uv python install 3.15.0rc2

uv python pin 3.15.0rc2

uv run python --version

uv run main.py
```

https://docs.python.org/3.15/library/profiling.sampling.html

https://docs.python.org/3.15/library/profiling.html

```
sudo -E uv run python -m profiling.sampling run main.py

sudo -E uv run python -m profiling.sampling run --flamegraph -o profile.html main.py

sudo -E uv run python -m profiling.sampling run --flamegraph main.py

sudo -E uv run python -m profiling.sampling run --live main.py

sudo -E uv run python -m profiling.tracing main.py

```
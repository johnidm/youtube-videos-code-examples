curl -LsSf https://astral.sh/uv/install.sh | sh

uv init my-app --no-package
cd my-app

uv python install 3.14
uv python pin 3.14

uv run python --version

uv add requests
uv add --dev ruff

uv run hello.py
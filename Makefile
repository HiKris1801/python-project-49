install:#install dependencies
	uv sync
braing-games:
	uv run brain-games
build:
	uv build
package-install:
	uv tool install dist/*.whl
make lint:
	uv run ruff chek brain_games
make check: 
	test lint

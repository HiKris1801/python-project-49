install:#install dependencies
	uv sync
braing-games:
	uv run brain-games
build:
	uv build
package-install:
	uv tool install dist/*.whl
make lint:
	uv run ruff check brain_games
braing-even:
	uv run brain-even


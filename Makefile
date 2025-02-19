install:#install dependencies
	uv sync
braing-games:
	uv run brain-games
build:
	uv build
package-install:
	uv tool install dist/*.whl

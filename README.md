# RSS-API

## Dependency Management

This project uses [pipenv](https://pipenv.pypa.io/) for dependency management. To install or update dependencies:

- To install exactly what is specified in `Pipfile.lock` (reproducible environment):
	```bash
	pipenv sync
	```
- To update all packages to the latest allowed by your `Pipfile` and regenerate `Pipfile.lock`:
	```bash
	pipenv update
	```
- To update a specific package and regenerate `Pipfile.lock`:
	```bash
	pipenv update <package-name>
	```

Make sure to activate your pipenv shell or use `pipenv run` for commands if not already inside the environment.

## Running the API Locally

Start API locally via

```
pipenv run uvicorn api.main:app --reload
```

Ensure you have a VPN connection to the server and opened a tunnel to the db.

The API returns title, text and ts_item_published for all articles within the specified time range. 

## Versioning with bumpver

This project uses [bumpver](https://github.com/mbarkhau/bumpver) for version management, following calendar versioning (`YYYY.MM.PATCH`). Versioning is configured in `pyproject.toml`.

- To bump the patch version (e.g., `2025.11.0` → `2025.11.1`):
	```bash
	bumpver update --patch
	```
- To bump the minor version (e.g., `2025.11.1` → `2025.12.1`):
	```bash
	bumpver update --minor
	```
- To bump the major version (e.g., `2025.12.1` → `2026.1.1`):
	```bash
	bumpver update --major
	```
- To preview the version change without making changes, use the `--dry` flag:
	```bash
	bumpver update --dry --patch
	```

By default, bumpver will update the version, commit, tag, and push the changes as configured in `pyproject.toml`.


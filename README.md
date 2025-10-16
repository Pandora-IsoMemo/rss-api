# RSS-API

Start API locally via

```
uvicorn api.main:app --reload
```

The API runs currently on a csv file, access example:

```
http://127.0.0.1:8000/items/?start_date=2024-08-04T00:00:00&end_date=2024-08-05T23:59:59
```

The API returns title, text and ts_item_published for all articles within the specified time range. 

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

## Versioning

The project uses calender versioning (`YYYY.MM.PATCH`). The following statement updates the version and pushes the update directly to github.

```
bumpver update --patch
```

To see how the version would be updated, use the `--dry` flag:

```
bumpver update --dry --patch
```


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

## Versioning

The project uses calender versioning (`YYYY.MM.PATCH`). The following statement updates the version and pushes the update directly to github.

```
bumpver update --patch
```

To see how the version would be updated, use the `--dry` flag:

```
bumpver update --dry --patch
```


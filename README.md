# Website Status Checker

A simple Python script that checks whether websites are up or down. It reads URLs from a file, visits each one using the `requests` module, and prints a report on the screen and saves it to `report.txt`.

## Features

- Reads URLs from `sites.txt`, one per line
- Shows the status code, response time (ms) and whether the site redirected
- Labels each site as `UP`, `CLIENT ERROR`, `SERVER ERROR`, `TIMEOUT`, `UNREACHABLE` or `INVALID URL`
- Prints a summary with the total, UP and NOT UP counts
- Saves the same report to `report.txt`

## Requirements

- Python 3
- `requests`

```bash
pip install requests
```

## Usage

1. Add your URLs to `sites.txt`, one per line:

```
https://www.google.com
http://github.com
https://httpbin.org/status/404
https://httpbin.org/status/500
https://httpbin.org/delay/10
https://thisdomaindoesnotexist12345.com
google.com
```

2. Run the script:

```bash
python checker.py
```

## Example Output

```
URL                                       STATUS   TIME(ms)   REDIRECTED   RESULT
https://www.google.com                    200      145        No           UP
http://github.com                         200      320        Yes          UP
https://httpbin.org/status/404            404      610        No           CLIENT ERROR
https://httpbin.org/status/500            500      598        No           SERVER ERROR
https://httpbin.org/delay/10              -        -          -            TIMEOUT
https://thisdomaindoesnotexist12345.com   -        -          -            UNREACHABLE
google.com                                -        -          -            INVALID URL

SUMMARY
-------
Total sites checked : 7
UP                  : 2
NOT UP              : 5
```

## Result Labels

| Label | Meaning |
|---|---|
| UP | Status code 200 to 299 |
| CLIENT ERROR | Status code 400 to 499 |
| SERVER ERROR | Status code 500 to 599 |
| TIMEOUT | No reply within 5 seconds |
| UNREACHABLE | Site could not be reached |
| INVALID URL | URL is not written correctly (for example, missing `http://` or `https://`) |

## Files

| File | Purpose |
|---|---|
| `checker.py` | The main script |
| `sites.txt` | List of URLs to check |
| `report.txt` | Report created when the script runs |
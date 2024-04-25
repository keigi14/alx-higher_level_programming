0x10-python-network_0

This collection consists of 10 tasks for the Python Network #0 project. The tasks encompass various concepts such as cURL, HTTP, and HTTPS protocols, headers, and web scraping.

## Task Overview
Outlined below are the tasks included in this repository:

| Task | Description |
| --- | --- |
| [0-body_size.sh](./0-body_size.sh) | This Bash script takes a URL as input, sends a request to that URL, and displays the size of the response body in bytes. |
| [1-body.sh](./1-body.sh) | This Bash script accepts a URL, sends a GET request to it, and displays the response body. |
| [2-delete.sh](./2-delete.sh) | Sends a DELETE request to a specified URL and displays the response body. |
| [3-methods.sh](./3-methods.sh) | Displays all HTTP methods accepted by the server for a given URL. |
| [4-header.sh](./4-header.sh) | Sends a GET request to a URL, displays the response body, and includes a header variable `X-HolbertonSchool-User-Id` with a value of `98`. |
| [5-post_params.sh](./5-post_params.sh) | Sends a POST request to a URL, displaying the response body, and sets variables `email` to `hr@holbertonschool.com` and `subject` to `I will always be here for PLD`. |
| [6-peak.py](./6-peak.py) | Python function to find a peak in an unsorted list of integers with a time complexity of `O(log(n))`. |
| [100-status_code.sh](./100-status_code.sh) | Sends a request to a specified URL and displays only the status code of the response. |
| [101-post_json.sh](./101-post_json.sh) | Sends a JSON POST request to a specified URL and displays the response body. |
| [102-catch_me.sh](./102-catch_me.sh) | Requests `0.0.0.0:5000/catch_me` causing the server to respond with `You got me!`. |

Each task is accompanied by detailed instructions on its expected behavior and implementation.

## Task Descriptions
Outlined are the functionalities of each task:

### Task 0: 0-body_size.sh
A Bash script that retrieves the size of the response body in bytes for a given URL.

### Task 1: 1-body.sh
A Bash script that retrieves and displays the response body of a GET request to a provided URL.

### Task 2: 2-delete.sh
A Bash script that sends a DELETE request to a specified URL and displays the response body.

### Task 3: 3-methods.sh
A Bash script that identifies the HTTP methods supported by a server for a given URL.

### Task 4: 4-header.sh
A Bash script that sends a GET request to a URL, displays the response body, and includes a custom header `X-HolbertonSchool-User-Id` with a value of `98`.

### Task 5: 5-post_params.sh
A Bash script that sends a POST request to a URL, displaying the response body, and sets specific variables.

### Task 6: 6-peak.py
A Python function that finds a peak in an unsorted list of integers with a specified time complexity.

### Task 100: 100-status_code.sh
A Bash script that retrieves and displays only the status code of a response for a provided URL.

### Task 101: 101-post_json.sh
A Bash script that sends a JSON POST request to a URL and displays the response body.

### Task 102: 102-catch_me.sh
A Bash script that triggers a specific response from a server endpoint.

## Usage
To execute the Bash scripts:

```bash
./script.sh [URL]
```

For instance, to run `0-body_size.sh`:

```bash
./0-body_size.sh http://example.com
```

## Contributing
To contribute to this project:

1. Fork the repository.
2. Create a new branch with your feature: `git checkout -b my-feature`.
3. Commit your changes: `git commit -m "feat: add new feature"`.
4. Push to the branch: `git push origin my-feature`.
5. Submit a pull request with your changes.


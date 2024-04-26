# 0x11. Python - Network #1

## Description
This repository contains Python scripts written as part of the "0x11. Python - Network #1" project at Holberton School. The scripts demonstrate various network operations using Python, focusing on fetching internet resources, making HTTP requests, handling responses, and interacting with APIs.

## Learning Objectives
At the end of this project, students are expected to be able to:

- Fetch internet resources with the Python package urllib.
- Decode urllib body response.
- Use the Python package requests for simplified HTTP requests.
- Make HTTP GET, POST, PUT, etc. requests.
- Fetch JSON resources.
- Manipulate data from an external service.

## Requirements
- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A README.md file at the root of the repo, containing a description of the repository
- Your code should use pycodestyle (version 2.8.\*) for styling
- All files must be executable
- The length of your files will be tested using wc
- All modules should have documentation
- Use `get` to access dictionary value by key
- Ensure code is not executed when imported

## Tasks
1. **0-hbtn_status.py**
   - Fetches https://alx-intranet.hbtn.io/status using urllib.
   - Display the body response.
  
2. **1-hbtn_header.py**
   - Takes a URL, sends a request, and displays the value of the X-Request-Id variable in the response header using urllib.

3. **2-post_email.py**
   - Sends a POST request with an email parameter to a given URL using urllib.
   - Displays the body of the response.

4. **3-error_code.py**
   - Sends a request to a URL using urllib.
   - Displays the body of the response and handles HTTPError exceptions.

5. **4-hbtn_status.py**
   - Fetches https://alx-intranet.hbtn.io/status using the requests package.
   - Display the body response.

6. **5-hbtn_header.py**
   - Takes a URL, sends a request, and displays the value of the X-Request-Id variable in the response header using requests.

7. **6-post_email.py**
   - Sends a POST request with an email parameter to a given URL using requests.
   - Displays the body of the response.

8. **7-error_code.py**
   - Sends a request to a URL using requests.
   - Displays the body of the response and handles HTTP status codes.

9. **8-json_api.py**
   - Sends a POST request with a letter parameter to a URL.
   - Displays the id and name from the JSON response or appropriate messages.

10. **10-my_github.py**
    - Uses Basic Authentication with a personal access token to access GitHub API.
    - Displays the user's id using provided credentials.

11. **100-github_commits.py**
    - Utilizes the GitHub API to list 10 commits (from the most recent to oldest) of a specified repository by a user.
    - Prints commits by `<sha>: <author name>` format.

## Resources
- [HOWTO Fetch Internet Resources Using urllib Package](https://docs.python.org/3/howto/urllib2.html)
- [Quickstart with Requests package](https://docs.python-requests.org/en/latest/user/quickstart/)
- [Requests package](https://docs.python-requests.org/en/latest/)
 

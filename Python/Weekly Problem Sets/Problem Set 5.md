# Problem Set 5 — Recursion & HTTP / APIs

**Topics covered:** recursion, `requests` module, REST APIs, HTTP methods and requests

**Autograder note:** When using automated tests, it often requires exact function names, parameter lists, and return types. Do not rename functions or change parameter names/order; avoid extra print statements unless the instructions ask for them; prefer returning values over printing when specified. Wrap any demonstration or test code in an `if __name__ == "__main__":` block so autograders can import your functions cleanly.

Work on a new branch named `python/problem-set-5` for this problem set.  Your submitted script must be named `Problem Set 5 starter.py` or `Problem Set 5.py` for it to be picked up by the autograder.  Once you have passed all tests, you can merge your code back into main.

## Submitting Your Work
As stated above, you should create a new branch and checkout that branch for this problem set called `python/problem-set-5`.  The general flow is shown below.

1. Fork the `AFC-AI2C/summer-course` repo (you only need to do this once)
   - This will create your own personal repo at `<github-username>/summer-course`
   - You have full ownership of that repo
2. Clone your personal repo locally (you only need to do this once)
3. Create and switch to a new branch called `python/problem-set-5`
4. Perform your work in either `Problem Set 5 starter.py` or a new file called `Problem Set 5.py`
5. Commit your changes
6. Push your changes
7. Review the output in GitHub Actions.  You can click into each run separately to see feedback
8. Fix any issues and repeat steps 5-7.
9. Once complete for all problems, you can merge your work back into main.

---

## Problem 1 — Basic Recursion

**Your task:**
- **Create a squares list using recursion**
  - Given an integer `n`, return a list of squares from `1..n` using recursion
  - Name your function `recursive_squares`
  - For example, if `n=5` then the function returns `[1, 4, 9, 16, 25]`
  - You only need to create the list using recursion, not the squares

- **Palindrome checker**
  - Given a string, check if it is a palindrome using recursion.  That is, is the string the same forwards and backwards, case insensitive.
  - Name your function `palindrome_checker`
  - For example, the input string `bacon` would return `False` while the string `radar` would return `True`.
  - Note, for our purposes, an empty string is a palindrome.
  - Note, for our purposes, punctuation and white space should be included.

- **List length**
  - Given a list, determine the length of the list using recursion
  - Name your function `length`
  - For example, the input list `[1, 2, 3]` would return `3`

### Challenge

- **Flatten**
  - Given a list, flatten the list into a single list using recursion.
  - Name your function `flatten`
  - For example, given `[1, [2, 3], [4], 5]` return `[1, 2, 3, 4, 5]`

---

## Problem 2 — Multiple Recursion

**Your task:**
- **Fibonacci sequence**
  - Given an integer `n`, return the nth Fibonacci number using multiple recursion
  - Name your function `fibonacci`
  - The Fibonacci sequence is: 0, 1, 1, 2, 3, 5, 8, 13, 21...
  - For example, `fibonacci(0)` returns `0`, `fibonacci(1)` returns `1`, `fibonacci(6)` returns `8`
  - Note: Use 0-based indexing (the sequence starts at index 0)

- **Count ways to climb stairs**
  - Given `n` stairs, return the number of distinct ways to climb to the top if you can take 1 or 2 steps at a time
  - Name your function `count_ways`
  - Use multiple recursion (consider both taking 1 step and taking 2 steps)
  - For example, `count_ways(3)` returns `3` (there are 3 ways: 1+1+1, 1+2, 2+1)
  - For example, `count_ways(4)` returns `5` (1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2)
  - Note: `count_ways(0)` returns `1` (one way to stay at the ground), `count_ways(1)` returns `1`

- **Grid paths**
  - Given a grid of size `m x n`, count the number of unique paths from top-left corner `(0,0)` to bottom-right corner `(m-1, n-1)`
  - You can only move right or down at any point
  - Name your function `grid_paths`
  - It should take two parameters: `m` (rows) and `n` (columns)
  - For example, `grid_paths(2, 2)` returns `2` (right-down or down-right)
  - For example, `grid_paths(3, 3)` returns `6`
  - Note: `grid_paths(1, 1)` returns `1`, `grid_paths(1, n)` returns `1`, `grid_paths(m, 1)` returns `1`

### Challenge

- **Generate all permutations**
  - Given a list of unique integers, return all possible permutations using recursion
  - Name your function `permutations`
  - For example, `permutations([1, 2])` returns `[[1, 2], [2, 1]]` (order doesn't matter)
  - For example, `permutations([1, 2, 3])` returns `[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]` (order doesn't matter)
  - An empty list returns `[[]]` (a list containing the empty list)


---

## Problem 3 — Basic HTTP Requests

For this problem, you'll create functions that make HTTP requests using different methods (GET, POST, PUT, DELETE) to the JSONPlaceholder API. This is a free fake REST API designed for testing that returns realistic responses. The base URL is `https://jsonplaceholder.typicode.com`.

**Note:** JSONPlaceholder is a mock API - it doesn't actually persist changes, so every request gets a fresh dataset. This is perfect for testing!

**Your task:**

- **`get_user(user_id: int) -> dict`**
  - Make a GET request to `https://jsonplaceholder.typicode.com/users/{user_id}`
  - Replace `{user_id}` with the provided user ID (1-10 are valid)
  - The API returns the user object directly as JSON (no nested "data" key)
  - Return the entire user dictionary
  - If the request fails (status code is not 200), return an empty dictionary `{}`
  - Example return: `{"id": 2, "name": "Ervin Howell", "username": "Antonette", "email": "Shanna@melissa.tv", ...}`

- **`create_user(name: str, job: str) -> dict`**
  - Make a POST request to `https://jsonplaceholder.typicode.com/users`
  - Send JSON data in the body: `{"name": name, "job": job}`
  - Hint: Use `requests.post(url, json={"name": name, "job": job})`
  - The API returns JSON with the created user including an `"id"` field
  - Return the entire response dictionary
  - If the request fails (status code is not 201), return an empty dictionary `{}`
  - Example return: `{"name": "John Doe", "job": "Developer", "id": 11}`

- **`update_user(user_id: int, name: str, job: str) -> dict`**
  - Make a PUT request to `https://jsonplaceholder.typicode.com/users/{user_id}`
  - Send JSON data in the body: `{"name": name, "job": job}`
  - Hint: Use `requests.put(url, json={"name": name, "job": job})`
  - The API returns JSON with the updated data including an `"id"` field
  - Return the entire response dictionary
  - If the request fails (status code is not 200), return an empty dictionary `{}`
  - Example return: `{"name": "Jane Smith", "job": "Manager", "id": 2}`

- **`delete_user(user_id: int) -> bool`**
  - Make a DELETE request to `https://jsonplaceholder.typicode.com/users/{user_id}`
  - Hint: Use `requests.delete(url)`
  - The API returns status code 200 for successful deletion
  - Return `True` if status code is 200, otherwise return `False`

**Example usage:**
```python
# GET a user
user = get_user(2)
print(f"User: {user['name']} ({user['email']})")

# POST to create a user
new_user = create_user("John Doe", "Developer")
print(f"Created user with ID: {new_user['id']}")

# PUT to update a user
updated = update_user(2, "Jane Smith", "Manager")
print(f"Updated: {updated}")

# DELETE a user
success = delete_user(2)
print(f"Deleted: {success}")
```

### Challenge

- **`get_users_page(page: int) -> list[dict]`**
  - Make a GET request to `https://reqres.in/api/users?page={page}`
  - See: [ReqRes API - List Users](https://reqres.in/docs#get-api-users)
  - The API returns JSON with format: `{"page": 1, "data": [...]}`
  - Return the list of users from the `"data"` key
  - If the request fails or page is invalid, return an empty list `[]`
  - Valid pages are 1-2 (each page has 6 users)

- **`partial_update_user(user_id: int, updates: dict) -> dict`**
  - Make a PATCH request to `https://reqres.in/api/users/{user_id}`
  - Send the `updates` dictionary as JSON data in the body
  - See: [ReqRes API - Patch](https://reqres.in/docs#patch-api-users-2)
  - PATCH is used for partial updates (unlike PUT which replaces the entire resource)
  - Return the entire response dictionary
  - If the request fails (status code is not 200), return an empty dictionary `{}`
  - Example: `partial_update_user(2, {"job": "Senior Developer"})` updates only the job field


---

## Problem 4 — Authenticated REST APIs

For this problem, you'll work with real-world APIs that require authentication. You'll learn two common authentication patterns: API keys and Bearer tokens.

### Setup Instructions

**TMDB API Key (for problem 1):**
1. Go to https://www.themoviedb.org/ and create a free account
2. Go to Settings → API → Request an API Key
3. Choose "Developer" option and fill out the form (use "Educational" as the purpose)
4. You'll receive an API key (v3 auth) - save this

**GitHub Personal Access Token (for problems 2-4):**
1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token (classic)
3. Give it a name like "Python Course API Practice"
4. Select scopes: `gist` (for creating/deleting gists) and `repo` (for viewing repos)
5. Generate token and **save it immediately** (you can't see it again!)

**Important:** Never commit API keys or tokens to git! Store them in environment variables or a config file that's in `.gitignore`.

---

**Your task:**

- **`search_movie(api_key: str, query: str) -> dict`**
  - Make a GET request to `https://api.themoviedb.org/3/search/movie`
  - Include query parameters: `api_key` and `query`
  - See: [TMDB API - Search Movies](https://developers.themoviedb.org/3/search/search-movies)
  - The API returns JSON with format: `{"results": [...]}`
  - Return the first movie from the `"results"` list (if any)
  - If the request fails or no results found, return an empty dictionary `{}`
  - Example: `search_movie(YOUR_KEY, "Inception")` returns info about the movie Inception

- **`get_github_user(token: str, username: str) -> dict`**
  - Make a GET request to `https://api.github.com/users/{username}`
  - Include authorization header: `{"Authorization": f"Bearer {token}"}`
  - See: [GitHub API - Get a user](https://docs.github.com/en/rest/users/users#get-a-user)
  - Return the entire response JSON
  - The response includes: `"login"`, `"name"`, `"public_repos"`, `"followers"`, etc.
  - If the request fails, return an empty dictionary `{}`
  - Example: `get_github_user(YOUR_TOKEN, "torvalds")` returns Linus Torvalds' profile

- **`create_gist(token: str, description: str, filename: str, content: str) -> str`**
  - Make a POST request to `https://api.github.com/gists`
  - Include authorization header: `{"Authorization": f"Bearer {token}"}`
  - Send JSON body with this structure:
    ```python
    {
        "description": description,
        "public": True,
        "files": {
            filename: {
                "content": content
            }
        }
    }
    ```
  - See: [GitHub API - Create a gist](https://docs.github.com/en/rest/gists/gists#create-a-gist)
  - The API returns the created gist data including an `"id"` field
  - Return the gist ID (as a string)
  - If the request fails (status code is not 201), return an empty string `""`
  - Example: `create_gist(YOUR_TOKEN, "Test gist", "hello.py", "print('Hello')")` creates a gist and returns its ID

- **`delete_gist(token: str, gist_id: str) -> bool`**
  - Make a DELETE request to `https://api.github.com/gists/{gist_id}`
  - Include authorization header: `{"Authorization": f"Bearer {token}"}`
  - See: [GitHub API - Delete a gist](https://docs.github.com/en/rest/gists/gists#delete-a-gist)
  - The API returns status code 204 for successful deletion
  - Return `True` if status code is 204, otherwise return `False`
  - Example: `delete_gist(YOUR_TOKEN, "abc123...")` deletes the gist

**Example usage:**
```python
TMDB_API_KEY = os.getenv("TMDB_API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# Search for a movie
movie = search_movie(TMDB_API_KEY, "The Matrix")
print(f"Title: {movie['title']}, Year: {movie['release_date'][:4]}")

# Get GitHub user info
user = get_github_user(GITHUB_TOKEN, "octocat")
print(f"{user['name']} has {user['public_repos']} public repos")

# Create and delete a gist
gist_id = create_gist(GITHUB_TOKEN, "My test gist", "test.txt", "Hello World!")
print(f"Created gist: https://gist.github.com/{gist_id}")
success = delete_gist(GITHUB_TOKEN, gist_id)
print(f"Deleted: {success}")
```

### Challenge

- **`get_spotify_track_info(access_token: str, track_id: str) -> dict`**
  - **Note:** This is more complex as Spotify uses OAuth2 authentication
  - You need to get an access token first using the Client Credentials flow
  - Make a GET request to `https://api.spotify.com/v1/tracks/{track_id}`
  - Include authorization header: `{"Authorization": f"Bearer {access_token}"}`
  - See: [Spotify API - Get Track](https://developer.spotify.com/documentation/web-api/reference/get-track)
  - Return a dictionary with these keys extracted from the response:
    - `"name"`: Track name
    - `"artist"`: First artist name (from `artists[0]["name"]`)
    - `"album"`: Album name (from `album["name"]`)
    - `"duration_ms"`: Duration in milliseconds
  - If the request fails, return an empty dictionary `{}`
  
  **Helper function to get access token:**
  ```python
  def get_spotify_token(client_id: str, client_secret: str) -> str:
      """Get Spotify access token using Client Credentials flow"""
      import base64
      
      # Encode credentials
      credentials = f"{client_id}:{client_secret}"
      encoded = base64.b64encode(credentials.encode()).decode()
      
      # Request token
      url = "https://accounts.spotify.com/api/token"
      headers = {"Authorization": f"Basic {encoded}"}
      data = {"grant_type": "client_credentials"}
      
      response = requests.post(url, headers=headers, data=data)
      if response.status_code == 200:
          return response.json()["access_token"]
      return ""
  ```
  
  **Getting Spotify credentials:**
  1. Go to https://developer.spotify.com/dashboard
  2. Log in and create an app
  3. Copy your Client ID and Client Secret
  
  **Example:** `get_spotify_track_info(token, "3n3Ppam7vgaVa1iaRUc9Lp")` returns info about a track


---

## References

### Recursion
- [Real Python - Thinking Recursively in Python](https://realpython.com/python-thinking-recursively/)
- [GeeksforGeeks - Recursion in Python](https://www.geeksforgeeks.org/recursion-in-python/)

### HTTP and APIs
- [Requests Library Documentation](https://requests.readthedocs.io/en/latest/)
- [Real Python - Python's Requests Library Guide](https://realpython.com/python-requests/)
- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- [HTTP Methods (GET, POST, PUT, PATCH, DELETE)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
- [Working with JSON in Python](https://realpython.com/python-json/)

### API Authentication
- [API Keys vs Bearer Tokens](https://stackoverflow.com/questions/34013299/web-api-authentication-basic-vs-bearer)
- [Understanding OAuth2](https://www.oauth.com/oauth2-servers/background/)
- [HTTP Headers for Authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)

### APIs Used in This Problem Set
- [ReqRes API Documentation](https://reqres.in/docs)
- [TMDB API Documentation](https://developers.themoviedb.org/3/getting-started/introduction)
- [GitHub REST API Documentation](https://docs.github.com/en/rest)
- [Spotify Web API Documentation](https://developer.spotify.com/documentation/web-api)

### REST API Concepts
- [What is a REST API?](https://www.redhat.com/en/topics/api/what-is-a-rest-api)
- [RESTful API Design Best Practices](https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/)


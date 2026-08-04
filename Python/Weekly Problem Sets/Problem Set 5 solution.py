"""Problem Set 5 — Recursion & HTTP / APIs"""


# ── Problem 1 ─────────────────────────────────────────────────────────────────
def recursive_squares(num: int) -> list[int]:
    # base cases
    if num == 0:
        return []
    if num == 1:
        return [1]

    # recursive step
    childs_list = recursive_squares(num - 1)

    # add our number to child's
    square = num**2
    childs_list.append(square)

    return childs_list


def palindrome_checker(value: str) -> bool:
    value = value.lower()
    # base cases
    if len(value) == 0:
        return True
    if len(value) == 1:
        return True
    if len(value) == 2 and value[0] == value[-1]:
        return True
    if value[0] != value[-1]:
        return False

    # recursive step
    result = palindrome_checker(value[1:-1])
    return result


def length(input_list: list) -> int:
    # base case
    if input_list == []:
        return 0

    # recursive step
    child_depth = length(input_list[1:])

    return 1 + child_depth


## Challenge Problem
def flatten(input_list: list) -> list:
    # base case
    if input_list == []:
        return []

    # work / recurse
    if isinstance(input_list[0], list):
        first_element = flatten(input_list[0])
    else:
        first_element = [input_list[0]]

    # recurse remaining elements
    remaining_elements = flatten(input_list[1:])

    result = first_element + remaining_elements
    return result


# ── Problem 2 ─────────────────────────────────────────────────────────────────
def fibonacci(n: int) -> int:
    # base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    # multiple recursive calls
    return fibonacci(n - 1) + fibonacci(n - 2)


def count_ways(n: int) -> int:
    # base cases
    if n == 0:
        return 1  # one way to stay at ground
    if n == 1:
        return 1  # only one step

    # multiple recursive calls: take 1 step OR take 2 steps
    one_step = count_ways(n - 1)
    two_steps = count_ways(n - 2)

    return one_step + two_steps


def grid_paths(m: int, n: int) -> int:
    # base cases
    if m == 1 or n == 1:
        return 1  # only one path along edge

    # multiple recursive calls: move down OR move right
    move_down = grid_paths(m - 1, n)
    move_right = grid_paths(m, n - 1)

    return move_down + move_right


## Challenge Problem
def permutations(lst: list) -> list[list]:
    # base case
    if len(lst) == 0:
        return [[]]

    result = []

    # for each element, make it the first and permute the rest
    for i in range(len(lst)):
        current = lst[i]
        remaining = lst[:i] + lst[i + 1 :]

        # multiple recursive calls (one per remaining element)
        for perm in permutations(remaining):
            result.append([current] + perm)

    return result


# ── Problem 3 ─────────────────────────────────────────────────────────────────
import requests


def get_user(user_id: int) -> dict:
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return {}


def create_user(name: str, job: str) -> dict:
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.post(url, json={"name": name, "job": job})

    if response.status_code == 201:
        return response.json()

    return {}


def update_user(user_id: int, name: str, job: str) -> dict:
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.put(url, json={"name": name, "job": job})

    if response.status_code == 200:
        return response.json()

    return {}


def delete_user(user_id: int) -> bool:
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.delete(url)

    return response.status_code == 200


## Challenge Problems
def get_all_users() -> list[dict]:
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return []


def partial_update_user(user_id: int, updates: dict) -> dict:
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.patch(url, json=updates)

    if response.status_code == 200:
        return response.json()

    return {}


# ── Problem 4 ─────────────────────────────────────────────────────────────────
def search_movie(api_key: str, query: str) -> dict:
    url = "https://api.themoviedb.org/3/search/movie"
    params = {"api_key": api_key, "query": query}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        results = data.get("results", [])
        if results:
            return results[0]

    return {}


def get_github_user(token: str, username: str) -> dict:
    url = f"https://api.github.com/users/{username}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()

    return {}


def create_gist(token: str, description: str, filename: str, content: str) -> str:
    url = "https://api.github.com/gists"
    headers = {"Authorization": f"Bearer {token}"}
    data = {"description": description, "public": True, "files": {filename: {"content": content}}}
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        return response.json().get("id", "")

    return ""


def delete_gist(token: str, gist_id: str) -> bool:
    url = f"https://api.github.com/gists/{gist_id}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.delete(url, headers=headers)

    return response.status_code == 204


## Challenge Problem
def get_spotify_track_info(access_token: str, track_id: str) -> dict:
    url = f"https://api.spotify.com/v1/tracks/{track_id}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return {
            "name": data.get("name", ""),
            "artist": data.get("artists", [{}])[0].get("name", ""),
            "album": data.get("album", {}).get("name", ""),
            "duration_ms": data.get("duration_ms", 0),
        }

    return {}

import requests

def get_todo_list() -> None:
    url = "https://jsonplaceholder.typicode.com/todos/1"

    #1.Make the Request
    response = requests.get(url)

    # 2. Check Status Code (200 means OK)
    print(f"Status Code: {response.status_code}")

    # 3. Print raw text (It looks like a string)
    print(f"Raw Data: {response.text}")

    if response.status_code == 200:
        # 1. Convert JSON string -> Python Dictionary
        data = response.json()

        # 2. Now we can access keys!
        print(f"Task: {data['title']}")
        print(f"Completed: {data['completed']}")
    else:
        print("Failed to fetch data")

def get_user_posts(user_id: int) -> None:
    url = "https://jsonplaceholder.typicode.com/posts"

    # We pass parameters as a dictionary
    # This turns the URL into: .../posts?userId=1
    params = {"user_id": user_id}

    response = requests.get(url, params=params)

    posts = response.json() # This returns a LIST of dictionaries
    print(f"\n--- Posts by User {user_id} ---")
    for post in posts[:3]: # Just print the first 3
        print(f"- {post['title']}")


def create_post() -> None:
    url = "https://jsonplaceholder.typicode.com/posts"

    # The data we want to send
    new_post: dict[str, str | int] = {
        "title": "Learning Backend",
        "body": "This is my first API call using Python!",
        "userId": 1
    }

    # Use .post() instead of .get()
    response = requests.post(url, json=new_post)

    print(f"\n--- Create Post Response ---")
    print(f"Status: {response.status_code}") # Should be 201 (Created)
    print(f"Response: {response.json()}")


if __name__ == "__main__":
    print("--- API CLIENT STARTED ---")
    get_todo_list()
    get_user_posts(1)

    create_post()
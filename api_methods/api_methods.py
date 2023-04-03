import requests
import uuid


def create_task(driver,payload, url):
    return requests.put(f"{url}create-task", json=payload)


def update_task(driver, payload, url):
    return requests.put(f"{url}update-task", json=payload)


def get_task(driver, task_id, url):
    return requests.get(f"{url}get-task/{task_id}")


def list_tasks(driver, user_id, url):
    return requests.get(f"{url}list-tasks/{user_id}")


def delete_task(driver, task_id, url):
    return requests.delete(f"{url}delete-task/{task_id}")


def new_task_payload(driver):
    user_id = f"test user_{uuid.uuid4().hex}"
    content = f"test_content_{uuid.uuid4().hex}"
    return {
        "content": content,
        "user_id": user_id,
        "is_done": False
    }
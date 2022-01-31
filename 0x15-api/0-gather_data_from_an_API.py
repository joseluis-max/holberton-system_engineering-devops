#!/usr/bin/python3
"""Script that, using this REST API, for a given employee ID,
returns information about his/her TO DO list progress.
"""
import json
from sys import argv
from urllib import request


if __name__ == "__main__":
    url_user = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    with request.urlopen(url_user) as response:
        html = response.read()
        html = json.loads(html.decode())
        name = html.get("name")
        print(f"Employee {name} is done with ", end="")

    url_task = f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos"
    with request.urlopen(url_task) as response:
        html = response.read()
        html = json.loads(html.decode())
        done = 0
        task = 0
        for t in html:
            if t.get("completed") is True:
                done += 1
            task += 1
        print(f"tasks({done}/{task}):")

        for t in html:
            if t.get("completed") is True:
                print("\t {}".format(t.get("title")))

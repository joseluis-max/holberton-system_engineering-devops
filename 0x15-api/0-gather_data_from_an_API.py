#!/usr/bin/python3
"""Script that, using this REST API, for a given employee ID"""
import json
from sys import argv
from urllib import request

if __name__ == "__main__":
    url_user = "https://jsonplaceholder.typicode.com/users/{}"\
                .format({argv[1]})
    with request.urlopen(url_user) as response:
        html = response.read()
        html = json.loads(html.decode())
        name = html.get("name")
        print("Employee {} is done with ".format(name), end="")

    url_task = "https://jsonplaceholder.typicode.com/users/{}/todos"\
               .format({argv[1]})
    with request.urlopen(url_task) as response:
        html = response.read()
        html = json.loads(html.decode())
        done = 0
        task = 0
        for t in html:
            if t.get("completed") is True:
                done += 1
            task += 1
        print("tasks({}/{}):".format(done, task))

        for t in html:
            if t.get("completed") is True:
                print("\t {}".format(t.get("title")))

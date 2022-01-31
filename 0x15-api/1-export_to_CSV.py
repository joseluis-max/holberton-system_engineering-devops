#!/usr/bin/python3
""" script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import csv
import json
from sys import argv
from urllib import request


if __name__ == "__main__":
    url_user = "https://jsonplaceholder.typicode.com/users/{}"\
                .format(argv[1])
    with request.urlopen(url_user) as response:
        user = json.loads(response.read().decode())

        url_task = "https://jsonplaceholder.typicode.com/users/{}/todos"\
                   .format(argv[1])
        with request.urlopen(url_task) as response:
            tasks = json.loads(response.read().decode())
            with open("{}.csv".format(user.get("id")),
                      mode="w", encoding='utf-8') as csvfile:
                filewriter = csv.writer(csvfile, delimiter=",", quotechar="'")
                for t in tasks:
                    filewriter.writerow([user.get("id"),
                                        user.get("username"),
                                        t.get("completed"),
                                        t.get("title")])

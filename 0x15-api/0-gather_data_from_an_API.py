#!/usr/bin/python3
""" script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
"""
import json
from sys import argv
import urllib.request

from numpy import take

with urllib.request.urlopen(f"https://jsonplaceholde\
                             typicode.com/users/{argv[1]}") as response:
    html = response.read()
    html = json.loads(html.decode())
    name = html.get("name")
    print(f"Employee {name} is done with ", end="")

with urllib.request.urlopen(f"https://jsonplaceholder.\
                             typicode.com/users/{argv[1]}/todos") as response:
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

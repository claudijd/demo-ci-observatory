import requests
import time
import os

from http_observatory_client import HTTPObservatoryClient

os.environ["HTTPOBS_API_URL"] = 'https://http-observatory.security.mozilla.org/api/v1'
client = HTTPObservatoryClient()

acceptable_grades = [
    "A+"
]

hostnames = [
    "blog.rubidus.com",
    "blog.rubidus.com",
    "blog.rubidus.com",
    "blog.rubidus.com",
    "blog.rubidus.com",
    "blog.rubidus.com",
    "blog.rubidus.com",
    "blog.rubidus.com",
    "blog.rubidus.com",
    "blog.rubidus.com",
]

for hostname in hostnames:
    scan_result = client.scan(hostname)
    grade = scan_result['scan']['grade']

    if grade in acceptable_grades:
        print(hostname + " PASSES Observatory Compliance with a grade of " + grade)
    else:
        print(hostname + " FAILS Observatory Compliance with a grade of " + grade)
        exit(1)

exit(0)

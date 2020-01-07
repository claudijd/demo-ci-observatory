import requests
import time
import os
import json

from http_observatory_client import HTTPObservatoryClient

os.environ["HTTPOBS_API_URL"] = 'https://http-observatory.security.mozilla.org/api/v1'
client = HTTPObservatoryClient()

grade_order = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F+", "F", "F-", ]

expectations = [
    {"site": "blog.rubidus.com", "grade": "A+"},
    {"site": "getpocket.com", "grade": "C"}
]

for expectation in expectations:
    grade_expectation = expectation["grade"]
    site = expectation["site"]

    scan_result = client.scan(site)
    grade_actual = scan_result['scan']['grade']

    if grade_expectation == grade_actual:
        print(site + " meets compliance with a grade of " + grade_actual)
    else:
        if grade_order.index(grade_expectation) < grade_order.index(grade_actual):
            print(site + " falls below compliance with a grade of " +
                  grade_actual + " (expected: " + grade_expectation + ")")
        else:
            print(site + " exceeds compliance with a grade of " +
                  grade_actual + " (expected: " + grade_expectation + ")")
        exit(1)

exit(0)

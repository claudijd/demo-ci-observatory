# demo-ci-observatory
This is a demo project to show how to monitor web observatory grades using a CI pipeline

# Setup

1. Change the hosts listed in run.py to the hosts you want to monitor
2. Change the grades that are acceptable to you
3. Enable the project in Travis and setup a Cron job to run at whatever interval you wish
4. Profit or whatever else you need to do with your extra time

# Example Travis Build

You should have something like [this](https://travis-ci.org/claudijd/demo-ci-observatory) when you are done.


# Passing example (w/ zero exit, so it appears as clean run)

```
$ python run.py 
blog.rubidus.com PASSES Observatory Compliance with a grade of A+
blog.rubidus.com PASSES Observatory Compliance with a grade of A+
blog.rubidus.com PASSES Observatory Compliance with a grade of A+
blog.rubidus.com PASSES Observatory Compliance with a grade of A+
blog.rubidus.com PASSES Observatory Compliance with a grade of A+
blog.rubidus.com PASSES Observatory Compliance with a grade of A+
blog.rubidus.com PASSES Observatory Compliance with a grade of A+
blog.rubidus.com PASSES Observatory Compliance with a grade of A+
blog.rubidus.com PASSES Observatory Compliance with a grade of A+
blog.rubidus.com PASSES Observatory Compliance with a grade of A+
```

# Failing example (w/ non-zero exit, so it trips CI failure)

```
$ python run.py 
blog.rubidus.com FAILS Observatory Compliance with a grade of F
```

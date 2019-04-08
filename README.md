# demo-ci-observatory
This is a demo project to show how to monitor web observatory grades using a CI pipeline


# Passing example (w/ zero exit, so it appears as clean run)

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

# Failing example (w/ non-zero exit, so it trips CI failure)

$ python run.py 
blog.rubidus.com FAILS Observatory Compliance with a grade of F
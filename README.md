# Test-Driven Development with Python

Environment
  - Mac OSX
  - Python 3.5.2
  - Django 1.10.5, selenium 3.0.2 (Chrome Web driver 2.27)

Chrome Web driver download page
  - https://sites.google.com/a/chromium.org/chromedriver/downloads

Initial steps

  $ mkdir tdd
  $ cd tdd

  $ virtualenv -p python3 vtdd
  $ source vtdd/bin/activate

  $ mkdir tddjango
  $ cd tddjango

  $ vi functional_tests.py

Directory Structure

  vtdd       : python virtual env
  tddjango   : root of git repository
  superlists : django project root

  tdd ---- vtdd
       +-- tddjango ---- functional_tests.py
                     +-- .git
                     +-- requirement.txt
                     +-- superlists  ---- manage.py
                                      +-- superlists ---- settings.py



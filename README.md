## Setup

Follow this setup only if you want to use a local copy of this application. 

1. `pip install requirements.txt`

**OR**

You can access the app directly to `http://qainterview.pythonanywhere.com` so you can skip the `How to run the application` step(s).


## How to run the application

To start the application, run `python qa_interview.py` and visit `localhost:6464` in your browser.


## What the application does

The application calculates the factorial of a given number. We have exactly one page with:
* one text box
* one submit button
* a page title
* three hyperlinks
* a copyright message


## Hint

The app has been seeded with a variety of bugs:
* a major functional bug
* a data limit bug
* a usability bug
* a typo
* a bug to test if the QA is reading the page content
* a slightly weird wording
* a cross-browser bug

The app also has several workflows which will work well and that the QA being interviewed should check. E.g.: Entering an integer followed by a string followed by an integer (does the form validation clear?).


## Guide

* Check functional correctness
* Keeping notes or screenshots to remember the cases
* Good QA are happy when they are discovering bugs
* Try to reproduce any bug you discover


## Task

* List your test cases (you can divide to positive cases and negative cases)
* Create the automation test using **Selenium Java** **OR** **Katalon**
* Create test documentation based on your test cases


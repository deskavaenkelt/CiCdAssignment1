# CI/CD Assignment 1

# Table of Content

- [Assignment 1](#assignment-1)
    - [What to evaluate](#what-to-evaluate)
    - [Introduction](#introduction)
- [Report](#report)
- [Installation requirements](#installation-requirements)
- [](#)
- [](#)
- [](#)
- [](#)

# Assignment 1

## What to evaluate

After completing the course, the student should be able to:

**Knowledge:**

1. Explain the different parts of Continuous Integration
2. Describe testing and device testing in the area
3. Explain CI/CD

**Skills:**

4. Use processes and methods for applying Continuous Integration

## Introduction

This assignment consists of two parts. With this assignment, you must write a report in which you document how you have
thought through the practical steps.

The goal of the assignment is to start a CI chain with the help of various tools before the deadline 7 May at 23:55

**Requirement:**

Create a python application with either Flask or any code that can be found on Github. This repo should have two
branches; **main**, **dev**

There must be at least two unit tests and one lint installed

A CI tool will be implemented to help us with our pull requests

All development takes place towards the dev industry and must be merged into the main with the help of a manual pull
request. This must be done regularly, ie as soon as something new has been implemented.

- Github
- CircleCI
- Python
- Pytest
- Flake8

**Report requirements:**

- The report must contain the tools you worked with
- How you used them during the task
- If you encountered any obstacles and how you solved them
- Describe how tests work and how you have used them in your task
- Explain what is missing for to achieve CD

# Report

## Installation requirements

```shell
pip install flake8
pip install pytest
```

[Change default test runner in PyCharm to pytest](https://www.jetbrains.com/help/pycharm/pytest.html#enable-pytest)

**flake8 settings in PyCharm**

![](img/1.png)


# Building a REST API with Python 3
Demo code for the course "Building a REST API with Python 3" on [Pluralsight](https://www.pluralsight.com).

There's a commit for each module in the course, as well as a tag:


- [Module 2: Getting Started](https://github.com/codesensei-courses/python_3_rest_api/releases/tag/project-start)
- [Module 3: Creating a datamodel](https://github.com/codesensei-courses/python_3_rest_api/releases/tag/datamodel-start)
- [Module 3 (end): Created database models, added .env](https://github.com/codesensei-courses/python_3_rest_api/releases/tag/datamodel-end)
- [Module 4 (end): Api endpoints and unit tests](https://github.com/codesensei-courses/python_3_rest_api/releases/tag/api-end)
- [Module 5: Exercise: Reading Content from the Filesystem](https://github.com/codesensei-courses/python_3_rest_api/releases/tag/files-start)
- [Module 5: Exercise: Parsing Frontmatter](https://github.com/codesensei-courses/python_3_rest_api/releases/tag/files-parse)
- [Module 5 (end): Fixed the final unit test](https://github.com/codesensei-courses/python_3_rest_api/releases/tag/course-end)


# Setup instructions

## 1. Install poetry

Follow the instructions at https://python-poetry.org/docs/#installation

## 2. Clone this repository

Check out any specific commit you like.

## 3. Install dependencies

Inside the project, run `poetry install`.

## 4. Run the project

The command for this is `poetry run python runserver.py`.

You can now view the project at http://localhost:8000

## 5. Test the project

For this you run `poetry run pytest`.

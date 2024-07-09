# todo-api 

## Requirements

- Python v3.11 or higher
- Poetry v1.8.2 or higher

## Setup

Step 1: Install latest poetry package

```
pip install poetry==1.8.2
```

Step 2: Create vitual environment for Python

```
python -m venv .venv
```

Step 3: Activate venv

```
source .venv/bin/activate
```

Step 4: Install libraries

```
poetry install
```

Step 5: Configure .env

Copy the `.env.example` to `.env`, then replace your config value.

Step 6: Run command:

```
$ docker-compose up -d
```

## DB Migration (only Local env)
Prerequisites

```shell
pip install alembic
pip install pyyaml
pip install pymysql
```

To create migration file

```shell
alembic revision -m “add_abc_table”
```

Run DB migration

```shell
alembic upgrade head
```

## Code Quality Inspection

**Prerequisites**

```shell
pip install pylint
```

**Run command**

```shell
pylint --enable=invalid-name,missing-final-newline --disable=all --rcfile=pylintrc --recursive=y app utils
``` 
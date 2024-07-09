# todo-api 

## Requirements

- Python v3.11
- Poetry v1.8.2 or higher

## Setup

Step 1: Configure .env

Copy the `.env.example` to `.env`, then replace your config value.

Step 2: Run command:

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
# Virtualness

## Description

Backend for the APIs

## Credentials

```
username: admin
password: Test@1234
```

## Installation

### Prerequisites

- Python [3.8]

### Step 1: Create a virtual environment

```
python -m venv myenv
```

### Step 2: Activate the virtual environment

```
source myenv/bin/activate
```

### Step 3: Install dependencies

```
pip install -r requirements.txt
```

## Usage

### Step 1: Run the server

```
python manage.py runserver
```

### Step 2: Access the Swagger endpoint

Open your web browser and go to [http://localhost:8000/swagger].

### Step 3: Test the API

To run the tests and check coverage, follow these steps:

#### Using coverage

```
coverage run manage.py test events/tests/. -v 2
coverage report
```

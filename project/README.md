# Project Title
    This project provides a RESTful API built with Django Rest Framework (DRF) for user registration, login, and profile picture management.

## Installation 
if not installed pyhton in your local system so visit this url <[https://www.python.org/downloads/](https://www.python.org/downloads/) download pyhton.
check version :- python --version

### Installation without docker

1. Clone git repogetory.
    - git clone <https://github.com/yogeshmagarde/python_django.git>

2. Create virtual environment.
    - python3 -m venv <env-name>

3. Activet virtual environment.

    - source <env-name>/bin/activate  # for mac or linux
    - .\<env-name>\Scripts\activate   # for windows

4. Install requirements.txt file.

    - pip install -r requirements.txt
    - pip install --upgrade pip

5. Run project.
    - python manage.py runsever

## Installation with docker 

1. Clone git repogetory.
    - git clone <https://github.com/yogeshmagarde/python_django.git>

2. Install docker in your local sytem.

3. Build the containers.
    - docker-compose up -d --build

4. Check runnig containers.
    - docker ps


**Notes:**

- Replace `<env-name>` with your desired virtual environment name.

- Ensure that Docker is installed and running before executing Docker commands.


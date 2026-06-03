# OnlyFlans Web Application

## Description
This repository contains the source code for a Django Web Application named "OnlyFlans". The application is designed to serve as a basic example of how to set up and run a simple Django project.

## Tech Stack
- **Programming Language**: Python
- **Framework**: Django
- **Database**: SQLite

## Usage
To use this repository, follow these steps:

1. Clone the repository to your local machine.
2. Navigate into the directory where you cloned the repository.
3. Run the following command to start the development server:
   ```bash
   python manage.py runserver
4. Access the application in your web browser by navigating to `http://127.0.0.1:8000/`.

## Directory Structure
- **manage.py**: Entry point for Django management commands.
- **app_onlyflans**: Contains all the code related to the application logic and models.
- **onlyflans**: Contains static files, templates, and other non-model-related Python modules.
- **web_app**: Contains views, URLs, and any other web-specific configurations.

## License
This project is licensed under the [MIT License](LICENSE).

---

**Note:** The repository contains a SQLite database file (`db.sqlite3`) which will be used during development. For production environments, consider using a full-fledged relational database system like PostgreSQL or MySQL.
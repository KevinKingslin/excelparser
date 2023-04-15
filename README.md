### **About**

ExcelParser is a web-application where users can upload a Excel sheet(.xlsx or .xls) and import that excel sheet to the database.
Users can view thier sheets on the website. Other features include sorting, and search of data and pagination of the table.

Tech Stack:
Backend: Django
Frontend: JavaScript and JQuery
Database: SQLite3

### **Files:**
The following is the file structure of the project where I added or modified. 

├── db.sqlite3 - SQLite3 database
├── excelparser - excelparser app
│   ├── admin.py - admin settings for model view
│   ├── apps.py
│   ├── __init__.py
│   ├── models.py - database models
│   ├── static - Folder for all static resources
│   │   └── excelparser
│   │       ├── scripts.js - Mainpage JavaScript file
│   │       └── styles.css - Mainpage CSS
│   ├── templates - Template folder
│   │   └── excelparser
│   │       └── index.html - Mainpage HTML
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── project - Main project
│   ├── asgi.py
│   ├── settings.py - project settings
│   ├── urls.py
│   └── wsgi.py
├── README.md
└── requirements.txt
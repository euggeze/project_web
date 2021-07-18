[![Coverage Status](https://coveralls.io/repos/github/euggeze/project_web/badge.svg?branch=developer)](https://coveralls.io/github/euggeze/project_web?branch=developer)
#About the project
*For read SRS-file [click](./documentation/SRS.md)*

This application is a web application that allows you to work with the data of employees and departments by connecting to a database. The web application can be deployed to **Gunicorn** using the command line. All information about the work will be displayed in the console and saved in the log file.

The web application can:
1. display a list of departments and the average salary (calculated automatically) for these departments 
2. display a list of employees in the departments with an indication of the salary for each employee and a search field to search for employees born on a certain date or in the period between dates
3. change (add/edit/delete) the above data


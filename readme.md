#About the project
*For read SRS-file [click](./documentation/SRS.md)*

Need create a web service (RESTful) for **CRUD operations**. 
One should be able to deploy the web service on **Gunicorn** 
using the command line. All functions/methods on all levels 
should include unit tests. Debug information should be displayed 
at the debugging level in the console and in a separate file. 
Classes and functions/methods must have docstrings comments.

Need create a simple web application for managing departments and employees. 
The web application should use the aforementioned web service for storing 
data and reading them from the database. One should be able to deploy 
the web application on **Gunicorn** using the command line. All public 
functions/methods on all levels should include unit tests. 
Debug information should be displayed at the debugging level 
in the console and in a separate file. Classes and functions/methods 
must have docstrings comments. 

*Finalize the README file which should contain a brief 
description of the project, instructions on how to build a project 
from the command line, how to start it, and at what addresses 
the Web service and the Web application will be available after launch.*

The web application should allow:
1. display a list of departments and the average salary (calculated automatically) for these departments 
2. display a list of employees in the departments with an indication of the salary for each employee and a search field to search for employees born on a certain date or in the period between dates
3. change (add/edit/delete) the above data

**NOTE**: This step may require updating existing or adding new REST endpoints to the aforementioned web service (if they were not taken into account in the previous step). For example, the implementation of employee search by date of birth or the addition of the possibility of calculating the average salary when getting a list of departments.

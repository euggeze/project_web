# Manager for department and employees

## Vision

This application is web-application that helps 
navigate in information about employees and 
departments. 

Application should provide:
* Storing information about employees and
departments in database;
* Display list of employees in department;
* Updating employees data (add,editing,delete);
* Display average cost of employees in a department;
* Display list of departments;
* Updating departments data (add,editing,delete);
* Filtering by date of birthday and period of dates.

## 1. Employees
### 1.1 Display list about employees
The mode is designed to view list of employees in department.
When user selects a department, a list of employees for that 
department appears **(pic 1.1)**.

#### *Main scenario*
* User select item Employees;
* Application open employees list.

![list_employees](./search_period.png)
**pic 1.1 - View the employees list**

The list displays the following columns:
* ID - identification employee number 
* Name - first and last employee name
* Date of birthday - employee's date of birthday
* Salary - employee salary
### 1.2 Search by date and period
For date search user have 2 mods.

#### *Main scenario*
1. Search by birthday:
   
   * User must uncheck **Period** and writes date
   * Click search and list will appear (pic 1.2).
   
![search_date](./search_date.png)
**pic 1.2 - View the employees list by date**

2. Search by date period.

   * User must check **Period** and writes dates. 
   * Then click search and list will appear (pic 1.3).
   
![search_period](./list_employees.png)
**pic 1.3 - View the employees list by period**

For dropping date and period lists user can click button **Drop**.

### 1.3 Add employee

#### *Main scenario*
* User clicks button **Add**;
* Application displays form for adding;
* User enters information and presses **Save**;
* If all information is valid, then information is adding in DB;
* If don't all information is valid, then error message is displaying.

![add_form](./add_employee.png)
**pic 1.4 - View the form for adding**

#### *Cancel operation scenario*
* User clicks button **Add**;
* Application displays form for adding;
* User clicks button **Cancel**;
* If user don't write information, then form will close;
* If user writes information and don't save, 
  then alert message is displaying.

### 1.4 Edit employee

#### *Main scenario*
* User clicks button **Edit**;
* Application displays form for editing;
* User edits information and presses **Save**;
* If all information is valid, then information is adding in DB;
* If don't all information is valid, then error message is displaying.

![edit_form](./edit_employee.png)
**pic 1.5 - View the form for editing**

#### *Cancel operation scenario*
* User clicks button **Edit**;
* Application displays form for editing;
* User clicks button **Cancel**;
* If user don't change information, then form will close;
* If user change information and don't save, 
  then alert message is displaying.
  
### 1.5 Delete employee

#### *Main scenario*
* User clicks button **Delete** in employee's line in lists;
* An alert window will appear and ask if user want to delete;
* User clicks "Yes", then information about employee
will be deleted;
* If user clicks "No", then window just will be closed and
information won't be deleted.
  
#### *Cancel operation scenario*
* User clicks button **Delete** in employee's line in lists;
* An alert window will appear and ask if user want to delete;
* User clicks "Yes", then information about employee
will be deleted;
![delete_form](./delete_employee.png)
**pic 1.6 - View the form for deleting**
  
  
## 2. Departments
The mode is designed to view list of departments.
This mode works just for edit list of departments **(pic 2.1)**.

#### *Main scenario*
* User select item Departments;
* Application open departments list.

![list_departments](./list_departments.png)
**pic 2.1 - View the departments list**

### 2.2 Add department

#### *Main scenario*
* User clicks button **Add**;
* Application displays form for adding;
* User enters information and presses **Save**;
* If all information is valid, then information is adding in DB;
* If don't all information is valid, then error message is displaying.

![add_form](./add_department.png)
**pic 2.2 - View the form for adding**

#### *Cancel operation scenario*
* User clicks button **Add**;
* Application displays form for adding;
* User clicks button **Cancel**;
* If user don't write information, then form will close;
* If user writes information and don't save, 
  then alert message is displaying.

### 2.3 Edit department

#### *Main scenario*
* User clicks button **Edit**;
* Application displays form for editing;
* User edits information and presses **Save**;
* If all information is valid, then information is adding in DB;
* If don't all information is valid, then error message is displaying.

![edit_form](./edit_department.png)
**pic 2.3 - View the form for editing**

#### *Cancel operation scenario*
* User clicks button **Edit**;
* Application displays form for editing;
* User clicks button **Cancel**;
* If user don't change information, then form will close;
* If user change information and don't save, 
  then alert message is displaying.
  
### 2.4 Delete department

#### *Main scenario*
* User clicks button **Delete** in department's line in lists;
* An alert window will appear and ask if user want to delete;
* User clicks "Yes", then information about department
will be deleted;
* If user clicks "No", then window just will be closed and
information won't be deleted.
  
#### *Cancel operation scenario*
* User clicks button **Delete** in department's line in lists;
* An alert window will appear and ask if user want to delete;
* User clicks "Yes", then information about department
will be deleted;
![delete_form](./delete_department.png)
**pic 2.4 - View the form for deleting**

function check_changed_department(data_department, url){
    if (id_name.value != data_department.full_name){
        if (confirm("Are you sure want to exit?")) {
            document.location.href = url
            }
    }
    else{
        document.location.href = url
    }
}

function check_changed_employee(data_employee, url){
    if (id_name.value != data_employee.full_name ||
        id_date.value != data_employee.date_of_birthday ||
        id_salary.value != data_employee.salary ){
        if (confirm("Are you sure want to exit?")) {
            document.location.href = url
            }
    }
    else{
        document.location.href = url
    }
}
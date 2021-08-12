function delete_func(id) {
    if (confirm("Are you sure want to delete this entry?")) {
       {% url 'employees_list' pk=1 %}
    }
    else{
       //undo delete
    }
  }
 function delete_func_dep(id) {
    if (confirm("Are you sure want to delete this entry?")) {
       alert (id)
    }
  }

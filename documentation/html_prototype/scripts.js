function delete_func() {
    if (confirm("Are you sure want to delete this entry?")) {
       document.location.href = 'deleted_empl.html'
    }
    else{
       //undo delete 
    }
  }
 function delete_func_dep() {
    if (confirm("Are you sure want to delete this entry?")) {
       document.location.href = 'deleted_dep.html'
    }
    else{
       //undo delete
    }
  }
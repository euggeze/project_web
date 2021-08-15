function change_checkbox() {
    if (check_period.checked){
        date_by.removeAttribute("readonly");
    }
    else {
        date_by.value = null;
        date_by.setAttribute("readonly","readonly");
    }
  }
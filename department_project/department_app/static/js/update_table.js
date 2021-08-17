$(document).ready(function () {
    $("#id_select").on('change', function (e) {
    var department = id_select.value;
    ajax_update_table(department)
    })
  })

function search_button() {
    var department = id_select.value;
    var start = date_from.value
    var end = date_by.value
    ajax_update_table(department, start, end)
    }

$(document).ready(function () {
    $("#drop_button").on('click', function (e) {
    var department = id_select.value;
    ajax_update_table(department)
    })
  })
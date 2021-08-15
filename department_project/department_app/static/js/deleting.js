function delete_func(id_object) {
    if (confirm("Are you sure want to delete this entry?")) {
       $.ajax({
                type: 'GET',
                url: delete_variable,
                data: {"id": id_object},
                success: function (response) {
                alert ("Entry has been deleted ");
                location.reload(true);
                },
                error: function (response) {
                    alert("Error while deleting data ");
                }
            })
    }
  }
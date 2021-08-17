function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function delete_func(id_object) {
    if (confirm("Are you sure want to delete this entry?")) {
       $.ajax({
                type: 'POST',
                url: delete_variable,
                data: {'csrfmiddlewaretoken' : getCookie('csrftoken'),  "id": id_object},
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
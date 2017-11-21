var $ = require('jquery');

$("#id_providers input:checkbox").change( function() {
    if ($("#id_providers input:checkbox:checked").length > 0){
        $("#delete_button")[0].style.visibility = 'visible';
    } else {
        $("#delete_button")[0].style.visibility = 'hidden';
    }
});

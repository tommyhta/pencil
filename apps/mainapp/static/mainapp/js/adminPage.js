$(document).ready(function(){
    // admin search option
    $('#searchName').keyup(function(){
        $.ajax({
            url: '/adminsearch',
            method: 'post',
            data: $(this).parent().serialize(),
            success: function(serverResponse){
                $('#table').html(serverResponse)
            }
        })
    }) 
});
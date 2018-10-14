$(document).ready(function(){
    
    $('#searchstandard').click(function(){
        $.ajax({
            url:'/store/searchstandard',
            success: function(serverResponse){
                $('#products').html(serverResponse)
            }
        })
    });

    $('#searchall').click(function(){
        $.ajax({
            url:'/store/searchall',
            success: function(serverResponse){
                $('#products').html(serverResponse)
            }
        })
    });
    $('#searchxl').click(function(){
        $.ajax({
            url:'/store/searchxl',
            success: function(serverResponse){
                $('#products').html(serverResponse)
            }
        })
    });
    $('#searchgoldmixed').click(function(){
        $.ajax({
            url:'/store/searchgoldmixed',
            success: function(serverResponse){
                $('#products').html(serverResponse)
            }
        })
    });
    $('#searchaccessories').click(function(){
        $.ajax({
            url:'/store/searchaccessories',
            success: function(serverResponse){
                $('#products').html(serverResponse)
            }
        })
    });
});
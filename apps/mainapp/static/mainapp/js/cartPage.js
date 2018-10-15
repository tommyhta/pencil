$(document).ready(function(){
    $('.quantityInput').each(function(){
        $(this).focusout(function(){
            $.ajax({
                url: '/store/cart/updatecart',
                method: 'post',
                data: $(this).parent().serialize(),
                success: location.reload()
            });
        })
    })
});







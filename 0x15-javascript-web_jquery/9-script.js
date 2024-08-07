#!/usr/bin/node

$.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    method: 'GET',
    success: function (response) {
        $('DIV#hello').html(response.hello);
    }    
});

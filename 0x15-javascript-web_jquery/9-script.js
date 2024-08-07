#!/usr/bin/node

// we have to ensure dom is fully loaded first
$(document).ready(function () {

    $.ajax({
        url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
        method: 'GET',
        success: function (response) {
            $('DIV#hello').html(response.hello);
        }    
    });
});

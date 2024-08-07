#!/usr/bin/node

const h = $('DIV#toggle_header');
h.on('click', function () {
  if ($('header').hasClass('green')) {
    $('header').removeClass('green').addClass('red');
  } else if ($('header').hasClass('red')) {
    $('header').removeClass('red').addClass('green');
  }
});

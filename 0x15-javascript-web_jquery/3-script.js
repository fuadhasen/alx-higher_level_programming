#!/usr/bin/node

const h = $('DIV#red_header');
h.on('click', function () {
  $('header').addClass('red');
});

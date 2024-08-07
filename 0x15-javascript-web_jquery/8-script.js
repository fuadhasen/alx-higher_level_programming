#!/usr/bin/node

$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  method: 'GET',
  success: function (response) {
    const results = response.results;
    results.forEach(films => {
      const item = $(`<li>${films.title}</li>`);
      $('UL#list_movies').append(item);
    });
  }
});

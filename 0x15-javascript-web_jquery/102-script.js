$('document').ready(function () {
  $('INPUT#btn_translate').click(function () {
    const langCode = $('INPUT#language_code').val(); // Get the value of the language code entered
    const url = `https://www.fourtonfish.com/hellosalut/?lang=${langCode}`;
    $.get(url, function (data) {
      $('DIV#hello').text(data.hello); // Display the translation of "Hello"
    });
  });
});

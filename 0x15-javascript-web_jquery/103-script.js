$('document').ready(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/?';

  function translate() {
    const langCode = $('INPUT#language_code').val();
    if (langCode) {
      $.get(url + $.param({ lang: langCode }), function (data) {
        $('DIV#hello').html(data.hello);
      });
    }
  }

  // Trigger translate on button click
  $('INPUT#btn_translate').click(translate);

  // Trigger translate on pressing Enter in the input field
  $('INPUT#language_code').keypress(function (e) {
    if (e.keyCode === 13) { // 13 is the Enter key
      translate();
    }
  });
});

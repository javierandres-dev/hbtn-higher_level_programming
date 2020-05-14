const $ = window.$;
window.onload = function () {
  $('INPUT#btn_translate').click(function () {
    const language = $('INPUT#language_code').val();
    $.get('https://fourtonfish.com/hellosalut/?lang=' + language, function (say, textStatus) {
      $('DIV#hello').text(say.hello);
    });
  });
};

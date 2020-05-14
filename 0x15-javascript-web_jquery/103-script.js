const $ = window.$;
window.onload = function () {
  $('INPUT#btn_translate').click(function () {
    showHello();
  });
  $('INPUT#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      showHello();
    }
  });
};
function showHello () {
  const language = $('INPUT#language_code').val();
  $.get('https://fourtonfish.com/hellosalut/?lang=' + language, function (say, textStatus) {
    $('DIV#hello').text(say.hello);
  });
}

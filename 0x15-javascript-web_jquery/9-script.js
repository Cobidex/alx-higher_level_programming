/* fetches from https://fourtonfish.com/hellosalut/?lang=fr and
 * displays the value of hello from that fetch in the HTML tag DIV#hello
 */
$.ajax({
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  type: 'GET',
  dataType: 'json'
})
  .done(function (json) {
  $('DIV#hello').text(json.hello);
});

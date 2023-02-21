/* adds, removes and clears LI elements
 * from a list when the user clicks
 */
$(function () {
  $('#add_item').click(function () {
    $('<li>Item</li>').appendTo('UL.my_list');
  });
  $('#remove_item').click(function () {
    $('UL.my_list li').remove(':last(<li>Item</li>)');
  });
  $('#clear_list').click(function () {
    $('UL.my_list li').remove();
  });
});

function showModal(message, input) {
  vex.dialog.open({
    message: message,
    input: input,
    buttons: [
      $.extend({}, vex.dialog.buttons.YES, {
        text: '选定离手'
      }), $.extend({}, vex.dialog.buttons.NO, {
        text: '返回重选'
      })
    ],
    callback: function(data) {
      if (data === false) {
        return console.log('Cancelled');
      }
      return console.log('Username', data.greeting, 'Password', data.email);
    }
  });
}

$(document).ready(function () {
  $('#main_content').headsmart();

  $('.boy').click(function(){
    showModal('你的选择是"男生" (Your choice is "boy"):', "<input name=\"greeting\" type=\"text\" placeholder=\"送他句祝福吧 (Send him a greeting please)\" required />\n<input name=\"email\" type=\"email\" placeholder=\"获取抽奖码和结果的Email (Email to get the code)\" required />")
  });

  $('.girl').click(function(){
    showModal('你的选择是"女生" (Your choice is "girl"):', "<input name=\"greeting\" type=\"text\" placeholder=\"送她句祝福吧 (Send her a greeting please)\" required />\n<input name=\"email\" type=\"email\" placeholder=\"获取抽奖码和结果的Email (Email to get the code)\" required />")
  });

})

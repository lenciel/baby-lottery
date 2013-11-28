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
      return console.log('greeting', data.greeting, 'email', data.email);
    }
  });
}

$(document).ready(function () {
  $('#main_content').headsmart();

  $('.boy').click(function(){
    showModal('你的选择是"男孩儿" (Your choice is "a boy")',
      "<style>\n    .vex-custom-field-wrapper {\n        margin: 1em 0;\n    }\n    .vex-custom-field-wrapper > label {\n        display: inline-block;\n        margin-bottom: .2em;\n    }\n</style>\n" +
        "<div class=\"vex-custom-field-wrapper\">\n    <label for=\"date\">送他句祝福吧</label>\n    <div class=\"vex-custom-input-wrapper\">\n        <input name=\"greeting\" type=\"text\" placeholder=\"Send him a greeting please\" required />\n    </div>\n</div>\n" +
        "<div class=\"vex-custom-field-wrapper\">\n    <label for=\"color\">获取抽奖码和结果的Email</label>\n    <div class=\"vex-custom-input-wrapper\">\n        <input name=\"email\" type=\"email\" placeholder=\"Email to get the code and maybe the present!\" required />    </div>\n</div>")
  });

  $('.girl').click(function(){
    showModal('你的选择是"女孩儿" (Your choice is "a girl")',
      "<style>\n    .vex-custom-field-wrapper {\n        margin: 1em 0;\n    }\n    .vex-custom-field-wrapper > label {\n        display: inline-block;\n        margin-bottom: .2em;\n    }\n</style>\n" +
        "<div class=\"vex-custom-field-wrapper\">\n    <label for=\"date\">送她句祝福吧</label>\n    <div class=\"vex-custom-input-wrapper\">\n        <input name=\"greeting\" type=\"text\" placeholder=\"Send her a greeting please\" required />\n    </div>\n</div>\n" +
        "<div class=\"vex-custom-field-wrapper\">\n    <label for=\"color\">获取抽奖码和结果的Email</label>\n    <div class=\"vex-custom-input-wrapper\">\n        <input name=\"email\" type=\"email\" placeholder=\"Email to get the code and maybe the present!\" required />    </div>\n</div>")
  });

})

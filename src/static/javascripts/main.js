function showModal(gender, message, input) {
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
      $.ajax({
        type: "POST",
        url: 'greeting/send',
        data: {
          name: data.name,
          email: data.email,
          message: data.message,
          gender: gender,
        },
        success: function(response) {
          if (response['ret'] == 0) {
            alert("谢谢您的祝福!");
          } else {
            alert('发送失败, 错误原因:"' + response['errmsg'] + '"');
          }
          vex.closeAll();
        },
        error: function() {
          alert('发送失败!');
          vex.closeAll();
        }
      });
    }
  });
}

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie != '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      if (cookie.substring(0, name.length + 1) == (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
      }
    }
  }
  return cookieValue;
}


$(document).ready(function () {
  $('#main_content').headsmart();

  var csrftoken = getCookie('csrftoken');

  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }

  $.ajaxSetup({
    crossDomain: false, // obviates need for sameOrigin test
    beforeSend: function(xhr, settings) {
      if (!csrfSafeMethod(settings.type)) {
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    }
  });

  $('.boy').click(function(){
    showModal(0, '你的选择是"男孩儿" (Your choice is "a boy")',
      "<style>\n    .vex-custom-field-wrapper {\n        margin: 1em 0;\n    }\n    .vex-custom-field-wrapper > label {\n        display: inline-block;\n        margin-bottom: .2em;\n    }\n</style>\n" +
        "\n<div class=\"vex-custom-field-wrapper\">\n    <label for=\"name\">怎么称呼您</label>\n    <div class=\"vex-custom-input-wrapper\">\n        <input name=\"name\" type=\"text\" placeholder=\"Name\" required />\n    </div>\n</div>\n" +
        "<div class=\"vex-custom-field-wrapper\">\n    <label for=\"email\">获取抽奖码和结果的Email</label>\n    <div class=\"vex-custom-input-wrapper\">\n        <input name=\"email\" type=\"email\" placeholder=\"Email to get the code and maybe the present!\" required />    </div>\n</div>" +
        "<div class=\"vex-custom-field-wrapper\">\n    <label for=\"message\">送他句祝福吧</label>\n    <div class=\"vex-custom-input-wrapper\">\n        <input name=\"message\" type=\"text\" placeholder=\"Send him a greeting please\" required />\n    </div>\n</div>")
  });

  $('.girl').click(function(){
    showModal(1, '你的选择是"女孩儿" (Your choice is "a girl")',
      "<style>\n    .vex-custom-field-wrapper {\n        margin: 1em 0;\n    }\n    .vex-custom-field-wrapper > label {\n        display: inline-block;\n        margin-bottom: .2em;\n    }\n</style>\n" +
        "<div class=\"vex-custom-field-wrapper\">\n    <label for=\"name\">怎么称呼您</label>\n    <div class=\"vex-custom-input-wrapper\">\n        <input name=\"name\" type=\"text\" placeholder=\"Name\" required />\n    </div>\n</div>\n" +
        "<div class=\"vex-custom-field-wrapper\">\n    <label for=\"email\">获取抽奖码和结果的Email</label>\n    <div class=\"vex-custom-input-wrapper\">\n        <input name=\"email\" type=\"email\" placeholder=\"to get the code and the present!\" required />    </div>\n</div>" +
        "<div class=\"vex-custom-field-wrapper\">\n    <label for=\"message\">送她句祝福吧</label>\n    <div class=\"vex-custom-input-wrapper\">\n        <input name=\"message\" type=\"text\" placeholder=\"Send her a greeting please\" required />\n    </div>\n</div>")
  });
})

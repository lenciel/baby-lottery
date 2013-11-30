function diffDays() {
  var secondDate = new Date(new Date().getFullYear()+1,0,15);
  var firstDate = new Date();
 return Math.round(Math.abs((firstDate.getTime() - secondDate.getTime())/(1000)));

}

$(document).ready(function () {
   var clock = $('.countdown').FlipClock(diffDays(), {
       clockFace: 'DailyCounter',
       countdown: true
   });

   $("span.days").nextUntil("span.hours").wrapAll("<div class='days-wrap'></div>");
   $("span.hours").nextUntil("span.minutes").wrapAll("<div class='hours-wrap'></div>");
   $("span.minutes").nextUntil("span.seconds").wrapAll("<div class='mins-wrap'></div>");
   $("span.seconds").nextUntil("span.test").wrapAll("<div class='seconds-wrap'></div>");
});



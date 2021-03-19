//Script Clock:
const deg = 6; //360deg / 60(min||sec) => 6
const hr = document.querySelector("#hr");
const mn = document.querySelector("#mn");
const sc = document.querySelector("#sc");
/*var digits = {};

var positions = ['h1', 'h2', ':', 'm1', 'm2', ':', 's1', 's2' ];

var digitHolder = clock.find('.digits');

$.each(positions, function(){
*/
setInterval(() => {
let day = new Date();
let hh = day.getHours() * 30; //360deg / 12 hour => 30
let mm = day.getMinutes() * deg;
let ss = day.getSeconds() * deg;
/*var digits = {};

var positions = ['h1', 'h2', ':', 'm1', 'm2', ':', 's1', 's2' ];

var digitHolder = clock.find('.digits');

$.each(positions, function(){
*/
hr.style.transform = `rotateZ(${hh + mm / 12}deg)`;
mn.style.transform = `rotateZ(${mm}deg)`;
sc.style.transform = `rotateZ(${ss}deg)`;
});
//End Script Clock:


//Script of jalali-date:
var sundte = new Date();
var yeardte = sundte.getFullYear();
var monthdte = sundte.getMonth();
var dtedte = sundte.getDate();
var daydte = sundte.getDay();
var sunyear;
switch (daydte) {
case 0:
var today = "يکشنبه";
break;
case 1:
var today = "دوشنبه";
break;
case 2:
var today = "سه شنبه";
break;
case 3:
var today = "چهارشنبه";
break;
case 4:
var today = "پنجشنبه";
break;
case 5:
var today = "جمعه";
break;
case 6:
var today = "شنبه";
break;
}
switch (monthdte) {
case 0:
sunyear = yeardte - 622;
if (dtedte <= 20) {
  var sunmonth = "دي";
  var daysun = dtedte + 10;
} else {
  var sunmonth = "بهمن";
  var daysun = dtedte - 20;
}
break;
case 1:
sunyear = yeardte - 622;
if (dtedte <= 19) {
  var sunmonth = "بهمن";
  var daysun = dtedte + 11;
} else {
  var sunmonth = "اسفند";
  var daysun = dtedte - 19;
}
break;
case 2:
{
  if ((yeardte - 621) % 4 == 0) var i = 10;
  else var i = 9;
  if (dtedte <= 20) {
    sunyear = yeardte - 622;
    var sunmonth = "اسفند";
    var daysun = dtedte + i;
  } else {
    sunyear = yeardte - 621;
    var sunmonth = "فروردين";
    var daysun = dtedte - 20;
  }
}
break;
case 3:
sunyear = yeardte - 621;
if (dtedte <= 20) {
  var sunmonth = "فروردين";
  var daysun = dtedte + 11;
} else {
  var sunmonth = "ارديبهشت";
  var daysun = dtedte - 20;
}
break;
case 4:
sunyear = yeardte - 621;
if (dtedte <= 21) {
  var sunmonth = "ارديبهشت";
  var daysun = dtedte + 10;
} else {
  var sunmonth = "خرداد";
  var daysun = dtedte - 21;
}

break;
case 5:
sunyear = yeardte - 621;
if (dtedte <= 21) {
  var sunmonth = "خرداد";
  var daysun = dtedte + 10;
} else {
  var sunmonth = "تير";
  var daysun = dtedte - 21;
}
break;
case 6:
sunyear = yeardte - 621;
if (dtedte <= 22) {
  var sunmonth = "تير";
  var daysun = dtedte + 9;
} else {
  var sunmonth = "مرداد";
  var daysun = dtedte - 22;
}
break;
case 7:
sunyear = yeardte - 621;
if (dtedte <= 22) {
  var sunmonth = "مرداد";
  var daysun = dtedte + 9;
} else {
  var sunmonth = "شهريور";
  var daysun = dtedte - 22;
}
break;
case 8:
sunyear = yeardte - 621;
if (dtedte <= 22) {
  var sunmonth = "شهريور";
  var daysun = dtedte + 9;
} else {
  var sunmonth = "مهر";
  var daysun = dtedte + 22;
}
break;
case 9:
sunyear = yeardte - 621;
if (dtedte <= 22) {
  var sunmonth = "مهر";
  var daysun = dtedte + 8;
} else {
  var sunmonth = "آبان";
  var daysun = dtedte - 22;
}
break;
case 10:
sunyear = yeardte - 621;
if (dtedte <= 21) {
  var sunmonth = "آبان";
  var daysun = dtedte + 9;
} else {
  var sunmonth = "آذر";
  var daysun = dtedte - 21;
}

break;
case 11:
sunyear = yeardte - 621;
if (dtedte <= 19) {
  var sunmonth = "آذر";
  var daysun = dtedte + 9;
} else {
  var sunmonth = "دي";
  var daysun = dtedte + 21;
}
break;
}
document.getElementById("demo").innerHTML =
today +
"&nbsp;" +
[daysun + 1] +
"&nbsp;" +
sunmonth +
"&nbsp;" +
sunyear



        // Online Clock2:
// var canvas = document.getElementById("canvas");
// var ctx = canvas.getContext("2d");
// var radius = canvas.height / 2;
// ctx.translate(radius, radius);
// radius = radius * 0.90
// setInterval(drawClock, 1000);
//
// function drawClock() {
//   drawFace(ctx, radius);
//   drawNumbers(ctx, radius);
//   drawTime(ctx, radius);
// }
//
// function drawFace(ctx, radius) {
//   var grad;
//   ctx.beginPath();
//   ctx.arc(0, 0, radius, 0, 2*Math.PI);
//   ctx.fillStyle = 'white';
//   ctx.fill();
//   grad = ctx.createRadialGradient(0,0,radius*0.95, 0,0,radius*1.05);
//   grad.addColorStop(0, '#333');
//   grad.addColorStop(0.5, 'white');
//   grad.addColorStop(1, '#333');
//   ctx.strokeStyle = grad;
//   ctx.lineWidth = radius*0.1;
//   ctx.stroke();
//   ctx.beginPath();
//   ctx.arc(0, 0, radius*0.1, 0, 2*Math.PI);
//   ctx.fillStyle = '#333';
//   ctx.fill();
// }
//
// function drawNumbers(ctx, radius) {
//   var ang;
//   var num;
//   ctx.font = radius*0.15 + "px arial";
//   ctx.textBaseline="middle";
//   ctx.textAlign="center";
//   for(num = 1; num < 13; num++){
//     ang = num * Math.PI / 6;
//     ctx.rotate(ang);
//     ctx.translate(0, -radius*0.85);
//     ctx.rotate(-ang);
//     ctx.fillText(num.toString(), 0, 0);
//     ctx.rotate(ang);
//     ctx.translate(0, radius*0.85);
//     ctx.rotate(-ang);
//   }
// }
//
// function drawTime(ctx, radius){
//     var now = new Date();
//     var hour = now.getHours();
//     var minute = now.getMinutes();
//     var second = now.getSeconds();
//     //hour
//     hour=hour%12;
//     hour=(hour*Math.PI/6)+
//     (minute*Math.PI/(6*60))+
//     (second*Math.PI/(360*60));
//     drawHand(ctx, hour, radius*0.5, radius*0.07);
//     //minute
//     minute=(minute*Math.PI/30)+(second*Math.PI/(30*60));
//     drawHand(ctx, minute, radius*0.8, radius*0.07);
//     // second
//     second=(second*Math.PI/30);
//     drawHand(ctx, second, radius*0.9, radius*0.02);
// }
//
// function drawHand(ctx, pos, length, width) {
//     ctx.beginPath();
//     ctx.lineWidth = width;
//     ctx.lineCap = "round";
//     ctx.moveTo(0,0);
//     ctx.rotate(pos);
//     ctx.lineTo(0, -length);
//     ctx.stroke();
//     ctx.rotate(-pos);
// }
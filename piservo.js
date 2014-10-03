var pan = 0;
var tilt = 0;
var midPan = 336; //Middle value for pan
var midTilt = 320;//Middle value for tilt
var leftPan = 512;
var downTilt = 440;
var rightPan = 160;
var upTilt = 102;
var led_stat = false;
var ajax_pipan;
var step = 10
var speed = 1 
 
if(window.XMLHttpRequest) {
  ajax_pipan = new XMLHttpRequest();
  //The XMLHttpRequest object is used to exchange data with a server.
}
else {
  ajax_pipan = new ActiveXObject("Microsoft.XMLHTTP");
  //For IE
}
 
function pipan_servo () {
  ajax_pipan.open("GET","piservo.php?pan=" + pan + "&tilt=" + tilt, true);
  //open(method,url,async)
  ajax_pipan.send();
}
 
function servo_left () {
  pan = document.getElementById('stepValue').innerHTML;
  tilt = 0;
  pipan_servo();
}
 
function servo_right () {
  pan = -document.getElementById('stepValue').innerHTML;
  tilt = 0;
  pipan_servo();
}
 
function servo_up () {
  tilt = -document.getElementById('stepValue').innerHTML;
  pan = 0;
  pipan_servo();
}
 
function servo_down () {
  tilt = document.getElementById('stepValue').innerHTML;
  pan = 0;
  pipan_servo();
}
 
/*function led_switch () {
 
  if(!led_stat) {
    led_stat = true;
    ajax_pipan.open("GET","piservo.php?red=" + document.getElementById("pilight_r").value + "&green=" + document.getElementById("pilight_g").value + "&blue=" + document.getElementById("pilight_b").value, true);
    ajax_pipan.send();
  }
  else {
    led_stat = false;
    ajax_pipan.open("GET","piservo.php?red=0&green=0&blue=0", true);
    ajax_pipan.send();
  }
 
} */

function servo_pan () {
  //tilt = 0;
  pan = 0;
  tilt = document.getElementById('speedValue').innerHTML;
  ajax_pipan.open("GET","piservo.php?pan=" + "panning"  + "&tilt=" + tilt, true);
  ajax_pipan.send();
}

function servo_center () {

  ajax_pipan.open("GET","piservo.php?pan=" + "centering" + "&tilt=" + "centering", true);
  //open(method,url,async)
  ajax_pipan.send();

}

function servo_tilt () {
  pan = document.getElementById('speedValue').innerHTML;
  //pan = 0;
  ajax_pipan.open("GET","piservo.php?pan=" + pan + "&tilt=" + "tilting", true);
  ajax_pipan.send();

}

function keyDown (e) {
 
  if(e.keyCode == 97) servo_left().innerHTML;
  else if(e.keyCode == 119) servo_up();
  else if(e.keyCode == 100) servo_right();
  else if(e.keyCode == 115) servo_down();
 
  //else if(e.keyCode == 102) led_switch();
 
}


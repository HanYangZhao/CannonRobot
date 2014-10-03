
var ajax_pimotor;

var direction = "stop"; 
 
if(window.XMLHttpRequest) {
  ajax_pimotor = new XMLHttpRequest();
  //The XMLHttpRequest object is used to exchange data with a server.
}
else {
  ajax_pimotor = new ActiveXObject("Microsoft.XMLHTTP");
  //For IE
}
 
function pi_movement() {
  ajax_pimotor.open("GET","pimotor.php?movement=" + direction, true);
  //open(method,url,async)
  ajax_pimotor.send();
}
 
function movement_left() {
  direction = "left";
  pi_movement();
}
 
function movement_right() {
  direction = "right";
  pi_movement();
}
 
function movement_forward() {
  
  direction = "forward";
  pi_movement();
}
 
function movement_backward() {
  direction = "backwards";
  pi_movement();
}
 
function movement_stop() {
  direction = "stop";
  pi_movement();
}

function movement_fire(){
  direction = "fire";
  pi_movment();
}

function movement_reload(){
  direction = "reload";
  pi_movment();
}
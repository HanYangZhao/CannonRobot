<?php
 
  //
  // settings
  //
  $min_pan = 160; //Right
  $max_pan = 512; //Left
  $min_tilt = 407; //down
  $max_tilt = 102; //up
 
 
  //
  // code
  //
  if(isset($_GET["pan"])) {
    if(is_numeric($_GET["pan"])) {
      if(is_numeric($_GET["tilt"])) {
        $pan = ($_GET["pan"]);
        $tilt = ($_GET["tilt"]);
        $pipe = fopen("FIFO_piservo","w");
        fwrite($pipe, "servo $pan $tilt ");
        fclose($pipe);
      }
    }
  }
 
  if(isset($_GET["pan"])) {
    if(!(is_numeric($_GET["pan"]))) {
      if(is_numeric($_GET["tilt"])) {
        $pan = 0;
 	$tilt = $_GET["tilt"];
        $pipe = fopen("FIFO_piservo","w");
        fwrite($pipe, "panning $pan $tilt ");
        fclose($pipe);
      }	
    }
  } 


  if(isset($_GET["pan"])) {
    if(!(is_numeric($_GET["pan"]))) {
      if(!(is_numeric($_GET["tilt"]))) {
        $pan = 0;
        $tilt = 0;
        $pipe = fopen("FIFO_piservo","w");
        fwrite($pipe, "centering $pan $tilt ");
        fclose($pipe);
      }
    }
  }

  if(isset($_GET["pan"])) { 
    if(is_numeric($_GET["pan"])) {
      if(!(is_numeric($_GET["tilt"]))) {
        $tilt = 0;
	$pan = $_GET["pan"];
	$pipe = fopen("FIFO_piservo","w");
	fwrite($pipe, "tilting $pan $tilt ");
	fclose($pipe);
     }
   }
 }
 
//  if(isset($_GET["red"])) {
//    if(is_numeric($_GET["red"])) {
//      if(is_numeric($_GET["green"])) {
//        if(is_numeric($_GET["blue"])) {
//          $pipe = fopen("FIFO_piservo","w");
//          fwrite($pipe, "led " . $_GET["red"] . " " . $_GET["green"] . " " . $_GET["blue"] . " ");
//          fclose($pipe);
//        }
//      }
//    }
//  }
 
?>

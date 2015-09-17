<?php

if(isset($_GET["movement"])) {
    	$movement = ($_GET["movement"]);
    	$pipe = fopen("FIFO_pimotor","w");
    	fwrite($pipe,"$movement");
    	fclose($pipe);
}
?>

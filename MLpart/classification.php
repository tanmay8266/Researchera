<?php 
$st = $_REQUEST['string'];
$inp = $_REQUEST['input'];
$pyscript = 'C:\\xampp\\htdocs\\BEPROJ\\MLpart\\test.py';
$python = 'C:\\Users\\ranet\\AppData\\Local\\Programs\\Python\\Python37-32\\python.exe';
$cmd = "$python $pyscript $st $inp";
exec("$cmd",$output);
print_r($output);


?>
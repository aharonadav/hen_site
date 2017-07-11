<?php
$command = escapeshellcmd('python compare.py');
echo "<pre>";
$output = shell_exec($command);
echo $output;
echo "</pre>";
?>

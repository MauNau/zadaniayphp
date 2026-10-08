<?php
session_start();
$_SESSION["name"] = "Иван";
echo "Имя сохранено в сессии.
";
echo '<a href="profile.php">Перейти на вторую страницу</a>';
?>
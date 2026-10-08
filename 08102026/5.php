<?php
session_start();
if (isset($_POST["name"])) {
    $name = trim($_POST["name"]);
    if ($name != "") {
        $_SESSION["name"] = $name;
        echo "Привет, " . $_SESSION["name"] . "!";
    } else {
        echo "Введите имя.";
    }
}
?>

<form method="POST">
    <input type="text" name="name" placeholder="Введите имя">
    <button type="submit">Сохранить</button>
</form>
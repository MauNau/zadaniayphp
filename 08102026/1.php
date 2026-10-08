<?php
if (isset($_COOKIE["name"])) {
    echo "Имя: " . $_COOKIE["name"];
} else {
    setcookie("name", "Иван", time() + 86400);
    echo "Имя не сохранено";
}
?>
<?php
setcookie("theme", "dark", time() + 86400);
if (isset($_COOKIE["theme"])) {
    echo "Текущая тема: " . $_COOKIE["theme"];
} else {
    echo "Тема ещё не сохранена";
}
?>
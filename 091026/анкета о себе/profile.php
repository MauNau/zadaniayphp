<?php
session_start();

if (empty($_SESSION["authorized"])) {
    header("Location: login.php");
    exit;
}

if (isset($_GET["logout"])) {
    $_SESSION = [];
    session_destroy();
    header("Location: login.php");
    exit;
}

function cookieValue($name) {
    return htmlspecialchars($_COOKIE[$name] ?? "Не указано", ENT_QUOTES);
}
?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Анкета о себе</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
<main class="container">
    <div class="brand">АНКЕТА <span>О СЕБЕ</span></div>
    <section class="card profile-card">
        <p class="eyebrow">ЛИЧНЫЙ КАБИНЕТ</p>
        <h1>Моя анкета</h1>
        <p class="subtitle">Ваша информация, сохранённая при регистрации</p>

        <div class="profile-head">
            <div class="avatar"><?= mb_strtoupper(mb_substr($_COOKIE["user_name"] ?? "?", 0, 1)) ?></div>
            <div>
                <h2><?= cookieValue("user_name") ?></h2>
                <p class="muted">@<?= htmlspecialchars($_SESSION["login"], ENT_QUOTES) ?></p>
            </div>
        </div>

        <div class="profile-section">
            <h3>Личные данные</h3>
            <div class="data-row"><span>Имя</span><strong><?= cookieValue("user_name") ?></strong></div>
            <div class="data-row"><span>Возраст</span><strong><?= cookieValue("user_age") ?> лет</strong></div>
            <div class="data-row"><span>Пол</span><strong><?= cookieValue("user_gender") ?></strong></div>
        </div>

        <div class="profile-section">
            <h3>Предпочтения</h3>
            <div class="data-row"><span>Питание</span><strong><?= cookieValue("user_food") ?></strong></div>
            <div class="data-row"><span>Стиль одежды</span><strong><?= cookieValue("user_clothing") ?></strong></div>
            <div class="data-row"><span>Любимая музыка</span><strong><?= cookieValue("user_music") ?></strong></div>
            <div class="data-row"><span>Хобби</span><strong><?= cookieValue("user_hobby") ?></strong></div>
        </div>

        <a class="button-link secondary-button" href="profile.php?logout=1">Выйти из аккаунта</a>
    </section>
</main>
</body>
</html>

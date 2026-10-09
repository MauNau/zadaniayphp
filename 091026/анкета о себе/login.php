<?php
session_start();

if (!empty($_SESSION["authorized"])) {
    header("Location: profile.php");
    exit;
}

$message = "";
$success = false;

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $login = trim($_POST["login"] ?? "");
    $password = trim($_POST["password"] ?? "");

    if (isset($_COOKIE["user_login"], $_COOKIE["user_password"]) &&
        $login === $_COOKIE["user_login"] &&
        $password === $_COOKIE["user_password"]) {
        session_regenerate_id(true);
        $_SESSION["authorized"] = true;
        $_SESSION["login"] = $login;
        $success = true;
        $message = "Вы успешно вошли в аккаунт.";
    } else {
        $message = "Неверный логин или пароль.";
    }
}
?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Вход — Анкета о себе</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
<main class="container">
    <div class="brand">АНКЕТА <span>О СЕБЕ</span></div>
    <section class="card login-card">
        <p class="eyebrow">РАДЫ ВИДЕТЬ ВАС СНОВА</p>
        <h1>Вход в аккаунт</h1>
        <p class="subtitle">Введите данные, указанные при регистрации</p>

        <?php if ($message !== ""): ?>
            <div class="message <?= $success ? 'success' : 'error' ?>">
                <?= htmlspecialchars($message, ENT_QUOTES) ?>
                <?php if ($success): ?><p><a href="profile.php">Перейти в личный кабинет →</a></p><?php endif; ?>
            </div>
        <?php endif?>

        <form method="post" action="login.php">
            <label for="login">Логин</label>
            <input id="login" name="login" type="text" autocomplete="username" required>
            <label for="password">Пароль</label>
            <input id="password" name="password" type="password" autocomplete="current-password" required>
            <button type="submit">Войти</button>
        </form>
        <p class="bottom-text">Ещё нет аккаунта? <a href="register.php">Зарегистрироваться</a></p>
    </section>
</main>
</body>
</html>

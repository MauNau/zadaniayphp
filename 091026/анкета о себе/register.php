<?php
$message = "";
$success = false;

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $login = trim($_POST["login"] ?? "");
    $password = trim($_POST["password"] ?? "");
    $name = trim($_POST["name"] ?? "");
    $age = trim($_POST["age"] ?? "");
    $gender = trim($_POST["gender"] ?? "");
    $food = trim($_POST["food"] ?? "");
    $clothing = trim($_POST["clothing"] ?? "");
    $music = trim($_POST["music"] ?? "");
    $hobby = trim($_POST["hobby"] ?? "");

    if ($login === "" || $password === "" || $name === "" || $age === "" ||
        $gender === "" || $food === "" || $clothing === "" || $music === "" || $hobby === "") {
        $message = "Заполните все поля анкеты.";
    } elseif (!filter_var($age, FILTER_VALIDATE_INT) || $age < 1 || $age > 120) {
        $message = "Введите корректный возраст от 1 до 120 лет.";
    } else {
        $days = time() + 7 * 24 * 60 * 60;
        $options = ["expires" => $days, "path" => "/", "samesite" => "Lax"];

        setcookie("user_login", $login, $options);
        setcookie("user_password", $password, $options);
        setcookie("user_name", $name, $options);
        setcookie("user_age", $age, $options);
        setcookie("user_gender", $gender, $options);
        setcookie("user_food", $food, $options);
        setcookie("user_clothing", $clothing, $options);
        setcookie("user_music", $music, $options);
        setcookie("user_hobby", $hobby, $options);

        $success = true;
        $message = "Регистрация прошла успешно! Теперь войдите в аккаунт.";
    }
}
?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Регистрация — Анкета о себе</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
<main class="container">
    <div class="brand">АНКЕТА <span>О СЕБЕ</span></div>
    <section class="card">
        <p class="eyebrow">СОЗДАЙТЕ ПРОФИЛЬ</p>
        <h1>Регистрация</h1>
        <p class="subtitle">Расскажите немного о себе</p>

        <?php if ($message !== ""): ?>
            <div class="message <?= $success ? 'success' : 'error' ?>">
                <?= htmlspecialchars($message, ENT_QUOTES) ?>
                <?php if ($success): ?><p><a href="login.php">Перейти ко входу →</a></p><?php endif; ?>
            </div>
        <?php endif; ?>

        <form method="post" action="register.php">
            <div class="section-title">Данные для входа</div>
            <label for="login">Логин</label>
            <input id="login" name="login" type="text" autocomplete="username" required>
            <label for="password">Пароль</label>
            <input id="password" name="password" type="password" autocomplete="new-password" required>

            <div class="section-title">Личная информация</div>
            <label for="name">Ваше имя</label>
            <input id="name" name="name" type="text" required>
            <label for="age">Возраст</label>
            <input id="age" name="age" type="number" min="1" max="120" required>

            <label for="gender">Пол</label>
            <select id="gender" name="gender" required>
                <option value="">Выберите вариант</option>
                <option>Женский</option>
                <option>Мужской</option>
                <option>Не хочу указывать</option>
            </select>

            <label for="food">Предпочтения в еде</label>
            <select id="food" name="food" required>
                <option value="">Выберите вариант</option>
                <option>Всеядное питание</option>
                <option>Вегетарианское питание</option>
                <option>Веганское питание</option>
                <option>Люблю сладкое</option>
                <option>Другое</option>
            </select>

            <label for="clothing">Стиль одежды</label>
            <select id="clothing" name="clothing" required>
                <option value="">Выберите вариант</option>
                <option>Повседневный</option>
                <option>Классический</option>
                <option>Спортивный</option>
                <option>Уличный</option>
                <option>Романтичный</option>
                <option>Альтернативный</option>
            </select>

            <label for="music">Любимая музыка</label>
            <input id="music" name="music" type="text" placeholder="Например, рок, поп, джаз" required>
            <label for="hobby">Хобби и увлечения</label>
            <textarea id="hobby" name="hobby" rows="3" placeholder="Что вам нравится делать?" required></textarea>

            <button type="submit">Зарегистрироваться</button>
        </form>
        <p class="bottom-text">Уже есть аккаунт? <a href="login.php">Войти</a></p>
    </section>
</main>
</body>
</html>

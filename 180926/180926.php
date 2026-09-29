<?php

$users = [
    [
        "user_name" => "Алексей",
        "user_age" => 21,
        "user_login" => "alex",
        "user_password" => "Alex@123"
    ],
    [
        "user_name" => "Мария",
        "user_age" => 19,
        "user_login" => "maria",
        "user_password" => "Maria#456"
    ],
    [
        "user_name" => "Иван",
        "user_age" => 25,
        "user_login" => "ivan",
        "user_password" => "Ivan_789"
    ]
];


$user_login = "alex";
$user_password = "Alex@123";

$user_found = false;


foreach ($users as $user) {

    if ($user["user_login"] == $user_login) {

        $user_found = true;


        if ($user["user_password"] != $user_password) {

            echo "Некорректный пароль.";

        } else {

            echo "Имя пользователя: " . $user["user_name"] . "";
            echo "Возраст: " . $user["user_age"] . "";


            $passwordLength = strlen($user_password);

            $hasNumber = preg_match("/[0-9]/", $user_password);
            $hasSpecial = preg_match("/[@&%#\[\]\(\)_!]/", $user_password);

            if ($passwordLength < 8 || !$hasNumber || !$hasSpecial) {
                echo "Внимание! Пароль является слабым.";
            } else {
                echo "Пароль достаточно надёжный.";
            }
        }

        break;
    }
}


if ($user_found == false) {
    echo "Пользователь с таким логином не существует.";
}

?>
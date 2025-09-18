<?php

require_once 'Car.php';
require_once 'Database.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $model = $_POST['model'];
    $year = $_POST['year'];
    $color = $_POST['color'];
    
    $database = new Database();

    $sql = 'INSERT INTO cars (model, year, color) VALUES (?, ?, ?)';
    $stmt = $database->getPdo()->prepare($sql);
    
    if ($stmt->execute([$model, $year, $color])) {
        echo 'Car added successfully';
    } else {
        echo 'Error adding car';
    }
    header('Location: index.php');
    exit;
}

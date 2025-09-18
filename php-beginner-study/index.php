<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP</title>
</head>
<body>

    <form action="index.form.php" method="post">
        <label for="model">Model:</label>
        <input type="text" id="model" name="model">

        <label for="year">Year:</label>
        <input type="number" id="year" name="year" required>

        <label for="color">Color:</label>
        <input type="text" id="color" name="color" required>

        <input type="submit" value="Submit">
    </form>

    <?php
        require_once 'Database.php';

        $database = new Database();
        $pdo = $database->getPdo();
        
        $sql = 'SELECT * FROM cars';
        
        $stmt = $pdo->query($sql);
        
        $cars = $stmt->fetchAll();
        foreach ($cars as $car) {
            echo $car['model'] . ' ' . $car['year'] . ' ' . $car['color'] . '<br>';
        }
        // $name = 'John';
        // echo 'My name is ' . $name;
        // require_once 'Car.php';
        // $car = new Car('Honda', 2023, 'red');
        // echo $car->getCarInfo(); // Honda 2023 red
    ?>
    
</body>
</html>
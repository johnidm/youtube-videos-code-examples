<?php

class Car {
    private string $model = 'Unknown';
    private int $year = 0000;

    private string $color = 'Unknown';

    private $allowedColors = [
        'red',
        'blue',
        'green',
    ];

    public function __construct(string $model, int $year, string $color)
    {
        $this->model = $model;
        $this->year = $year;

        if (in_array($color, $this->allowedColors)) {
            $this->color = $color;
        }
    }

    public function getModel(): string
    {
        return $this->model;
    }

    public function getYear(): int
    {
        return $this->year;
    }

    public function getColor(): string
    {
        return $this->color;
    }

    public function getCarInfo(): string 
    {
        return $this->model . ' ' . $this->year . ' ' . $this->color;
    } 
}

// $car = new Car('Honda', 2023);
// echo $car->getModel(); // Honda
// echo $car->getYear(); // 2023
// echo $car->getCarInfo(); // Honda 2023

<?php

class Database {
    private string $dbFile = 'database.sqlite'; // SQLite database file
    private $pdo;

    public function __construct()
    {
        $this->connect();
        $this->createTables();
    }

    private function connect(): void
    {
        try {
            // SQLite connection string
            $dsn = 'sqlite:' . $this->dbFile;
            
            // Create PDO instance
            $this->pdo = new PDO($dsn);
            
            // Set error mode to exception
            $this->pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            $this->pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
            
        } catch(PDOException $e) {
            echo "Connection failed: " . $e->getMessage();
        }
    }

    private function createTables(): void
    {
        $sql = 'CREATE TABLE IF NOT EXISTS cars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            model TEXT,
            year INTEGER,
            color TEXT
        )';

        $this->pdo->exec($sql);
    }
    
    // Method to get the PDO instance
    public function getPdo() {
        return $this->pdo;
    }


}
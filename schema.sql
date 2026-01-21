-- creamos la base de datos.
create database console;
-- usamos la base de datos.
use console;

-- ─────────────── Tabla de usuarios ───────────────
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- ─────────────── Tabla de registro de alimentos ───────────────
CREATE TABLE IF NOT EXISTS food_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    food_name VARCHAR(100) NOT NULL,
    calories INT NOT NULL,
    log_date DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

SELECT * FROM users;
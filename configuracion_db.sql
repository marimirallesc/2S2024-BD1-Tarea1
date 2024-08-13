-- Crear la base de datos si no existe
CREATE DATABASE IF NOT EXISTS EmpleadosDB;
USE EmpleadosDB;

-- Crear la tabla Empleado si no existe
CREATE TABLE IF NOT EXISTS Empleado (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Salario DECIMAL(18, 2) NOT NULL
);

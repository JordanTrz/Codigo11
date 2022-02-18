CREATE DATABASE IF NOT EXISTS company;

USE company;

CREATE TABLE employee(
  id INT(11) NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) DEFAULT NULL,
  salary INT(11) DEFAULT NULL,
  PRIMARY KEY(id)
);

INSERT INTO employee(name,salary) VALUES
  ('Jordan TA', 4000),
  ('Lucerito YT', 3000),
  ('Monica RS', 3500);

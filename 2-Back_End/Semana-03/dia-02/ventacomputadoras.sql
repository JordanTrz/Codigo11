CREATE TABLE if not exists `cliente` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) DEFAULT NULL,
  `pais` varchar(200) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `state` char(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1001 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

create table if not exists usuario(
  id int(11) not null AUTO_INCREMENT,
  cliente_id int(11) UNIQUE,
  nombre VARCHAR(255) not null,
  clave varchar(255) not null,
  PRIMARY key(id),
  FOREIGN KEY(cliente_id) REFERENCES cliente(id)
) ENGINE=InnoDB;

CREATE TABLE if not exists `computadora` (
  `id` int NOT NULL AUTO_INCREMENT,
  `marca` varchar(100) DEFAULT NULL,
  `precio` double DEFAULT NULL,
  `modelo` varchar(100) DEFAULT NULL,
  `ram` varchar(20) DEFAULT NULL,
  `arquitectura` varchar(100) DEFAULT NULL,
  `monitor` varchar(100) DEFAULT NULL,
  `sistema_operativo` varchar(100) DEFAULT NULL,
  `procesador` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

create table if not exists venta(
  id int(11) not null AUTO_INCREMENT,
  cliente_id int(11) not null,
  fecha date,
  PRIMARY KEY(id),
  FOREIGN KEY(cliente_id) REFERENCES cliente(id)
) ENGINE=InnoDB;

create table if not exists venta_detalle(
  id int(11) not null AUTO_INCREMENT,
  computadora_id int(11) not null,
  cantidad int(5) not null,
  precio DOUBLE,
  venta_id int(11) not null,
  PRIMARY KEY(id),
  FOREIGN KEY(computadora_id) REFERENCES computadora(id),
  FOREIGN KEY(venta_id) REFERENCES venta(id)
) ENGINE=InnoDB;


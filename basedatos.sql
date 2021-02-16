CREATE DATABASE IF NOT EXISTS master_python;

USE master_python;

CREATE TABLE usuarios(
    id int(25) auto_increment not null,
    nombre      varchar(100),
    apellido    varchar(255),
    email       varchar(255) not null,
    password    varchar(255) not null,
    fecha       date not null,
    CONSTRAINT pk_usuarios PRIMARY KEY(id),
    CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InnoDb;

CREATE TABLE notas(
    id              int(25) auto_increment not null,
    id_user         int(25) not null,
    titulo          varchar(255) not null,
    descripcion     MEDIUMTEXT,
    fecha           date not null,
    CONSTRAINT pk_notas PRIMARY KEY(id),
    CONSTRAINT fk_nota_usuario FOREIGN KEY(id_user) REFERENCES usuarios(id)
)ENGINE=InnoDb;
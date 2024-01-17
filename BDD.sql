-- Active: 1693360576251@@localhost@3306
----------------------------------
/* CREACION DE BASE DE DATOS */
----------------------------------
/*CREATE DATABASE uno;

USE uno;*/

------------------------
/* CREACION DE TABLAS */
------------------------

/*CREATE TABLE IF NOT EXISTS puntajes(
    Nombre CHAR(15) NOT NULL,
    Apuesta CHAR(200) NOT NULL
);*/

---------------------
/* INSERT DE DATOS */
---------------------

/*INSERT INTO puntajes (Nombre, Apuesta)
VALUES
('MACO', 'Sacar las cosas del lava-vajillas y ordenar la cocina'),
('FACU', 'Selfie con los caballos'),
('MACO', 'Sacar la basura y sacarse una selfie en mc donalds'),
('FACU', 'Ayudar al pequi a hacer el matambre'),
('RAMA', 'Ir a buscar al abuelo a lo de Alberto'),
('FACU', 'Acompaniar al abuelo a comprar pan y coca cola'),
('MACO', 'Hacer la guarnicion para el matambre del abuelo'),
('FACU', 'Hacer te y lavar todo'),
('MACO', 'Hacer la merienda'),
('FACU', 'Lavar los platos'),
('RAMA', 'Lavar'),
('RAMA', 'Lavar las ollas'),
('RAMA', 'Cocinar y lavar todo'),
('FACU', 'Estar una hora atrapado en la pileta'),
('RAMA', 'Subir las escaleras de la pileta 50 veces'),
('MACO', 'Cocinar'),
('FACU', 'Guardar todo y ocuparse de la cena'),
('FACU', 'Lavar todo a mano y sacar la basura'),
('FACU', 'Lavar la fuente de milanesas'),
('RAMA', 'Estar una hora encerrado en la pileta'),
('RAMA', 'Ayudar al abuelo a armar el arbolito'),
('FACU', 'Robar un limon o tirarse a la pileta'),
('FACU', 'Robar un limon o tirarse a la pileta');*/

---------------------------------------
/* VER CUANTAS VECES PERDIO CADA UNO */
---------------------------------------

/*SELECT Nombre, count(*) AS 'Perdidas' FROM puntajes GROUP BY Nombre;*/

--------------------------------------
/* INSERT PARA CADA RESULTADO NUEVO */
--------------------------------------

/*INSERT INTO puntajes (Nombre, Apuesta) VALUES ({self.__elPerdedor}, {self.__laApuesta});*/

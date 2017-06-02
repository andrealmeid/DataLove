-- arquivo para criacao das tabelas do banco de dados

BEGIN TRANSACTION;
CREATE TABLE "Tag" (
	`id_tag`	INTEGER NOT NULL,
	`nome`	TEXT NOT NULL,
	`quantidade`	INTEGER NOT NULL,
	PRIMARY KEY(`id_tag`)
);
CREATE TABLE "Spotted" (
	`id_spot`	INTEGER NOT NULL,
	`texto`	TEXT,
	`horário`	DATETIME,
	`cita`	INTEGER,
	`autor`	INTEGER,
	PRIMARY KEY(`id_spot`),
	FOREIGN KEY(`cita`) REFERENCES `Pessoa`(`id_pes`),
	FOREIGN KEY(`autor`) REFERENCES `Pessoa`(`id_pes`)
);
CREATE TABLE "Reage" (
	`id_pes`	INTEGER NOT NULL,
	`id_spot`	INTEGER NOT NULL,
	`horario`	TEXT,
	`tipo`	TEXT,
	PRIMARY KEY(`id_pes`,`id_spot`),
	FOREIGN KEY(`id_pes`) REFERENCES `Pessoa`(`id_pes`),
	FOREIGN KEY(`id_spot`) REFERENCES `Spotted`(`id_spot`)
);
CREATE TABLE Pessoa(
	id_pes INTEGER PRIMARY KEY NOT NULL,
	nome TEXT,
	idade INTEGER
);
CREATE TABLE "Local" (
	`id_tag`	INTEGER NOT NULL,
	`evento`	TEXT,
	PRIMARY KEY(`id_tag`)
);
CREATE TABLE "Fenotipo" (
	`id_tag`	INTEGER NOT NULL,
	`categoria`	TEXT,
	PRIMARY KEY(`id_tag`)
);
CREATE TABLE "Descrita" (
	`id_pes`	INTEGER NOT NULL,
	`id_tag`	INTEGER NOT NULL,
	PRIMARY KEY(`id_pes`,`id_tag`),
	FOREIGN KEY(`id_pes`) REFERENCES `Pessoa`(`id_pes`),
	FOREIGN KEY(`id_tag`) REFERENCES `Tag`(`id_tag`)
);
CREATE TABLE "Curso" (
	`id_tag`	INTEGER NOT NULL,
	`instituto`	TEXT,
	PRIMARY KEY(`id_tag`)
);
CREATE TABLE "Contem" (
	`id_spot`	INTEGER NOT NULL,
	`id_tag`	INTEGER NOT NULL,
	PRIMARY KEY(`id_spot`,`id_tag`),
	FOREIGN KEY(`id_spot`) REFERENCES `Spotted`(`id_spot`),
	FOREIGN KEY(`id_tag`) REFERENCES `Tag`(`id_tag`)
);
CREATE TABLE "Comentario" (
	`id_coment`	INTEGER NOT NULL,
	`texto`	TEXT,
	`horario`	DATETIME,
	`id_spot`	INTEGER NOT NULL,
	`autor`	INTEGER,
	PRIMARY KEY(`id_coment`,`id_spot`),
	FOREIGN KEY(`id_spot`) REFERENCES `Spotted`(`id_spot`),
	FOREIGN KEY(`autor`) REFERENCES `Pessoa`(`id_pes`)
);
COMMIT;

import os,pymysql
from configDB import dbConnect, getParamsConnexion, serveurConnect 

#requêtes de création de la base
_requetes = {
    "drop" : "DROP DATABASE IF EXISTS base_rapfr",
    "createBase" : "CREATE DATABASE IF NOT EXISTS base_rapfr DEFAULT CHARACTER SET utf8",
    "use" : "USE base_rapfr",
    "createTableAnnonces" : "CREATE TABLE annonces ( N°annonces INTEGER PRIMARY KEY AUTO_INCREMENT,\
        Concert TEXT NOT NULL,\
        Date DATE NOT NULL,\
        LieuDépart TEXT NOT NULL,\
        HeureDépart TEXT NOT NULL,\
        Places INTEGER NOT NULL) ; ",
    
    "createTableChanteurs" : "CREATE TABLE chanteurs ( N°chanteurs INTEGER PRIMARY KEY AUTO_INCREMENT,\
        NomScène TEXT NOT NULL,\
        Nom TEXT NOT NULL,\
        Prénom TEXT NOT NULL,\
        DateNaissance DATE NOT NULL,\
        LienInsta TEXT NOT NULL,\
        DatePremierAlbum DATE NOT NULL,\
        NomGroupe TEXT NOT NULL) ; ",
    
    "createTableConcerts" : "CREATE TABLE concerts ( N°concerts INTEGER PRIMARY KEY AUTO_INCREMENT,\
        Chanteur TEXT NOT NULL,\
        Lieu TEXT NOT NULL,\
        Date DATE NOT NULL,\
        Heure TEXT NOT NULL,\
        Durée INTEGER NOT NULL,\
        Prix INTEGER NOT NULL) ; ",
    
    "createTableGroupes" : "CREATE TABLE groupes ( N°groupes INTEGER PRIMARY KEY AUTO_INCREMENT,\
        NomGroupe TEXT NOT NULL,\
        DateFormation DATE NOT NULL,\
        DatePremierAlbum DATE NOT NULL) ; ",
    
    "createTableMusiques" : "CREATE TABLE musiques ( N°musiques INTEGER PRIMARY KEY AUTO_INCREMENT,\
        Nom TEXT NOT NULL,\
        Auteur TEXT NOT NULL,\
        Durée TEXT NOT NULL,\
        DateSortie DATE NOT NULL,\
        Genre TEXT NOT NULL) ; ",
    
    "createTableUsers" : "CREATE TABLE users ( N°users INTEGER PRIMARY KEY AUTO_INCREMENT,\
        Nom TEXT NOT NULL,\
        Prénom TEXT NOT NULL,\
        NuméroTel INT NOT NULL) ; ",

    "insertAnnonces" : "INSERT INTO annonces VALUES (NULL,'Orelsan','2023-07-15','Bruxelle','20','3'),\
        (NULL,'Orelsan','2023-07-02','Lyon','18','4');",
    
    "insertChanteurs" : "INSERT INTO chanteurs VALUES (NULL,'Orelsan','Cotentin','Aurélien','1982-08-01','https://www.instagram.com/orelsan/','2009-02-16','Casseurs Flowteurs');",
    
    "insertChanteurs2" : "INSERT INTO chanteurs VALUES (NULL,'Gringe','Tranchant','Guillaume','1980-02-20','https://www.instagram.com/gringe/','2018-11-02','Casseurs Flowteurs');",
    
    "insertChanteurs3" : "INSERT INTO chanteurs VALUES (NULL,'Vald','Le Du','Valentin','1992-07-15','https://www.instagram.com/valdsullyvan/','2017-01-20','Aucun');",
    
    "insertChanteurs4" : "INSERT INTO chanteurs VALUES (NULL,'Damso','Kalubi Mwamba','William','1992-05-10','https://www.instagram.com/thedamso/','2016-07-08','Aucun');",
    
    "insertChanteurs5" : "INSERT INTO chanteurs VALUES (NULL,'Nekfeu','Samaras','Ken','1990-04-03','https://open.spotify.com/artist/4LXBc13z5EWsc5N32bLxfH?autoplay=true','2015-06-08','1995');",
    
    "insertChanteurs6" : "INSERT INTO chanteurs VALUES (NULL,'Alpha Wann','Oumar Wann','Alpha','1989-07-02','https://www.instagram.com/alphawann/','2018-09-21','1995');",
    
    "insertChanteurs7" : "INSERT INTO chanteurs VALUES (NULL,'Lorenzo','Serrandour','Jérémie','1994-06-04','https://www.instagram.com/el_larrygarcia/','2017-05-04','Colombine');",
    
    "insertConcerts" : "INSERT INTO concerts VALUES (NULL,'Orelsan','Dour','2023-07-15','23','2','70');",
    
    "insertConcerts2" : "INSERT INTO concerts VALUES (NULL,'Lorenzo','Paris','2023-11-19','20','4','50');",
    
    "insertConcerts3" : "INSERT INTO concerts VALUES (NULL,'Damso','Lyon','2023-08-24','22','2','90');",
    
    "insertGroupes" : "INSERT INTO groupes VALUES (NULL,'Casseurs Flowters','2000-01-01','2013-11-18');",
    
    "insertGroupes2" : "INSERT INTO groupes VALUES (NULL,'1995','2008-01-01','2012-12-31');",
    
    "insertGroupes3" : "INSERT INTO groupes VALUES (NULL,'S-CREW','2001-01-01','2016-06-17');",
    
    "insertMusiques" : "INSERT INTO musiques VALUES (NULL,'San','Orelsan','242','2017-10-20','Rap');",
    
    "insertMusiques2" : "INSERT INTO musiques VALUES (NULL,'Humain','Damso','234','2018-06-15','Rap/Nostalgie');",
    
    "insertMusiques3" : "INSERT INTO musiques VALUES (NULL,'Le chant des sirènes','Orelsan','347','2011-09-26','Conscient/Naration');",
    
    "insertMusiques4" : "INSERT INTO musiques VALUES (NULL,'Des mes cendres','Nekfeu','216','2019-06-06','Rap/Pop');",
    
    "insertMusiques5" : "INSERT INTO musiques VALUES (NULL,'Anunnaki','Vald','203','2022-01-07','Rap');",
    
    "insertMusiques6" : "INSERT INTO musiques VALUES (NULL,'Carton Rouge','Lorenzo','187','2018-01-12','Troll Rap');",
    
    "insertMusiques7" : "INSERT INTO musiques VALUES (NULL,'Changement','Orelsan','198','2008-02-22','Rap');",
    
    "insertUsers" : "INSERT INTO users VALUES (NULL,'Schmidt','Matteo','123456789');",
    
    }

#création de la base
def createBaseMySQL() -> None :
     _dbRap, _cursorRap = serveurConnect()
     _cursorRap.execute(_requetes["drop"])
     _cursorRap.execute(_requetes["createBase"])
     _cursorRap.execute(_requetes["use"])
     _cursorRap.execute(_requetes["createTableAnnonces"])
     _cursorRap.execute(_requetes["createTableChanteurs"])
     _cursorRap.execute(_requetes["createTableConcerts"])
     _cursorRap.execute(_requetes["createTableGroupes"])
     _cursorRap.execute(_requetes["createTableMusiques"])
     _cursorRap.execute(_requetes["createTableUsers"])
     _cursorRap.execute(_requetes["insertAnnonces"])
     _cursorRap.execute(_requetes["insertChanteurs"])
     _cursorRap.execute(_requetes["insertChanteurs4"])
     _cursorRap.execute(_requetes["insertChanteurs3"])
     _cursorRap.execute(_requetes["insertChanteurs2"])
     _cursorRap.execute(_requetes["insertChanteurs5"])
     _cursorRap.execute(_requetes["insertChanteurs7"])
     _cursorRap.execute(_requetes["insertChanteurs6"])
     _cursorRap.execute(_requetes["insertConcerts"])
     _cursorRap.execute(_requetes["insertConcerts2"])
     _cursorRap.execute(_requetes["insertConcerts3"])
     _cursorRap.execute(_requetes["insertGroupes"])
     _cursorRap.execute(_requetes["insertGroupes2"])
     _cursorRap.execute(_requetes["insertGroupes3"])
     _cursorRap.execute(_requetes["insertMusiques"])
     _cursorRap.execute(_requetes["insertMusiques2"])
     _cursorRap.execute(_requetes["insertMusiques3"])
     _cursorRap.execute(_requetes["insertMusiques4"])
     _cursorRap.execute(_requetes["insertMusiques5"])
     _cursorRap.execute(_requetes["insertMusiques6"])
     _cursorRap.execute(_requetes["insertMusiques7"])
     _cursorRap.execute(_requetes["insertUsers"])
     _dbRap.commit()


#création de la base
createBaseMySQL()

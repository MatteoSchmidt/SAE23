import os,pymysql
from configDB import dbConnect, getParamsConnexion, serveurConnect 



#variable de requêtes
chADD="INSERT INTO "
chDEL="DELETE FROM "
chAFF="SELECT * FROM "



state=False
while state!=True:
    print("")
    print("1 afficher une table")
    print("2 ajouter un élément dans une table")
    print("3 supprimer un élément dans une table")
    print("4 afficher toutes les tables")
    repCommande=str(input("Que voulez vous faire ? (''=fin du programme):"))
    _dbRap, _cursorRap = serveurConnect()
    
    #commande de fin
    if repCommande=="":
         print("Au revoir !")
         state=True
    #commande d'affichage
    elif repCommande=="1":
        rep=str(input("Quelle table voulez vous afficher :"))
        reqf=chAFF+"base_rapfr."+rep+";"
        print("_________________________________________")
        print("")
        cr=_cursorRap.execute(reqf)
        res=_cursorRap.fetchall()
        _dbRap.commit()
        for elem in res:
             ch=""
             for i in elem:
                  ch=ch+str(i)+" | "
             print(ch)
        print("")
        print("_________________________________________")
        print("")
    #commande d'ajout d'élément
    elif repCommande=="2":
        rep=str(input("Quelle table voulez vous modifier :"))
        reqf=chADD+"base_rapfr."+rep+" VALUES (NULL"
        if rep=='annonces':
            maxv=5
            listch=["Artiste du concert (TEXT):", "Date (AAAA-MM-JJ):", "Lieu de départ (TEXT):", "Heure de départ (TEXT):", "Places (ENTIER):"]
        elif rep=='chanteurs':
            maxv=7
            listch=["Nom de scène (TEXT):","Nom (TEXT):","Prénom (TEXT):", "Date de naissance (AAAA-MM-JJ):", "Lien insta (TEXT):", "Date du premier album (AAAA-MM-JJ):", "Nom du groupe (TEXT):"]
        elif rep=='concerts':
            maxv=6
            listch=["Nom du chanteur (TEXT):", "Lieu (TEXT):", "Date (AAAA-MM-JJ):", "Heure (TEXT):", "Durée (INT):", "Prix (INT):"]
        elif rep=='groupes':
            maxv=3
            listch=["Nom du groupe (TEXT):", "Date de formation (AAAA-MM-JJ):","Date du premier album (AAAA-MM-JJ):"]
        elif rep=='musiques':
            maxv=5
            listch=["Nom de la musique (TEXT):", "Auteur (TEXT):","Durée (TEXT):", "Date de sortie (AAAA-MM-JJ):", "Genre (TEXT):"]
        elif rep=='users':
            maxv=3
            listch=["Nom (TEXT):", "Prénom (TEXT):","Numéro de tel (INT 10 chiffres sans espaces):"]
        else:
            print("mauvaise table")
        i=1
        while i<=maxv:
            rep=input(f"{listch[i-1]}")
            reqf=reqf+","+"'"+rep+"'"
            i+=1
        reqf=reqf+");"
        print("_________________________________________")
        print("")
        cr=_cursorRap.execute(reqf)
        res=_cursorRap.fetchall()
        _dbRap.commit()
        print("")
    #commande de suppression
    elif repCommande=="3":
        rep=str(input("Quelle table voulez vous modifier :"))
        req=chDEL+"base_rapfr."+rep+" WHERE N°"+rep+" = "
        elem=str(input("Quel colonne voulez vous supprimer (N°):"))
        reqf=req+elem
        print("_________________________________________")
        print("")
        cr=_cursorRap.execute(reqf)
        res=_cursorRap.fetchall()
        _dbRap.commit()
        print("")
    elif repCommande=="4":
        print("_________________________________________")
        print("")
        print("Annonces :")
        cr=_cursorRap.execute("SELECT * FROM base_rapfr.annonces")
        res=_cursorRap.fetchall()
        for elem in res:
             ch=""
             for i in elem:
                  ch=ch+str(i)+" | "
             print(ch)
        print("")
        print("Chanteurs :")
        cr=_cursorRap.execute("SELECT * FROM base_rapfr.chanteurs")
        res=_cursorRap.fetchall()
        for elem in res:
             ch=""
             for i in elem:
                  ch=ch+str(i)+" | "
             print(ch)
        print("")
        print("Concerts :")
        cr=_cursorRap.execute("SELECT * FROM base_rapfr.concerts")
        res=_cursorRap.fetchall()
        for elem in res:
             ch=""
             for i in elem:
                  ch=ch+str(i)+" | "
             print(ch)
        print("")
        print("Groupes :")
        cr=_cursorRap.execute("SELECT * FROM base_rapfr.groupes")
        res=_cursorRap.fetchall()
        for elem in res:
             ch=""
             for i in elem:
                  ch=ch+str(i)+" | "
             print(ch)
        print("")
        print("Musiques :")
        cr=_cursorRap.execute("SELECT * FROM base_rapfr.musiques")
        res=_cursorRap.fetchall()
        for elem in res:
             ch=""
             for i in elem:
                  ch=ch+str(i)+" | "
             print(ch)
        print("")
        print("Users :")
        cr=_cursorRap.execute("SELECT * FROM base_rapfr.users")
        res=_cursorRap.fetchall()
        for elem in res:
             ch=""
             for i in elem:
                  ch=ch+str(i)+" | "
             print(ch)
        print("")
        print("_________________________________________")
    else:
        print("Faites un choix entre 1 / 2 / 3")
        state=False
            

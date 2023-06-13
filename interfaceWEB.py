import cherrypy, os, os.path,pymysql,shutil,random

from mako.template import Template
from mako.lookup import TemplateLookup
from createBASE import createBaseMySQL
from configDB import dbConnect
from configDB import dbConnect, getParamsConnexion, serveurConnect 


_dbRap, _cursorRap = serveurConnect()


mylookup = TemplateLookup(directories=['res/templates'], input_encoding='utf-8', module_directory='res/tmp/mako_modules')

def Rappeurs():
    cr=_cursorRap.execute("SELECT * FROM base_rapfr.chanteurs;")
    resChanteurs=_cursorRap.fetchall()
    _dbRap.commit()
    chRappeur=[]
    for elem in resChanteurs:
        chc=""
        nbimage=random.randint(1,4)
        nomimg="rappeur"+str(nbimage)+".png"
        rappeur=f"""
                            <div class="col mb-5">
                                <div class="card h-100">
                                    <!-- Product image-->
                                    <img class="card-img-top" src="static/assets/{nomimg}" alt="..." width="300px" height="150px"/>
                                    <!-- Product details-->
                                    <div class="card-body p-4">
                                        <div class="text-center">
                                            <!-- Product name-->
                                            <h5 class="fw-bolder">{elem[1]}</h5>
                                            <br>
                                            <span>Nom : {elem[3]}</span>
                                            <br>
                                            <span>Prénom : {elem[2]}</span>
                                            <br>
                                            <span>Date de naissance : {elem[4]}</span>
                                            <br>
                                            <span>Date du 1er album : {elem[6]}</span>
                                            <br>
                                            <span>Groupe : {elem[7]}</span>
                                        </div>
                                    </div>
                                    <!-- Product actions-->
                                    <div class="card-footer p-4 pt-0 border-top-0 bg-transparent">
                                        <div class="text-center"><a class="btn btn-outline-dark mt-auto" href="{elem[5]}">Insta</a></div>
                                    </div>
                                </div>
                            </div>
        """
        chc=chc+rappeur
        chRappeur.append(chc)
    return chRappeur

def TriRappeurs(ch):
    req=f"SELECT * FROM base_rapfr.chanteurs ORDER BY {ch};"
    cr=_cursorRap.execute(req)
    resChanteurs=_cursorRap.fetchall()
    _dbRap.commit()
    chRappeur=[]
    for i in range(len(resChanteurs)):
        chc=""
        nbimage=random.randint(1,4)
        nomimg="rappeur"+str(nbimage)+".png"
        rappeur=f"""
                            <div class="col mb-5">
                                <div class="card h-100">
                                    <!-- Product image-->
                                    <img class="card-img-top" src="static/assets/{nomimg}" alt="..." width="300px" height="150px"/>
                                    <!-- Product details-->
                                    <div class="card-body p-4">
                                        <div class="text-center">
                                            <!-- Product name-->
                                            <h5 class="fw-bolder">{resChanteurs[i][1]}</h5>
                                            <br>
                                            <span>Nom : {resChanteurs[i][2]}</span>
                                            <br>
                                            <span>Prénom : {resChanteurs[i][3]}</span>
                                            <br>
                                            <span>Date de naissance : {resChanteurs[i][4]}</span>
                                            <br>
                                            <span>Date du 1er album : {resChanteurs[i][6]}</span>
                                            <br>
                                            <span>Groupe : {resChanteurs[i][7]}</span>
                                        </div>
                                    </div>
                                    <!-- Product actions-->
                                    <div class="card-footer p-4 pt-0 border-top-0 bg-transparent">
                                        <div class="text-center"><a class="btn btn-outline-dark mt-auto" href="{resChanteurs[i][5]}">Insta</a></div>
                                    </div>
                                </div>
                            </div>
        """
        chc=chc+rappeur
        chRappeur.append(chc)
    return chRappeur

def Groupes():
    cr=_cursorRap.execute("SELECT * FROM base_rapfr.groupes;")
    resGroupes=_cursorRap.fetchall()
    _dbRap.commit()
    chGroupes=[]
    for i in range(len(resGroupes)):
        chm=""
        groupes=f"""
                            <div class="col mb-5">
                                <div class="card h-100">
                                    <!-- Product image-->
                                    <img class="card-img-top" src="static/assets/groupe1.jpg" alt="..." width="300px" height="150px"/>
                                    <!-- Product details-->
                                    <div class="card-body p-4">
                                        <div class="text-center">
                                            <!-- Product name-->
                                            <h5 class="fw-bolder">{resGroupes[i][1]}</h5>
                                            <br>
                                            <span>Date de formation : {resGroupes[i][2]}</span>
                                            <br>
                                            <span>Date du premier album : {resGroupes[i][3]}</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
        """
        chm=chm+groupes
        chGroupes.append(chm)
    return chGroupes

def TriGroupes(ch):
    req=f"SELECT * FROM base_rapfr.groupes ORDER BY {ch};"
    cr=_cursorRap.execute(req)
    resGroupes=_cursorRap.fetchall()
    _dbRap.commit()
    chGroupes=[]
    for i in range(len(resGroupes)):
        chm=""
        groupes=f"""
                            <div class="col mb-5">
                                <div class="card h-100">
                                    <!-- Product image-->
                                    <img class="card-img-top" src="static/assets/groupe1.jpg" alt="..." width="300px" height="150px"/>
                                    <!-- Product details-->
                                    <div class="card-body p-4">
                                        <div class="text-center">
                                            <!-- Product name-->
                                            <h5 class="fw-bolder">{resGroupes[i][1]}</h5>
                                            <br>
                                            <span>Date de formation : {resGroupes[i][2]}</span>
                                            <br>
                                            <span>Date du premier album : {resGroupes[i][3]}</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
        """
        chm=chm+groupes
        chGroupes.append(chm)
    return chGroupes

def Musiques():
    crMusiques=_cursorRap.execute("SELECT * FROM base_rapfr.musiques;")
    resMusiques=_cursorRap.fetchall()
    _dbRap.commit()
    chMusiques=[]
    for i in range(len(resMusiques)):
        chm=""
        nbimage=random.randint(1,4)
        nomimg="musiques"+str(nbimage)+".jpg"
        musiques=f"""
                            <div class="col mb-5">
                                <div class="card h-100">
                                    <!-- Product image-->
                                    <img class="card-img-top" src="static/assets/{nomimg}" alt="Image aléatoire représentant de la musiques" width="300px" height="150px"/>
                                    <!-- Product details-->
                                    <div class="card-body p-4">
                                        <div class="text-center">
                                            <!-- Product name-->
                                            <h5 class="fw-bolder">{resMusiques[i][1]}</h5>
                                            <br>
                                            <span>Auteur : {resMusiques[i][2]}</span>
                                            <br>
                                            <span>Durée : {resMusiques[i][3]}s</span>
                                            <br>
                                            <span>Date de sortie : {resMusiques[i][4]}</span>
                                            <br>
                                            <span>Genre : {resMusiques[i][5]}</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
        """
        chm=chm+musiques
        chMusiques.append(chm)
    return chMusiques

def TriMusiques(ch):
    req=f"SELECT * FROM base_rapfr.musiques ORDER BY {ch};"
    crMusiques=_cursorRap.execute(req)
    resMusiques=_cursorRap.fetchall()
    _dbRap.commit()
    chMusiques=[]
    for i in range(len(resMusiques)):
        chm=""
        nbimage=random.randint(1,4)
        nomimg="musiques"+str(nbimage)+".jpg"
        musiques=f"""
                            <div class="col mb-5">
                                <div class="card h-100">
                                    <!-- Product image-->
                                    <img class="card-img-top" src="static/assets/{nomimg}" alt="Image aléatoire représentant de la musiques" width="300px" height="150px"/>
                                    <!-- Product details-->
                                    <div class="card-body p-4">
                                        <div class="text-center">
                                            <!-- Product name-->
                                            <h5 class="fw-bolder">{resMusiques[i][1]}</h5>
                                            <br>
                                            <span>Auteur : {resMusiques[i][2]}</span>
                                            <br>
                                            <span>Durée : {resMusiques[i][3]}s</span>
                                            <br>
                                            <span>Date de sortie : {resMusiques[i][4]}</span>
                                            <br>
                                            <span>Genre : {resMusiques[i][5]}</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
        """
        chm=chm+musiques
        chMusiques.append(chm)
    return chMusiques

def Concerts():
    crConcerts=_cursorRap.execute("SELECT * FROM base_rapfr.concerts;")
    resConcerts=_cursorRap.fetchall()
    _dbRap.commit()
    chConcerts=[]
    for i in range(len(resConcerts)):
        chm=""
        nbimage=random.randint(1,4)
        nomimg="concerts"+str(nbimage)+".jpeg"
        concerts=f"""
                            <div class="col mb-5">
                                <div class="card h-100">
                                    <!-- Product image-->
                                    <img class="card-img-top" src="static/assets/{nomimg}" alt="Image de concerts aléatoire" width="300px" height="150px"/>
                                    <!-- Product details-->
                                    <div class="card-body p-4">
                                        <div class="text-center">
                                            <!-- Product name-->
                                            <h5 class="fw-bolder">{resConcerts[i][1]}</h5>
                                            <br>
                                            <span>Lieu : {resConcerts[i][2]}</span>
                                            <br>
                                            <span>Date : {resConcerts[i][3]}</span>
                                            <br>
                                            <span>Heure : {resConcerts[i][4]}h</span>
                                            <br>
                                            <span>Durée : {resConcerts[i][5]}h</span>
                                            <br>
                                            <span>Prix : {resConcerts[i][6]}€</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
        """
        chm=chm+concerts
        chConcerts.append(chm)
    return chConcerts

def TriConcerts(ch):
    req=f"SELECT * FROM base_rapfr.concerts ORDER BY {ch};"
    crConcerts=_cursorRap.execute(req)
    resConcerts=_cursorRap.fetchall()
    _dbRap.commit()
    chConcerts=[]
    for i in range(len(resConcerts)):
        chm=""
        nbimage=random.randint(1,4)
        nomimg="concerts"+str(nbimage)+".jpeg"
        concerts=f"""
                            <div class="col mb-5">
                                <div class="card h-100">
                                    <!-- Product image-->
                                    <img class="card-img-top" src="static/assets/{nomimg}" alt="Image de concerts aléatoire" width="300px" height="150px"/>
                                    <!-- Product details-->
                                    <div class="card-body p-4">
                                        <div class="text-center">
                                            <!-- Product name-->
                                            <h5 class="fw-bolder">{resConcerts[i][1]}</h5>
                                            <br>
                                            <span>Lieu : {resConcerts[i][2]}</span>
                                            <br>
                                            <span>Date : {resConcerts[i][3]}</span>
                                            <br>
                                            <span>Heure : {resConcerts[i][4]}h</span>
                                            <br>
                                            <span>Durée : {resConcerts[i][5]}h</span>
                                            <br>
                                            <span>Prix : {resConcerts[i][6]}€</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
        """
        chm=chm+concerts
        chConcerts.append(chm)
    return chConcerts

def Annonces():
    crAnnonces=_cursorRap.execute("SELECT * FROM base_rapfr.annonces;")
    resAnnonces=_cursorRap.fetchall()
    _dbRap.commit()
    chAnnonces=[]
    for i in range(len(resAnnonces)):
        chm=""
        nbimage=random.randint(1,4)
        nomimg="concerts"+str(nbimage)+".jpeg"
        annonces=f"""
                            <div class="col mb-5">
                                <div class="card h-100">
                                    <!-- Product image-->
                                    <img class="card-img-top" src="static/assets/{nomimg}" alt="Image de concerts aléatoire" width="300px" height="150px"/>
                                    <!-- Product details-->
                                    <div class="card-body p-4">
                                        <div class="text-center">
                                            <!-- Product name-->
                                            <h5 class="fw-bolder">N°{resAnnonces[i][0]}</h5>
                                            <br>
                                            <span>Auteur : {resAnnonces[i][1]}</span>
                                            <br>
                                            <span>Date : {resAnnonces[i][2]}</span>
                                            <br>
                                            <span>Lieu de départ : {resAnnonces[i][3]}</span>
                                            <br>
                                            <span>Heure de départ : {resAnnonces[i][4]}h</span>
                                            <br>
                                            <span>Places : {resAnnonces[i][5]}</span>
                                            <br>
                                        </div>
                                    </div>
                                </div>
                            </div>
        """
        chm=chm+annonces
        chAnnonces.append(chm)
    return chAnnonces
    
def nbPlaces():
    crAnnonces=_cursorRap.execute("SELECT * FROM base_rapfr.annonces;")
    resAnnonces=_cursorRap.fetchall()
    _dbRap.commit()
    listPlaces=[]
    for i in resAnnonces:
        nbplaces=i[5]
        listPlaces.append(int(nbplaces))
    return listPlaces

listInscrit=["<span></span><br>"]
def userAnnonces(num, n, p, t):
    crAnnonces=_cursorRap.execute("SELECT * FROM base_rapfr.annonces;")
    resAnnonces=_cursorRap.fetchall()
    _dbRap.commit()
    ch=""
    for elem in resAnnonces:
        if num==int(elem[0]):
            ch=ch+f"""
                            <div class="col mb-5">
                                <div class="card h-100">
                                    <div class="card-body p-4">
                                        <div class="text-center">
                                            <!-- Product name-->
                                            <h5 class="fw-bolder">Covoiturage N°{num}</h5>
                                            <br>
                                            <span>Nom : {n}</span>
                                            <br>
                                            <span>Prénom : {p}</span>
                                            <br>
                                            <span>Numéro : {t}</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
            """
            listInscrit.append(ch)
        else:
            pass
    return listInscrit


def allBase():
    chAll=[]
    crRap=_cursorRap.execute("SELECT * FROM base_rapfr.chanteurs;")
    resRap=_cursorRap.fetchall()
    _dbRap.commit()
    for i in range(len(resRap)):
        chm=""
        nbimage=random.randint(1,4)
        nomimg="rappeur"+str(nbimage)+".png"
        rappeur=f"""
                            <div class="col mb-5">
                                <div class="card h-100">
                                    <!-- Product image-->
                                    <img class="card-img-top" src="static/assets/{nomimg}" alt="" width="300px" height="150px"/>
                                    <!-- Product details-->
                                    <div class="card-body p-4">
                                        <div class="text-center">
                                            <!-- Product name-->
                                            <h5 class="fw-bolder">Rappeur N°{resRap[i][0]}</h5>
                                            <br>
                                            <span>Nom : {resRap[i][1]}</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
        """
        chm=chm+rappeur
        chAll.append(chm)
        
    crGroupe=_cursorRap.execute("SELECT * FROM base_rapfr.groupes;")
    resGroupe=_cursorRap.fetchall()
    _dbRap.commit()
    for i in range(len(resGroupe)):
        chm=""
        groupe=f"""
                            <div class="col mb-5">
                                <div class="card h-100">
                                    <!-- Product image-->
                                    <img class="card-img-top" src="static/assets/groupe1.jpg" alt="" width="300px" height="150px"/>
                                    <!-- Product details-->
                                    <div class="card-body p-4">
                                        <div class="text-center">
                                            <!-- Product name-->
                                            <h5 class="fw-bolder">Groupe N°{resGroupe[i][0]}</h5>
                                            <br>
                                            <span>Nom : {resGroupe[i][1]}</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
        """
        chm=chm+groupe
        chAll.append(chm)
    
    crMusique=_cursorRap.execute("SELECT * FROM base_rapfr.musiques;")
    resMusique=_cursorRap.fetchall()
    _dbRap.commit()
    for i in range(len(resMusique)):
        chm=""
        nbimage=random.randint(1,4)
        nomimg="musiques"+str(nbimage)+".jpg"
        musique=f"""
                            <div class="col mb-5">
                                <div class="card h-100">
                                    <!-- Product image-->
                                    <img class="card-img-top" src="static/assets/{nomimg}" alt="" width="300px" height="150px"/>
                                    <!-- Product details-->
                                    <div class="card-body p-4">
                                        <div class="text-center">
                                            <!-- Product name-->
                                            <h5 class="fw-bolder">Musique N°{resMusique[i][0]}</h5>
                                            <br>
                                            <span>Nom : {resMusique[i][1]}</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
        """
        chm=chm+musique
        chAll.append(chm)
    
    crConcert=_cursorRap.execute("SELECT * FROM base_rapfr.concerts;")
    resConcert=_cursorRap.fetchall()
    _dbRap.commit()
    for i in range(len(resConcert)):
        chm=""
        nbimage=random.randint(1,4)
        nomimg="concerts"+str(nbimage)+".jpeg"
        concert=f"""
                            <div class="col mb-5">
                                <div class="card h-100">
                                    <!-- Product image-->
                                    <img class="card-img-top" src="static/assets/{nomimg}" alt="" width="300px" height="150px"/>
                                    <!-- Product details-->
                                    <div class="card-body p-4">
                                        <div class="text-center">
                                            <!-- Product name-->
                                            <h5 class="fw-bolder">Concert N°{resConcert[i][0]}</h5>
                                            <br>
                                            <span>Nom : {resConcert[i][1]}</span>
                                            <br>
                                            <span>Date : {resConcert[i][3]}</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
        """
        chm=chm+concert
        chAll.append(chm)
    return chAll



class InterfaceWebRap(object):    
    ###### Page d'accueil #############
    @cherrypy.expose
    def index(self):
        mytemplate = mylookup.get_template("index.html")
        return mytemplate.render()
        
    @cherrypy.expose
    def affRappeurs(self):
        mytemplate = mylookup.get_template("rappeur.html")
        return mytemplate.render(mesRappeurs=Rappeurs())
    
    @cherrypy.expose
    def affMusiques(self):
        mytemplate = mylookup.get_template("musiques.html")
        return mytemplate.render(mesMusiques=Musiques())
    
    @cherrypy.expose
    def affGroupes(self):
        mytemplate = mylookup.get_template("groupes.html")
        return mytemplate.render(mesGroupes=Groupes())
    
    @cherrypy.expose
    def affConcerts(self):
        mytemplate = mylookup.get_template("concerts.html")
        return mytemplate.render(mesConcerts=Concerts())
    
    @cherrypy.expose
    def affCovoiturage(self):
        mytemplate = mylookup.get_template("covoiturage.html")
        return mytemplate.render()
    
    @cherrypy.expose
    def affAnnonces(self):
        listPlaces=nbPlaces()
        mytemplate = mylookup.get_template("inscrire.html")
        return mytemplate.render(mesAnnonces=Annonces())
    
    @cherrypy.expose
    def affProposer(self):
        mytemplate = mylookup.get_template("proposer.html")
        return mytemplate.render()
    
    @cherrypy.expose
    def affRappeursParGroupe(self):
        mytemplate = mylookup.get_template("rappeur.html")
        return mytemplate.render(mesRappeurs=TriRappeurs("NomGroupe"))
    
    @cherrypy.expose
    def affRappeursParDate(self):
        mytemplate = mylookup.get_template("rappeur.html")
        return mytemplate.render(mesRappeurs=TriRappeurs("DateNaissance"))
    
    @cherrypy.expose
    def affMusiquesParDate(self):
        mytemplate = mylookup.get_template("musiques.html")
        return mytemplate.render(mesMusiques=TriMusiques("DateSortie"))
    
    @cherrypy.expose
    def affMusiquesParAuteur(self):
        mytemplate = mylookup.get_template("musiques.html")
        return mytemplate.render(mesMusiques=TriMusiques("Auteur"))
    
    @cherrypy.expose
    def affConcertsDate(self):
        mytemplate = mylookup.get_template("concerts.html")
        return mytemplate.render(mesConcerts=TriConcerts("Date"))
    
    @cherrypy.expose
    def affConcertsPrix(self):
        mytemplate = mylookup.get_template("concerts.html")
        return mytemplate.render(mesConcerts=TriConcerts("Prix"))
    
    @cherrypy.expose
    def affGroupesDate(self):
        mytemplate = mylookup.get_template("groupes.html")
        return mytemplate.render(mesGroupes=TriGroupes("DateFormation"))
    
    @cherrypy.expose
    def affGroupesNom(self):
        mytemplate = mylookup.get_template("groupes.html")
        return mytemplate.render(mesGroupes=TriGroupes("NomGroupe"))
    
    @cherrypy.expose
    def addAnnonces(self, **params):
        req=f"INSERT INTO base_rapfr.annonces VALUES (NULL,'{params['Concert']}','{params['Date']}','{params['LieuDépart']}','{params['HeureDépart']}','{params['Places']}');"
        _dbRap, _cursorRap = serveurConnect()
        _cursorRap.execute(req)
        _dbRap.commit()
        mytemplate = mylookup.get_template("inscrire.html")
        return mytemplate.render(mesAnnonces=Annonces())
        

    @cherrypy.expose
    def inscriptionAnnonces(self, **params):
        nb=int(params['Concert'])
        nom=params['Nom']
        prénom=params['Prénom']
        tel=params['Numéro']
        listPlaces=nbPlaces()
        if listPlaces[nb-1]>0:
            req=f"UPDATE base_rapfr.annonces SET Places={listPlaces[nb-1]-1} WHERE N°annonces='{nb}';"
            _dbRap, _cursorRap = serveurConnect()
            _cursorRap.execute(req)
            _dbRap.commit()
            mytemplate = mylookup.get_template("userInscrit.html")
            return mytemplate.render(listInscrit=userAnnonces(nb, nom, prénom, tel))
        else:
            mytemplate = mylookup.get_template("plusDePlace.html")
            return mytemplate.render()
    
    
    @cherrypy.expose
    def pageInscrit(self):
        mytemplate = mylookup.get_template("userInscrit.html")
        return mytemplate.render(listInscrit=userAnnonces(0, "", "", ""))
    
    @cherrypy.expose
    def pageAjouter(self):
        mytemplate = mylookup.get_template("ajouter.html")
        return mytemplate.render()
    
    @cherrypy.expose
    def addRappeur(self, **params):
        req=f"INSERT INTO base_rapfr.chanteurs VALUES (NULL,'{params['NomScène']}','{params['Nom']}','{params['Prénom']}','{params['Date']}','{params['LienInsta']}','{params['DateAlbum']}','{params['NomGroupe']}');"
        _dbRap, _cursorRap = serveurConnect()
        _cursorRap.execute(req)
        _dbRap.commit()
        mytemplate = mylookup.get_template("rappeur.html")
        return mytemplate.render(mesRappeurs=Rappeurs())
    

    @cherrypy.expose
    def addGroupe(self, **params):
        req=f"INSERT INTO base_rapfr.groupes VALUES (NULL,'{params['Nom']}','{params['DateF']}','{params['DateA']}');"
        _dbRap, _cursorRap = serveurConnect()
        _cursorRap.execute(req)
        _dbRap.commit()
        mytemplate = mylookup.get_template("groupes.html")
        return mytemplate.render(mesGroupes=Groupes())
    
    @cherrypy.expose
    def addMusique(self, **params):
        req=f"INSERT INTO base_rapfr.musiques VALUES (NULL,'{params['Nom']}','{params['Auteur']}','{params['Durée']}','{params['Date']}','{params['Genre']}');"
        _dbRap, _cursorRap = serveurConnect()
        _cursorRap.execute(req)
        _dbRap.commit()
        mytemplate = mylookup.get_template("musiques.html")
        return mytemplate.render(mesMusiques=Musiques())
    
    @cherrypy.expose
    def addConcert(self, **params):
        req=f"INSERT INTO base_rapfr.concerts VALUES (NULL,'{params['Chanteur']}','{params['Lieu']}','{params['Date']}','{params['Heure']}','{params['Durée']}','{params['Prix']}');"
        _dbRap, _cursorRap = serveurConnect()
        _cursorRap.execute(req)
        _dbRap.commit()
        mytemplate = mylookup.get_template("concerts.html")
        return mytemplate.render(mesConcerts=Concerts())
    
    @cherrypy.expose
    def pageSupprimer(self):
        mytemplate = mylookup.get_template("supprimer.html")
        return mytemplate.render(listbase=allBase())
    
    @cherrypy.expose
    def supprimer(self, **params):
        req=f"DELETE FROM base_rapfr.{params['Table']} WHERE N°{params['Table']}={params['Num']}"
        _dbRap, _cursorRap = serveurConnect()
        _cursorRap.execute(req)
        _dbRap.commit()
        mytemplate = mylookup.get_template("supprimer.html")
        return mytemplate.render(listbase=allBase())
    
if __name__ == '__main__':
    createBaseMySQL()
    cherrypy.quickstart(InterfaceWebRap(), '/', 'config.txt')

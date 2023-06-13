# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1686068284.0597143
_enable_loop = True
_template_filename = 'res/templates/supprimer.html'
_template_uri = 'supprimer.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        listbase = context.get('listbase', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html lang="fr">\n    <head>\n        <meta charset="utf-8" />\n        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />\n        <meta name="description" content="" />\n        <meta name="author" content="" />\n        <title>100% RAPFR</title>\n        <!-- Favicon-->\n        <link rel="icon" type="image/x-icon" href="static/assets/disque.ico" />\n        <!-- Bootstrap icons-->\n        <link href="static/css/bootstrap-icons.css" rel="stylesheet" />\n        <!-- Core theme CSS (includes Bootstrap)-->\n        <link href="static/css/styles.css" rel="stylesheet" />\n    </head>\n    <body>\n        <!-- Navigation-->\n        <nav class="navbar navbar-expand-lg navbar-light bg-light">\n            <div class="container px-4 px-lg-5">\n                <a class="navbar-brand" href="#!">100% RAP</a>\n                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>\n                <div class="collapse navbar-collapse" id="navbarSupportedContent">\n                    <ul class="navbar-nav me-auto mb-2 mb-lg-0 ms-lg-4">\n                        <li class="nav-item"><a class="nav-link active" aria-current="page" href="index">Accueil</a></li>\n                        <li class="nav-item"><a class="nav-link" href="affRappeurs">Rappeurs</a></li>\n                        <li class="nav-item"><a class="nav-link" href="affGroupes">Groupes</a></li>\n                        <li class="nav-item"><a class="nav-link" href="affMusiques">Musiques</a></li>\n                        <li class="nav-item"><a class="nav-link" href="affConcerts">Concerts</a></li>\n                        <li class="nav-item dropdown">\n                            <a class="nav-link dropdown-toggle" id="navbarDropdown" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">Covoiturage</a>\n                            <ul class="dropdown-menu" aria-labelledby="navbarDropdown">\n                                <li><a class="dropdown-item" href="affCovoiturage">Les covoiturages</a></li>\n                                <li><hr class="dropdown-divider" /></li>\n                                <li><a class="dropdown-item" href="affProposer">Proposer un covoiturage</a></li>\n                                <li><a class="dropdown-item" href="affAnnonces">S\'inscrire à un covoiturage</a></li>\n                                <li><a class="dropdown-item" href="pageInscrit">Liste des inscrits</a></li>\n                            </ul>\n                        </li>\n                        <li class="nav-item dropdown">\n                            <a class="nav-link dropdown-toggle" id="navbarDropdown" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false"><strong>CRUD</strong></a>\n                            <ul class="dropdown-menu" aria-labelledby="navbarDropdown">\n                                <li><a class="dropdown-item" href="">CRUD</a></li>\n                                <li><hr class="dropdown-divider" /></li>\n                                <li><a class="dropdown-item" href="pageAjouter">Ajouter</a></li>\n                                <li><a class="dropdown-item" href="pageSupprimer"><strong>Supprimer</strong></a></li>\n                            </ul>\n                        </li>\n                    </ul>\n                </div>\n            </div>\n        </nav>\n        <!-- Header-->\n        <header class="bg-dark py-5">\n            <div class="container px-4 px-lg-5 my-5">\n                <div class="text-center text-white">\n                    <h1 class="display-4 fw-bolder">Supprimer un élément de la base</h1>\n                    <p class="lead fw-normal text-white-50 mb-0">Séléctionnez la table dans laquel vous voulez supprimer et N° de l\'élément</p>\n                </div>\n            </div>\n        </header>\n        <!-- Section-->\n        <section class="py-5">\n            <div class="container px-4 px-lg-5 mt-5">\n                <div class="row gx-4 gx-lg-5 row-cols-2 row-cols-md-3 row-cols-xl-4 justify-content-center">\n')
        for e in listbase :
            __M_writer('                        ')
            __M_writer(str(e))
            __M_writer(' <br />\n')
        __M_writer('                    \n                    \n                    <h1>Formulaire de base de suppression</h1>\n                    <form action="supprimer">\n                        <input type="radio" id="Table" name="Table" value="musiques">Musiques\n                        <br>\n                        <input type="radio" id="Table" name="Table" value="chanteurs">Rappeurs\n                        <br>\n                        <input type="radio" id="Table" name="Table" value="groupes">Groupes\n                        <br>\n                        <input type="radio" id="Table" name="Table" value="concerts">Concerts\n                        <br>\n                        <label for="Num">Numéro :</label>\n                        <input type="int" id="Num" name="Num" required><br><br>\n                        \n                        <input type="submit" value="SUPPRIMER">\n                    </form>\n\n                </div>\n            </div>\n        </section>\n        <!-- Footer-->\n        <footer class="py-5 bg-dark">\n            <div class="container"><p class="m-0 text-center text-white">Matteo SCHMIDT &copy; 100% RAPFR</p></div>\n        </footer>\n        <!-- Bootstrap core JS-->\n        <script src="static/js/bootstrap.bundle.min.js"></script>\n        <!-- Core theme JS-->\n        <script src="static/js/scripts.js"></script>\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/supprimer.html", "uri": "supprimer.html", "source_encoding": "utf-8", "line_map": {"16": 0, "22": 1, "23": 65, "24": 66, "25": 66, "26": 66, "27": 68, "33": 27}}
__M_END_METADATA
"""

# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1686068253.1743338
_enable_loop = True
_template_filename = 'res/templates/groupes.html'
_template_uri = 'groupes.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        mesGroupes = context.get('mesGroupes', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<!DOCTYPE html>\r\n<html lang="fr">\r\n    <head>\r\n        <meta charset="utf-8" />\r\n        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />\r\n        <meta name="description" content="" />\r\n        <meta name="author" content="" />\r\n        <title>100% RAPFR</title>\r\n        <!-- Favicon-->\r\n        <link rel="icon" type="image/x-icon" href="static/assets/disque.ico" />\r\n        <!-- Bootstrap icons-->\r\n        <link href="static/css/bootstrap-icons.css" rel="stylesheet" />\r\n        <!-- Core theme CSS (includes Bootstrap)-->\r\n        <link href="static/css/styles.css" rel="stylesheet" />\r\n    </head>\r\n    <body>\r\n        <!-- Navigation-->\r\n        <nav class="navbar navbar-expand-lg navbar-light bg-light">\r\n            <div class="container px-4 px-lg-5">\r\n                <a class="navbar-brand" href="#!">100% RAP</a>\r\n                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>\r\n                <div class="collapse navbar-collapse" id="navbarSupportedContent">\r\n                    <ul class="navbar-nav me-auto mb-2 mb-lg-0 ms-lg-4">\r\n                        <li class="nav-item"><a class="nav-link active" aria-current="page" href="index">Accueil</a></li>\r\n                        <li class="nav-item"><a class="nav-link" href="affRappeurs">Rappeurs</a></li>\r\n                        <li class="nav-item"><a class="nav-link" href="affGroupes"><strong>Groupes</strong></a></li>\r\n                        <li class="nav-item"><a class="nav-link" href="affMusiques">Musiques</a></li>\r\n                        <li class="nav-item"><a class="nav-link" href="affConcerts">Concerts</a></li>\r\n                        <li class="nav-item dropdown">\r\n                            <a class="nav-link dropdown-toggle" id="navbarDropdown" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">Covoiturage</a>\r\n                            <ul class="dropdown-menu" aria-labelledby="navbarDropdown">\r\n                                <li><a class="dropdown-item" href="affCovoiturage">Les covoiturages</a></li>\r\n                                <li><hr class="dropdown-divider" /></li>\r\n                                <li><a class="dropdown-item" href="affProposer">Proposer un covoiturage</a></li>\r\n                                <li><a class="dropdown-item" href="affAnnonces">S\'inscrire à un covoiturage</a></li>\r\n                                <li><a class="dropdown-item" href="pageInscrit">Liste des inscrits</a></li>\r\n                            </ul>\r\n                        </li>\r\n                        <li class="nav-item dropdown">\r\n                            <a class="nav-link dropdown-toggle" id="navbarDropdown" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">CRUD</a>\r\n                            <ul class="dropdown-menu" aria-labelledby="navbarDropdown">\r\n                                <li><a class="dropdown-item" href="">CRUD</a></li>\r\n                                <li><hr class="dropdown-divider" /></li>\r\n                                <li><a class="dropdown-item" href="pageAjouter">Ajouter</a></li>\r\n                                <li><a class="dropdown-item" href="pageSupprimer">Supprimer</a></li>\r\n                            </ul>\r\n                        </li>\r\n                    </ul>\r\n                </div>\r\n            </div>\r\n        </nav>\r\n        <!-- Header-->\r\n        <header class="bg-dark py-5">\r\n            <div class="container px-4 px-lg-5 my-5">\r\n                <div class="text-center text-white">\r\n                    <h1 class="display-4 fw-bolder">Les groupes à découvrir</h1>\r\n                    <p class="lead fw-normal text-white-50 mb-0">Découvrez de nombreuses informations sur vos groupes préférés !</p>\r\n                </div>\r\n            </div>\r\n        </header>\r\n        <!-- Section-->\r\n        <section class="py-5">\r\n            <div class="card-footer p-4 pt-0 border-top-0 bg-transparent">\r\n                <div class="text-center"><a class="btn btn-outline-dark mt-auto" href="affGroupes">Trier par défaut</a></div>\r\n            </div>\r\n            <div class="card-footer p-4 pt-0 border-top-0 bg-transparent">\r\n                <div class="text-center"><a class="btn btn-outline-dark mt-auto" href="affGroupesDate">Trier par date de formation</a></div>\r\n            </div>\r\n            <div class="card-footer p-4 pt-0 border-top-0 bg-transparent">\r\n                <div class="text-center"><a class="btn btn-outline-dark mt-auto" href="affGroupesNom">Trier par nom</a></div>\r\n            </div>\r\n            <div class="container px-4 px-lg-5 mt-5">\r\n                <div class="row gx-4 gx-lg-5 row-cols-2 row-cols-md-3 row-cols-xl-4 justify-content-center">\r\n')
        for e in mesGroupes :
            __M_writer('                    ')
            __M_writer(str(e))
            __M_writer(' <br />\r\n')
        __M_writer('\r\n                </div>\r\n            </div>\r\n        </section>\r\n        <!-- Footer-->\r\n        <footer class="py-5 bg-dark">\r\n            <div class="container"><p class="m-0 text-center text-white">Matteo SCHMIDT &copy; 100% RAPFR</p></div>\r\n        </footer>\r\n        <!-- Bootstrap core JS-->\r\n        <script src="static/js/bootstrap.bundle.min.js"></script>\r\n        <!-- Core theme JS-->\r\n        <script src="static/js/scripts.js"></script>\r\n    </body>\r\n</html>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/groupes.html", "uri": "groupes.html", "source_encoding": "utf-8", "line_map": {"16": 0, "22": 1, "23": 75, "24": 76, "25": 76, "26": 76, "27": 78, "33": 27}}
__M_END_METADATA
"""

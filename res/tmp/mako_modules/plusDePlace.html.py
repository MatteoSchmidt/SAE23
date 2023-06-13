# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1686071737.8678336
_enable_loop = True
_template_filename = 'res/templates/plusDePlace.html'
_template_uri = 'plusDePlace.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\r\n<!DOCTYPE html>\r\n<html lang="fr">\r\n    <head>\r\n        <meta charset="utf-8" />\r\n        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />\r\n        <meta name="description" content="" />\r\n        <meta name="author" content="" />\r\n        <title>100% RAPFR</title>\r\n        <!-- Favicon-->\r\n        <link rel="icon" type="image/x-icon" href="static/assets/disque.ico" />\r\n        <!-- Bootstrap icons-->\r\n        <link href="static/css/bootstrap-icons.css" rel="stylesheet" />\r\n        <!-- Core theme CSS (includes Bootstrap)-->\r\n        <link href="static/css/styles.css" rel="stylesheet" />\r\n    </head>\r\n    <body>\r\n        <!-- Header-->\r\n        <header class="bg-dark py-5">\r\n            <div class="container px-4 px-lg-5 my-5">\r\n                <div class="text-center text-white">\r\n                    <h1 class="display-4 fw-bolder">Malheursement il n\'y a plus de places dans cette annonces !</h1>\r\n                </div>\r\n            </div>\r\n        </header>\r\n        <section class="py-5">\r\n            <div class="container px-4 px-lg-5 mt-5">\r\n                <div class="row gx-4 gx-lg-5 row-cols-2 row-cols-md-3 row-cols-xl-4 justify-content-center">\r\n                    <div class="card-footer p-4 pt-0 border-top-0 bg-transparent">\r\n                        <div class="text-center"><a class="btn btn-outline-dark mt-auto" href="affAnnonces">Retour</a></div>\r\n                    </div>\r\n                </div>\r\n            </div>\r\n        </section>\r\n        <footer class="py-5 bg-dark">\r\n            <div class="container"><p class="m-0 text-center text-white">Matteo SCHMIDT &copy; 100% RAPFR</p></div>\r\n        </footer>\r\n        <!-- Bootstrap core JS-->\r\n        <script src="static/js/bootstrap.bundle.min.js"></script>\r\n        <!-- Core theme JS-->\r\n        <script src="static/js/scripts.js"></script>\r\n    </body>\r\n</html>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/plusDePlace.html", "uri": "plusDePlace.html", "source_encoding": "utf-8", "line_map": {"16": 0, "21": 1, "27": 21}}
__M_END_METADATA
"""

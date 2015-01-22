# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1421804365.639749
_enable_loop = True
_template_filename = 'C:\\Users\\Blake\\apps\\homepage\\templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n  <meta charset="UTF-8">\r\n  <head>\r\n    \r\n    <title>HomePage</title>\r\n    \r\n')
        __M_writer('    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\r\n    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css"></link>\r\n    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></link>\r\n        \r\n    \r\n\r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\r\n  \r\n  </head>\r\n  <body>\r\n  \r\n    <header>\r\n        <nav class="navbar navbar-default">\r\n            <div class="container-fluid">\r\n                <div class="navbar-header">\r\n                    <a class="navbar-brand" href="/"> Colonial Heritage Foundation</a>\r\n                </div>\r\n                <div class="collapse navbar-collapse">\r\n                  <ul class="nav navbar-nav">\r\n                    <li><a href="/items">Browse</a></li>\r\n                    <li><a href="/items">Rent </a></li>\r\n                  </ul>\r\n                  <ul class="nav navbar-nav navbar-right">\r\n                    <li data-toggle="modal" data-target="#loginModal"><a href="#">Login</a></li>\r\n                    <li><a href="#">Register</a></li>\r\n                  </ul>\r\n                </div>\r\n            </div>\r\n        </nav>\r\n    </header>\r\n      \r\n    <div class="container-fluid">\r\n        <div class="row">\r\n            <div class="col-md-1 left-nav">\r\n                <ul class="nav nav-pills nav-stacked">\r\n                    <li><a href="/about">about</a></li>\r\n                    <li><a href="/contact">contact</a></li>\r\n                    <li><a href="/terms">terms</a></li>\r\n                </ul>\r\n            </div>\r\n            <div class="col-md-11">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n            </div>\r\n        </div>\r\n    </div>\r\n      <div class="modal hide" id="loginModal">\r\n      <div class="modal-dialog">\r\n        <div class="modal-content">\r\n          <div class="modal-header">\r\n              header\r\n          </div>\r\n          <div class="modal-body">\r\n              body\r\n          </div>\r\n          <div class="modal-footer">\r\n            footer\r\n          </div>\r\n        </div>\r\n      </div>\r\n    </div>\r\n      \r\n    <footer>\r\n        <div class="row well">\r\n            <div class="col-md-4">about</div>\r\n            <div class="col-md-4">contact</div>\r\n            <div class="col-md-4">terms</div>\r\n        </div>\r\n    </footer>\r\n  \r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('  \r\n  </body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"33": 5, "34": 15, "35": 22, "36": 22, "37": 22, "42": 58, "43": 87, "44": 87, "45": 87, "16": 4, "18": 0, "51": 57, "57": 57, "27": 2, "28": 4, "29": 5, "63": 57}, "source_encoding": "ascii", "uri": "base.htm", "filename": "C:\\Users\\Blake\\apps\\homepage\\templates/base.htm"}
__M_END_METADATA
"""

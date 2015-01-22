# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1421809147.382278
_enable_loop = True
_template_filename = 'C:\\Users\\Blake\\apps\\homepage\\templates/items.html'
_template_uri = 'items.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="row well col-md-11">\r\n        <form class="form-inline">\r\n          <div class="form-group">\r\n            <input type="text" class="form-control" id="Search" placeholder="Search For An Item">\r\n          </div>\r\n            <div class="btn-group">\r\n              <button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown" aria-expanded="false">\r\n                Any <span class="caret"></span>\r\n              </button>\r\n              <ul class="dropdown-menu" role="menu">\r\n                <li><a href="#">Any</a></li>\r\n                <li><a href="#">Buy</a></li>\r\n                <li><a href="#">Rent</a></li>\r\n              </ul>\r\n            </div>\r\n          <button type="submit" class="btn btn-default">Search</button>\r\n        </form>\r\n    </div>\r\n    <div class="row well col-md-11">\r\n        <div class="col-md-2">\r\n            <img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/colonial_jacket.jpg" alt="">\r\n        </div>\r\n        <div class="row col-md-10">\r\n            Some fancy information about the Product\r\n            <div class="text-muted">FOR RENT: $3.00/day</div>\r\n        </div>\r\n    </div>\r\n    <div class="row well col-md-11">\r\n        <div class="col-md-2">\r\n            <img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/loom.jpg" alt="">\r\n        </div>\r\n        <div class="row col-md-10">\r\n            <div>\r\n                <p class="text-left">Some even more fancy information about a product.<span class="text-right text-danger">OUT OF STOCK!</span></p>\r\n            </div>\r\n            <div class="text-muted">FOR SALE: $69.99</div>\r\n        </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"35": 1, "52": 2, "53": 23, "54": 23, "55": 32, "56": 32, "27": 0, "45": 2, "62": 56}, "source_encoding": "ascii", "uri": "items.html", "filename": "C:\\Users\\Blake\\apps\\homepage\\templates/items.html"}
__M_END_METADATA
"""

# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1421800788.737349
_enable_loop = True
_template_filename = 'C:\\Users\\Blake\\apps\\homepage\\templates/index.html'
_template_uri = 'index.html'
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
        __M_writer('\r\n\r\n')
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
        __M_writer('\r\n    <div id="carousel-index" class="carousel slide" data-ride="carousel">\r\n      <!-- Indicators -->\r\n      <ol class="carousel-indicators">\r\n        <li data-target="#carousel-index" data-slide-to="0" class="active"></li>\r\n        <li data-target="#carousel-index" data-slide-to="1"></li>\r\n        <li data-target="#carousel-index" data-slide-to="2"></li>\r\n      </ol>\r\n\r\n      <!-- Wrapper for slides -->\r\n      <div class="carousel-inner" role="listbox">\r\n        <div class="item active">\r\n          <img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/mayflower.jpg" alt="The Mayflower">\r\n          <div class="carousel-caption">\r\n            <p>The Colonial Heritage Foundation is dedicated to the preservation of the values, culture, skills and history of America\'s founding.</p>\r\n          </div>\r\n        </div>\r\n        <div class="item">\r\n          <img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/colonials.jpg" alt="Colonials">\r\n          <div class="carousel-caption">\r\n            <p>Items are available for rent as well as for sale.</p>\r\n          </div>\r\n        </div>\r\n        <div class="item">\r\n          <img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/artisan.jpg" alt="...">\r\n          <div class="carousel-caption">\r\n            <p>Custom orders can be made and filled by skilled artisans.</p>\r\n          </div>\r\n        </div>\r\n      </div>\r\n\r\n      <!-- Controls -->\r\n      <a class="left carousel-control" href="#carousel-index" role="button" data-slide="prev">\r\n        <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>\r\n        <span class="sr-only">Previous</span>\r\n      </a>\r\n      <a class="right carousel-control" href="#carousel-index" role="button" data-slide="next">\r\n        <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>\r\n        <span class="sr-only">Next</span>\r\n      </a>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"64": 58, "35": 1, "52": 3, "53": 15, "54": 15, "55": 21, "56": 21, "57": 27, "58": 27, "27": 0, "45": 3}, "filename": "C:\\Users\\Blake\\apps\\homepage\\templates/index.html", "uri": "index.html"}
__M_END_METADATA
"""

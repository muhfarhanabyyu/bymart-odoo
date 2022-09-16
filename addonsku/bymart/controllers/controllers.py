# -*- coding: utf-8 -*-
# from odoo import http


# class Bymart(http.Controller):
#     @http.route('/bymart/bymart', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bymart/bymart/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bymart.listing', {
#             'root': '/bymart/bymart',
#             'objects': http.request.env['bymart.bymart'].search([]),
#         })

#     @http.route('/bymart/bymart/objects/<model("bymart.bymart"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bymart.object', {
#             'object': obj
#         })

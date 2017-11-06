# -*- coding: utf-8 -*-
from odoo import http

# class Musicregister(http.Controller):
#     @http.route('/musicregister/musicregister/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/musicregister/musicregister/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('musicregister.listing', {
#             'root': '/musicregister/musicregister',
#             'objects': http.request.env['musicregister.musicregister'].search([]),
#         })

#     @http.route('/musicregister/musicregister/objects/<model("musicregister.musicregister"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('musicregister.object', {
#             'object': obj
#         })
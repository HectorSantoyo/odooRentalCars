# -*- coding: utf-8 -*-
from odoo import http

# class Rentalcars(http.Controller):
#     @http.route('/rentalcars/rentalcars/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rentalcars/rentalcars/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rentalcars.listing', {
#             'root': '/rentalcars/rentalcars',
#             'objects': http.request.env['rentalcars.rentalcars'].search([]),
#         })

#     @http.route('/rentalcars/rentalcars/objects/<model("rentalcars.rentalcars"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rentalcars.object', {
#             'object': obj
#         })
# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Car(models.Model):
    _name = 'rentalcars.car'
    _description = "rentalcars cars"

    model = fields.Char(string="Model", required=True)
    color = fields.Char(string="Color")
    status = fields.Selection([ ('Libre', 'Libre'),('Rentado', 'Rentado'),],'Status', default='Libre')
    year = fields.Integer(string="Year")
    client_ids = fields.Many2one('rentalcars.client',
    	ondelete='cascade', string="Client")
    	
    @api.onchange('status', 'client_ids')
    def _verify_rented_car(self):
        if self.status == 'Libre':
            self.client_ids = ''
            
            
            
class Client(models.Model):
    _name = 'rentalcars.client'
    _description = "rentalcars client"

    name = fields.Char(required=True)
    address = fields.Char()
    phone = fields.Integer(string="Phone number")
    car_id = fields.Many2one('rentalcars.car',
        ondelete='cascade', string="Car")
    

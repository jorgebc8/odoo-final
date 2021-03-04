from odoo import fields, models


class TechPhones(models.Model):
    _name = 'tech.phones'

    name = fields.Char(string="Name")
    model = fields.Char(string="model")
    os = fields.Char(string="os")
    price = fields.Char(string="price")
    color = fields.Char(string="color")
    

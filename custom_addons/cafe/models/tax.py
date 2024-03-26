from odoo import models,fields


class Tax(models.Model):
    _name = 'cafe.tax'

    name = fields.Char(string='Tax Name', required=True)
    code = fields.Char(string='Tax Code')
    percent = fields.Float(string='Percentage', required=True)

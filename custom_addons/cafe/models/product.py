from odoo import models, fields, api


class Product(models.Model):
    _name = 'cafe.product'
    _description = 'This is Product Model'

    name = fields.Char(string='Product Name', required=True)
    code = fields.Char(string='Product Code')
    image = fields.Binary(string='Product Image')
    cost_price = fields.Float(string='Cost Price', required=True)
    sale_price = fields.Float(string='Sale Price', required=True)
    gpm = fields.Float(string='Gross Profit Margin', compute='_compute_gpm', store=True)

    @api.depends('cost_price', 'sale_price')
    def _compute_gpm(self):
        for product in self:
            if product.cost_price and product.sale_price:
                product.gpm = product.sale_price - product.cost_price
            else:
                product.gpm = 0

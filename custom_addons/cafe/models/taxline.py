from odoo import models, fields, api


class SaleTaxLine(models.Model):
    _name = 'cafe.sale.tax.line'
    _description = 'This is TaxLine Model'

    tax = fields.Many2one('cafe.tax', string='Tax', required=True)
    base_price = fields.Float(string='Base Price', required=True)
    percentage = fields.Float(string='Percentage', required=True)
    tax_amount = fields.Float(string='Tax Amount', compute='_compute_tax_amount', store=True)
    sale_id = fields.Many2one('cafe.sale', string='Sale')

    @api.depends('base_price', 'percentage')
    def _compute_tax_amount(self):
        for line in self:
            line.tax_amount = (line.base_price * line.percentage) / 100

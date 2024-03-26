from odoo import fields, models, api


class SaleOrderLine(models.Model):
    _name = 'cafe.sale.order.line'

    product = fields.Many2one('cafe.product', string='Product', required=True)
    quantity = fields.Float(string='Quantity', required=True)
    price = fields.Float(string='Price', required=True)
    sub_total = fields.Float(string='Sub Total', compute='_compute_sub_total', store=True)
    taxes = fields.Many2many('cafe.tax', string='Taxes')
    tax_amount = fields.Float(string='Tax Amount', compute='_compute_tax_amount', store=True)
    total = fields.Float(string='Total', compute='_compute_total', store=True)
    sale_id = fields.Many2one('cafe.sale', string='Sale')

    @api.depends('quantity', 'price')
    def _compute_sub_total(self):
        for line in self:
            line.sub_total = line.quantity * line.price

    @api.depends('sub_total', 'taxes')
    def _compute_tax_amount(self):
        for line in self:
            tax_percentage = line.taxex.mapped('percent')
            line.tax_amount = line.sub_total * tax_percentage / 100

    @api.depends('sub_total', 'tax_amount')
    def _compute_total(self):
        for line in self:
            line.total = line.sub_total + line.tax_amount

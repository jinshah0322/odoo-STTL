from odoo import fields, models, api


class Sale(models.Model):
    _name = 'cafe.sale'

    customer = fields.Many2one('res.partner', string='Customer', required=True, readonly=True, states={'draft': [('readonly', False)]})
    date = fields.Date(string='Date', default=fields.Date.today, readonly=True, states={'draft': [('readonly', False)]})
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('canceled', 'Canceled')
    ], string='State', default='draft', required=True)
    order_line = fields.One2many('cafe.sale.order.line', 'sale_id', string='Order Line', readonly=True, states={'draft': [('readonly', False)]})
    tax_line = fields.One2many('cafe.sale.tax.line', 'sale_id', string='Tax Line', readonly=True)
    untaxed_amount = fields.Float(string='Untaxed Amount', compute='_compute_amounts', store=True, readonly=True)
    tax_amount = fields.Float(string='Tax Amount', compute='_compute_amounts', store=True, readonly=True)
    total_amount = fields.Float(string='Total Amount', compute='_compute_amounts', store=True, readonly=True)

    def action_confirm(self):
        for sale in self:
            if self.state == 'draft':
                self.state = 'confirmed'

    def action_done(self):
        for sale in self:
            if sale.state == 'confirmed':
                sale.state = 'done'

    def action_cancel(self):
        for sale in self:
            if sale.state == 'confirmed' or sale.state == 'done':
                sale.state = 'canceled'

    def action_draft(self):
        for sale in self:
            if sale.state == 'canceled':
                sale.state = 'draft'

    @api.depends('order_line.sub_total', 'tax_line.tax_amount')
    def _compute_amounts(self):
        for sale in self:
            sale.untaxed_amount = sum(line.sub_total for line in sale.order_line)
            sale.tax_amount = sum(line.tax_amount for line in sale.tax_line)
            sale.total_amount = sale.untaxed_amount + sale.tax_amount


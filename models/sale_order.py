from odoo import models, fields

# inheritance
class SaleOrder(models.Model):
    _inherit = 'sale.order'
    #
    ceren_field = fields.Char(string='TEST')
    ceren_second_field = fields.Char(string='TEST2')


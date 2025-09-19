from odoo import models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def confirm_quotations_bulk(self):
        """Confirm selected quotations"""
        for order in self:
            if order.state in ['draft', 'sent']:
                order.action_confirm()
        return True
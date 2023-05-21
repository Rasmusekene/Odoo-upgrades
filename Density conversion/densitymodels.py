from odoo import api, models, fields
class ProductTemplate(models.Model):
    _inherit = 'product.template'

    density = fields.Float('Density')
class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    volume = fields.Float('Volume')

    @api.onchange('volume')
    def _onchange_volume(self):
        if self.volume and self.product_id.density:
            self.product_qty = self.volume * self.product_id.density
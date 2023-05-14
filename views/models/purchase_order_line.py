# Copyright (C) 2017 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models
from datetime import datetime

class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    @api.model
    def _prepare_from_pos(self, purchase_order, order_line_data):
        ProductProduct = self.env["product.product"]
        product = ProductProduct.browse(order_line_data["product_id"])
        return {
            "order_id": purchase_order.id,
            "product_id": order_line_data["product_id"],
            "name": product.name,
            "date_planned": datetime.today(),
            "product_qty": order_line_data["qty"],
            #PoS do not handle uom so put a random number
            "product_uom": 1,
#            "discount": order_line_data["discount"],
            "price_unit": order_line_data["price_unit"],
            "taxes_id": order_line_data["tax_ids"],
        }

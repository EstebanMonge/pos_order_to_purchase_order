# Copyright (C) 2017 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging
from odoo import _, api, models
from datetime import datetime

_logger = logging.getLogger(__name__)

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @api.model
    def _prepare_from_pos(self, order_data):
        _logger.error("Caca")
        _logger.error(order_data)
        PosSession = self.env["pos.session"]
        session = PosSession.browse(order_data["pos_session_id"])
        return {
            "partner_id": order_data["partner_id"],
            "origin": _("Point of Sale %s") % (session.name),
#            "client_order_ref": order_data["name"],
            "user_id": order_data["user_id"],
#            "pricelist_id": order_data["pricelist_id"],
            "fiscal_position_id": order_data["fiscal_position_id"],
        }

    @api.model
    def create_order_from_pos(self, order_data, action):
        PurchaseOrderLine = self.env["purchase.order.line"]

        # Create Draft Purchase order
        order_vals = self._prepare_from_pos(order_data)
        purchase_order = self.create(order_vals.copy())
        purchase_order.onchange_partner_id()
        # we rewrite data, because onchange could alter some
        # custom data (like pricelist)
        purchase_order.write(order_vals)

        # create Purchase order lines
        for order_line_data in order_data["lines"]:
            # Create Purchase order lines
            order_line_vals = PurchaseOrderLine._prepare_from_pos(
                purchase_order, order_line_data[2])
            purchase_order_line = PurchaseOrderLine.create(
                order_line_vals.copy())
            #purchase_order_line.product_id_change()
            # we rewrite data, because onchange could alter some
            # data (like quantity, or price)
            purchase_order_line.write(order_line_vals)

        # Confirm Purchase Order
        if action in ["confirmed", "delivered"]:
            purchase_order.write({'state': 'purchase', 'date_approve': datetime.today()})

        # mark picking as delivered
        if action == "delivered":
            # Mark all moves are delivered
            for move in purchase_order.mapped(
                    "picking_ids.move_ids_without_package"):
                move.quantity_done = move.product_uom_qty
            purchase_order.mapped("picking_ids").button_validate()

        return {
            "purchase_order_id": purchase_order.id,
        }

# Copyright (C) 2017 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class PosConfig(models.Model):
    _inherit = "pos.config"

    iface_create_purchase_order = fields.Boolean(
        string="Create Purchase Orders",
        compute="_compute_iface_create_purchase_order",
        store=True)

    iface_create_draft_purchase_order = fields.Boolean(
        string="Create Draft Purchase Orders",
        default=True,
        help="If checked, the cashier will have the possibility to create"
        " a draft Purchase Order, based on the current draft PoS Order.",
    )

    iface_create_confirmed_purchase_order = fields.Boolean(
        string="Create Confirmed Purchase Orders",
        default=True,
        help="If checked, the cashier will have the possibility to create"
        " a confirmed Purchase Order, based on the current draft PoS Order.",
    )

    iface_create_delivered_purchase_order = fields.Boolean(
        string="Create Delivered Purchase Orders",
        default=True,
        help="If checked, the cashier will have the possibility to create"
        " a confirmed Purchase Order, based on the current draft PoS Order.\n"
        " the according picking will be marked as delivered. Only invoices"
        " process will be possible.",
    )

    @api.depends(
        "iface_create_draft_purchase_order",
        "iface_create_confirmed_purchase_order",
        "iface_create_delivered_purchase_order",
    )
    def _compute_iface_create_purchase_order(self):
        for config in self:
            config.iface_create_purchase_order = any([
                config.iface_create_draft_purchase_order,
                config.iface_create_confirmed_purchase_order,
                config.iface_create_delivered_purchase_order,
            ])

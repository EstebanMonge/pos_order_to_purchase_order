# Copyright (C) 2017 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "PoS Order To Purchase Order",
    "version": "12.0.1.0.1",
    "author": "GRAP,Odoo Community Association (OCA),Esteban Monge",
    "category": "Point Of Sale",
    "license": "AGPL-3",
    "depends": ["point_of_sale","purchase"],
    "installable" : True,
    "maintainers": ["estebanmonge"],
    "development_status": "Production/Stable",
    "website": "https://github.com/OCA/pos",
    "data": [
        "views/view_pos_config.xml",
#        "views/assets.xml",
    ],
    "assets": {
        "point_of_sale.assets": [
            "pos_order_to_purchase_order/static/src/js/PosOrderToPurchaseOrderButton.js",
            "pos_order_to_purchase_order/static/src/js/PosOrderToPurchaseOrderPopup.js",
        ],
    "web.assets_qweb": [
        "pos_order_to_purchase_order/static/src/xml/PosOrderToPurchaseOrderButton.xml",
        "pos_order_to_purchase_order/static/src/xml/PosOrderToPurchaseOrderPopup.xml",
     ],
    },
}

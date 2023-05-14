odoo.define("pos_order_to_purchase_order.PosOrderToPurchaseOrderPopup", function (require) {
    "use strict";

    const {useState} = owl.hooks;
    const AbstractAwaitablePopup = require("point_of_sale.AbstractAwaitablePopup");
    const Registries = require("point_of_sale.Registries");
    var rpc = require('web.rpc');

    class PosOrderToPurchaseOrderPopup extends AbstractAwaitablePopup {
        constructor() {
            super(...arguments);
        }
        click_create_draft_purchase_order(orderJson) {
           rpc.query({
               model: 'purchase.order',
               method: 'create_order_from_pos',
               args: [this.props.orderJson, "draft"],
           }).then(function (result) {
               alert("Order created");
               //self.hook_create_purchase_order_success(result);
           }).catch(function (error, event) {
               //self.hook_create_purchase_order_error(error, event);
               alert("Something goes wrong. Order not created");
           });
           //I was forced to remove the client and order lines instead removeo rder
           this.props.order.set_client(null);
           this.props.order.remove_orderline(this.props.order_lines);
           this.trigger("close-popup");
        }
        async click_create_confirmed_purchase_order() {
           alert("confirmed");
           rpc.query({
               model: 'purchase.order',
               method: 'create_order_from_pos',
               args: [this.props.order, "purchase"],
           }).then(function (result) {
               alert("Order created");
               //self.hook_create_purchase_order_success(result);
           }).catch(function (error, event) {
               //self.hook_create_purchase_order_error(error, event);
               alert("Something goes wrong. Order not created");
           });
           this.props.order.set_client(null);
           this.props.order.remove_orderline(this.props.order_lines);
           this.trigger("close-popup");
        }
        async click_create_delivered_purchase_order() {
           alert("delivered");
           rpc.query({
               model: 'purchase.order',
               method: 'create_order_from_pos',
               args: [this.props.order, "done"],
           }).then(function (result) {
               alert("Order created");
               //self.hook_create_purchase_order_success(result);
           }).catch(function (error, event) {
               //self.hook_create_purchase_order_error(error, event);
               alert("Something goes wrong. Order not created");
           });
           this.props.order.set_client(null);
           this.props.order.remove_orderline(this.props.order_lines);
           this.trigger("close-popup");
        }
    }
    PosOrderToPurchaseOrderPopup.template = "PosOrderToPurchaseOrderPopup";
    PosOrderToPurchaseOrderPopup.defaultProps = {
        cancelText: "Cancel",
        array: [],
    };

    Registries.Component.add(PosOrderToPurchaseOrderPopup);

    return PosOrderToPurchaseOrderPopup;
});

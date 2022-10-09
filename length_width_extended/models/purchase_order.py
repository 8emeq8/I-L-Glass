# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    unit_length = fields.Float(string='Length', digits='Product Unit of Measure')
    unit_width = fields.Float(string='Width', digits='Product Unit of Measure')
    total_meter = fields.Float(string='Meter', digits='Product Unit of Measure', compute='_compute_total_meter')
    unit_qty = fields.Float(string='Units', digits='Product Unit of Measure')

    @api.depends('unit_length', 'unit_width')
    def _compute_total_meter(self):
        for rec in self:
            rec.total_meter = rec.unit_length * rec.unit_width

    @api.onchange('unit_length', 'unit_width', 'unit_qty')
    def _set_product_qty(self):
        for rec in self:
            rec.product_qty = rec.total_meter * rec.unit_qty

    def _prepare_account_move_line(self, move=False):
        res = super()._prepare_account_move_line(move)
        res.update({
            'unit_length': self.unit_length,
            'unit_width': self.unit_width,
            'total_meter': self.total_meter,
            'unit_qty': self.unit_qty,
        })
        return res

    def _prepare_stock_move_vals(self, picking, price_unit, product_uom_qty, product_uom):
        res = super(PurchaseOrderLine, self)._prepare_stock_move_vals(picking, price_unit, product_uom_qty, product_uom)
        res.update({
            'unit_length': self.unit_length,
            'unit_width': self.unit_width,
            'total_meter': self.total_meter,
            'unit_qty': self.unit_qty,
        })
        return res


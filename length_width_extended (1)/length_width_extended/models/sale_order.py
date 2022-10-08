# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    unit_length = fields.Float(string='Length')
    unit_width = fields.Float(string='Width')
    total_meter = fields.Float(string='Meter', compute='_compute_total_meter')
    unit_qty = fields.Float(string='Units')

    @api.depends('unit_length', 'unit_width')
    def _compute_total_meter(self):
        for rec in self:
            rec.total_meter = rec.unit_length * rec.unit_width

    @api.onchange('unit_length', 'unit_width', 'unit_qty')
    def _set_product_uom_qty(self):
        for rec in self:
            rec.product_uom_qty = rec.total_meter * rec.unit_qty

    def _prepare_invoice_line(self, **optional_values):
        res = super(SaleOrderLine, self)._prepare_invoice_line(**optional_values)
        res.update({
            'unit_length': self.unit_length,
            'unit_width': self.unit_width,
            'total_meter': self.total_meter,
            'unit_qty': self.unit_qty,
        })
        return res






# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class StockMove(models.Model):
    _inherit = 'stock.move'

    unit_length = fields.Float(string='Length', digits='Product Unit of Measure')
    unit_width = fields.Float(string='Width', digits='Product Unit of Measure')
    total_meter = fields.Float(string='Meter', digits='Product Unit of Measure', compute='_compute_total_meter')
    unit_qty = fields.Float(string='Units', digits='Product Unit of Measure')

    @api.model
    def create(self, vals):
        if vals.get('sale_line_id'):
            sol = self.env['sale.order.line'].browse(vals.get('sale_line_id'))
            vals.update({
                'unit_length': sol.unit_length,
                'unit_width': sol.unit_width,
                'total_meter': sol.total_meter,
                'unit_qty': sol.unit_qty,
            })
        return super(StockMove, self).create(vals)

    @api.depends('unit_length', 'unit_width')
    def _compute_total_meter(self):
        for rec in self:
            rec.total_meter = rec.unit_length * rec.unit_width

    @api.onchange('unit_length', 'unit_width', 'unit_qty')
    def _set_product_uom_quantity(self):
        for rec in self:
            rec.product_uom_qty = rec.total_meter * rec.unit_qty


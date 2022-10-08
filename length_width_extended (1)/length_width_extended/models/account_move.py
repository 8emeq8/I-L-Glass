# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    unit_length = fields.Float(string='Length')
    unit_width = fields.Float(string='Width')
    total_meter = fields.Float(string='Meter', compute='_compute_total_meter')
    unit_qty = fields.Float(string='Units')

    @api.depends('unit_length', 'unit_width')
    def _compute_total_meter(self):
        for rec in self:
            rec.total_meter = rec.unit_length * rec.unit_width

    @api.onchange('unit_length', 'unit_width', 'unit_qty')
    def _set_quantity(self):
        for rec in self:
            rec.quantity = rec.total_meter * rec.unit_qty


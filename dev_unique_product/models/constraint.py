# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://www.devintellecs.com>).
#
#    For Module Support : devintelle@gmail.com  or Skype : devintelle 
#
##############################################################################


from odoo import api, models, fields, _
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    
    _inherit = "sale.order"
    
    allow_duplicate = fields.Boolean('Allow Duplicates', default=False, copy=False)

    def copy(self, default=None):
        self.ensure_one()
        default = dict(default or {})
        res=super(SaleOrder,self).copy(default)
        pro=[]
        for line in res.order_line:
            if line.product_id.id not in pro:
                pro.append(line.product_id.id)
            else:
                raise ValidationError(_('Product should be Unique per Sale Order !'))
        return res
    
    def _prepare_invoice(self):
        res= super(SaleOrder,self)._prepare_invoice()
        if self.allow_duplicate and res:
            res.update({
                'allow_duplicate':True,
            })
        return res
    

    
class SaleOrderLine(models.Model):
    
    _inherit = "sale.order.line"
    
    @api.constrains('product_id', 'order_id')
    def _check_unique_constraint(self):
        if not self.order_id.allow_duplicate:
            if len(self.search([('order_id', '=', self.order_id.id),('product_id', '=', self.product_id.id)])) > 1:
                raise ValidationError("Product %s must be unique per Sale Order"% (self.product_id.name,))

class AccountInvoice(models.Model):
    
    _inherit = "account.move"
#    
#    
    allow_duplicate = fields.Boolean('Allow Duplicates', default=False, copy=False)
#    
    @api.model
    def default_get(self,vals):
        res = super(AccountInvoice,self).default_get(vals)
        if res.get('purchase_id'):
            purchase = self.env['purchase.order'].browse(res.get('purchase_id'))
            if purchase.allow_duplicate:
                res.update({
                    'allow_duplicate':purchase.allow_duplicate,
                })
                
        return res
    
    @api.model
    def create(self,vals):
        inv_id = super(AccountInvoice,self).create(vals)
        if self._context.get('default_purchase_id'):
            purchase_pool= self.env['purchase.order']
            purchase_id = purchase_pool.browse(self._context.get('default_purchase_id'))
            if purchase_id.allow_duplicate and inv_id:  
                inv_id.write({
                    'allow_duplicate':purchase_id.allow_duplicate,
                })
            
        return inv_id
        
    
    def copy(self, default=None):
        self.ensure_one()
        default = dict(default or {})
        res=super(AccountInvoice,self).copy(default)
        pro=[]
        for line in res.invoice_line_ids:
            if line.product_id.id not in pro:
                pro.append(line.product_id.id)
            else:
                raise ValidationError(_('Product should be Unique per Invoice !'))
        return res
        
    
class AccountInvoiceLine(models.Model):
    
    _inherit = "account.move.line"

    @api.constrains('product_id', 'move_id')
    def _check_unique_constraint(self):
        for product in self.product_id:
            if len(self.search([('move_id', '=', self.move_id.id),('product_id', '=', product.id),('exclude_from_invoice_tab', '=', False)])) > 1:
                if not self.move_id.allow_duplicate:
                    raise ValidationError("Product %s must be unique per Invoice "%(product.name,))
    
class PurchaseOrder(models.Model):
    
    _inherit = "purchase.order"
    
    allow_duplicate = fields.Boolean('Allow Duplicates', default=False, copy=False)
    
    
    def copy(self, default=None):
        self.ensure_one()
        default = dict(default or {})
        res=super(PurchaseOrder,self).copy(default)
        pro=[]
        for line in res.order_line:
            if line.product_id.id not in pro:
                pro.append(line.product_id.id)
            else:
                raise ValidationError(_('Product should be Unique per Purchase Order !'))
        return res
    

class PurchaseOrderLine(models.Model):
    
    _inherit = "purchase.order.line"

    @api.constrains('product_id', 'order_id')
    def _check_unique_constraint(self):
        for product in self.product_id:
            if len(self.search([('order_id', '=', self.order_id.id),('product_id', '=', product.id)])) > 1:
                if not self.order_id.allow_duplicate:
                    raise ValidationError("Product %s must be unique per Purchase Order" %(product.name,))

    
    

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:


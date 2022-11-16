# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://www.devintellecs.com>).
#
#    For Module Support : devintelle@gmail.com  or Skype : devintelle 
#
##############################################################################
{
    'name': 'Unique Product on Sale,Purchase and Invoice,Uniq Sale Product, uniq Purchase product, Uniq Invoice product',
    'version': '15.0.1.0',
    'sequence':1,
    'category': 'Sales',
    'summary': 'odoo app will raise a warning when same Product repeated on Sale,Purchase and Invoice lines, Uniq Sale Product, uniq purchase product, uniq invoice product, uniq sales product',
    'description': """
       odoo app will raise a warning when same Product repeated on Sale,Purchase and Invoice lines.
Unique Product on Sale,Purchase and Invoice
Odoo Unique Product on Sale,Purchase and Invoice
Unique product on sale 
Odoo unique product on sale 
Unique product on purchase 
Odoo unique product on purchase 
Unique product on invoice 
Odoo unique product on invoice 
Manage Unique product on sale 
Odoo manage unique product on sale 
Manage Unique product on purchase 
Odoo manage unique product on purchase 
Manage Unique product on invoice 
Odoo manage unique product on invoice 
Print Unique product on sale 
Odoo print unique product on sale 
Print Unique product on purchase 
Odoo print unique product on purchase 
Print Unique product on invoice 
Odoo print unique product on invoice 
raise a warning when same Product repeated on Sale,Purchase and Invoice lines
odoo raise a warning when same Product repeated on Sale,Purchase and Invoice lines
Raise a warning when same Product repeated on Sale Order
Odoo Raise a warning when same Product repeated on Sale Order
Raise a warning when same Product repeated on Purchase Order
Odoo Raise a warning when same Product repeated on Purchase Order
Raise a warning when same Product repeated on Invoice
Odoo Raise a warning when same Product repeated on Invoice
Unique product reference code 
Odoo unique product reference code 
Manage Unique product reference code 
Odoo manage Unique product reference code 
Product reference code 
Odoo product reference code 
Manage product reference code 
Odoo manage product reference code 
odoo app will help to set Internal Reference of product must be unique
Product's Internal Reference will be unique for each product
Odoo Product's Internal Reference will be unique for each product
Product code uniq Warning Message
Odoo Product code uniq Warning Message
Manage product code 
Odoo manage product code 
Manage unique product code 
Odoo manage unique product code 
    """,
    'depends': ['sale', 'purchase', 'stock', 'account'],
    'data': [
        'views/sale_view.xml',
        'views/account_invoice_view.xml',
        'views/purchase_order_view.xml',
    ],
    'demo': [],
    'test': [],
    'css': [],
    'qweb': [],
    'js': [],
    'images': ['images/main_screenshot.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    
    # author and support Details =============#
    'author': 'DevIntelle Consulting Service Pvt.Ltd',
    'website': 'http://www.devintellecs.com',    
    'maintainer': 'DevIntelle Consulting Service Pvt.Ltd', 
    'support': 'devintelle@gmail.com',
    'price':10.0,
    'currency':'EUR',
    #'live_test_url':'https://youtu.be/A5kEBboAh_k',
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

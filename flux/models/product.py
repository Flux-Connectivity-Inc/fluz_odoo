# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    default_code = fields.Char(default=lambda self: self.env['ir.sequence'].next_by_code('product.product.sku'))

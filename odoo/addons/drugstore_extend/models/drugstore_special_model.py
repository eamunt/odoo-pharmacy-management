from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class Drugstore_Special(models.Model):
    _name = "drugstore.special" # new model.
    _inherit = "my.drugstore" # inherit field and methods from my.drugstore
    _description = "drugstore.special"

    # add new fields
    side_effect = fields.Boolean("Side effect", default = False)
    drowsy = fields.Boolean("Drowsy", default = False)
    color = fields.Char("Color")
    country = fields.Many2one('res.country', string="Drug's country")
    product_ids = fields.Many2many(comodel_name='product.product', 
                                string="Related Products", 
                                # relation table
                                relation='drug_special_product_rel',
                                column1='col_drug_id',
                                column2='col_product_id')
    basic_price = fields.Float("Basic price", default = 3)
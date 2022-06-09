from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class Product_Drugs(models.Model):
    _name = "product.drugs" # new model.
    _inherits = {'drugstore.special': 'drug_id'} # Khóa ngoại trỏ đến model drugstore.special là drug_id.
    _description = "product.drugs"

    # define drug_id
    drug_id = fields.Many2one(
        'drugstore.special', 'Drugstore special',
        auto_join = True, index = True, ondelete='cascade', required=True
    )

    storage_environment = fields.Selection([
        ('low','<20oC'), 
        ('medium','<30oC and >20oC'), 
        ('high','>30oC')
    ], string='Storage environment', default='medium')

    location = fields.Selection([
        ('A', 'Zone A'),
        ('B', 'Zone B'),
        ('C', 'Zone C'),
        ('D', 'Zone D'),
    ], string='Location', default='A')

    bonus_price = fields.Float("Bonus price", default = 0)
    final_price = fields.Float("Final price", compute='_compute_final_price') 

    def _compute_final_price(self):
        for record in self:
            record.final_price = record.basic_price + record.bonus_price

    product_ids = fields.Many2many(comodel_name='product.product', 
                                string="Related Products", 
                                relation='product_drugs_rel',
                                column1='col_drug_id',
                                column2='col_product_id')

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
import json

class Product_Drugs(models.Model):
    _name = "product.drugs" # new model.
    _inherits = {'drugstore.special': 'drug_id'} # Khóa ngoại trỏ đến model drugstore.special là drug_id.
    _description = "product.drugs"

    # define drug_id
    # index: yêu cầu Odoo tạo index trong database
    # ondelete='cascade':tự động xóa dữ liệu ở bảng con khi xóa dữ liệu ở bảng cha
        # referential for foreign key
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
    final_price = fields.Float("Final price", compute='_compute_final_price', store=True) 


    @api.depends('basic_price', 'bonus_price')
    def _compute_final_price(self):
        for record in self:
            record.final_price = record.basic_price + record.bonus_price

    product_ids = fields.Many2many(comodel_name='product.product', 
                                string="Related Products", 
                                relation='product_drugs_rel',
                                column1='col_drug_id',
                                column2='col_product_id')



    @api.onchange('basic_price')
    def _check_basic_price(self):
        if self.basic_price <= 2:
            raise ValidationError("Basic price need more than 2 !")

    drug_code = fields.Char("Drug code")

    @api.model
    def create(self, vals):
        #print("Successfull")
        c11 = ""
        c22 = ""
        c1 = vals.get('name')
        c2 = vals.get('color')
        if c1 or c2:
            c11 = ""
            c22 = ""
            if len(str(c1)) >=3:
                c11 += c1[0:3]
            else:
                c11 += c1[0:len(c1)]
            if len(str(c2)) >=3:
                c22 += c2[0:3]
            else:
                c22 += c2[0:len(c2)]
            vals['drug_code'] = c11 +"-"+ c22

        return super(Product_Drugs, self).create(vals)
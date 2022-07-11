# đây là file model, sẽ chứa thông tin cần lưu trữ các thuộc tính nào cho thú cưng.


# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class MyDrugstore(models.Model):
    _name = "my.drugstore"
    _description = "My drugstore model"

    name = fields.Char('Drug name', required=True)
    shortname = fields.Char('Short name')
    description = fields.Text('Description')
    exp = fields.Integer('EXPry (month)', default=1)
    weight = fields.Float('Weight (gram)')
    import_date = fields.Date('Import date', required=True)
    type = fields.Selection([('tpbs', 'supplements'),('thuoc', 'Drug'),('dcyt',"Medical equipment")]
    , string='Type', default='thuoc')
    # help: hiển thị trợ giúp trong giao diện người dùng.
    drug_image = fields.Binary("Drug Image", attachment=True, help="Drug Image")    
    cus_id = fields.Many2one('res.partner', string='Customer')
    product_ids = fields.Many2many(comodel_name='product.product', 
                                string="Related Products", 
                                relation='drug_product_rel',
                                column1='col_drug_id',
                                column2='col_product_id')

    lname = fields.Char('Lname', compute='get_name')

    @api.model
    def get_name(self):
        for i in self:
            i.lname = "pôppo"

    def printd(self):
        lname = 'toto'

    # @api.one
    # @api.depends('name')
    # def get_name(self):
    #     reg = []
    #     reg.append(self.name)
    #     raise ValidationError(reg)


    
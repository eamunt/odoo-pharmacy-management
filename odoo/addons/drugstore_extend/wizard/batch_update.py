# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

import logging
_logger = logging.getLogger(__name__)

class BatchUpdateWizard(models.TransientModel):
    _name = "product.drugs.batch.update.wizard"
    _description = "product.drugs.batch.update.wizard"


    name = fields.Char('Drug name')
    cus_id = fields.Many2one('res.partner', string='Customer')

    exp = fields.Integer('EXPry (month)', default=1)
    weight = fields.Float('Weight (gram)')
    import_date = fields.Date('Import date')
    type = fields.Selection([('tpbs', 'supplements'),('thuoc', 'Drug'),('dcyt',"Medical equipment")]
    , string='Type', default='thuoc')
    # help: hiển thị trợ giúp trong giao diện người dùng.
    drug_image = fields.Binary("Drug Image", attachment=True, help="Drug Image")  

    side_effect = fields.Boolean("Side effect", default = True)
    drowsy = fields.Boolean("Drowsy", default = True)
    color = fields.Char("Color")
    country = fields.Many2one('res.country', string="Drug's country")
    basic_price = fields.Float("Basic price", default = 0)

    shortname = fields.Char('Short name')
    description = fields.Text('Description')

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


    def multi_update(self):
        # id của các record đc chọn (tick) trong bảng product.drugs sẽ đc truyền vào context
        # truy xuất bằng id = ....
        ids = self.env.context['active_ids']
        my_drugs = self.env['product.drugs'].browse(ids)
        new_edit = {}

        if self.name:
            new_edit['name'] = self.name
        if self.cus_id:
            new_edit['cus_id'] = self.cus_id

        # exp > 1
        if self.exp > 1:
            new_edit['exp'] = self.exp
        if self.weight:
            new_edit['weight'] = self.weight
        if self.import_date:
            new_edit['import_date'] = self.import_date
        if self.type:
            new_edit['type'] = self.type
        if self.drug_image:
            new_edit['drug_image'] = self.drug_image
        
        # side_effect
        if self.side_effect == False:
            new_edit['side_effect'] = self.side_effect
        else:
            new_edit['side_effect'] = self.side_effect

        # drowsy
        if self.drowsy == False:
            new_edit['drowsy'] = self.drowsy
        else:
            new_edit['drowsy'] = self.drowsy

        if self.color:
            new_edit['color'] = self.color
        if self.country:
            new_edit['country'] = self.country
        if self.basic_price > 0:
            new_edit['basic_price'] = self.basic_price
        if self.shortname:
            new_edit['shortname'] = self.shortname
        if self.description:
            new_edit['description'] = self.description
        if self.storage_environment:
            new_edit['storage_environment'] = self.storage_environment
        if self.location:
            new_edit['location'] = self.location
        if self.bonus_price:
            new_edit['bonus_price'] = self.bonus_price

        my_drugs.write(new_edit)
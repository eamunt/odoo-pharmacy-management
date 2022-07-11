

# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
from datetime import datetime
class DonThuoc(models.Model):
    _name = "don.thuoc"
    _inherits = {'benh.nhan': 'bn_id'}
    _description = "don.thuoc"

    bn_id = fields.Many2one(
        'benh.nhan', 'Bệnh nhân',
        auto_join = True, index= True, ondelete='cascade', required=True
    )

    ma_donthuoc = fields.Char('Mã đơn thuốc')
    ten_bacsi = fields.Many2one('bac.si', String = "Tên bác sĩ")
    ngay = fields.Date("Ngày", default=datetime.today())

    chan_doan = fields.Text("Chẩn đoán")
    thuoc_ids = fields.Many2many('line.thuoc', string = 'Thuốc')


    @api.model
    def create(self, vals):
        #print("Successfull")
        c11 = ""
        c33 = ""
        c44 = ""
        c1 = vals.get('name')
        c3 = vals.get('chan_doan')
        c4 = vals.get('ngay_sinh')
        if c1 or c2 or c3 or c4:
            c11 = ""
            c22 = ""
            c33 = ""
            c44 = ""
            if len(str(c1)) >=3:
                c11 += c1[len(str(c1))-3:len(str(c1))]
            else:
                c11 += c1[0:len(c1)]
            
            
            if len(str(c3)) >=4:
                c33 += c3[len(str(c3))-4:len(str(c3))]
            else:
                c33 += c3[0:len(c3)]
            
            c44 += str(c4)
            vals['ma_donthuoc'] = c11 +"_"+ c33 + "-" + c44

        return super(DonThuoc, self).create(vals)
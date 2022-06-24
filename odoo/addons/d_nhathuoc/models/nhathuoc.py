# đây là file model, sẽ chứa thông tin cần lưu trữ các thuộc tính nào cho thú cưng.


# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class NhaThuoc(models.Model):
    _name = "nha.thuoc"
    _description = "nha.thuoc"

    name = fields.Char('Tên thuốc', required=True)
    ma_thuoc = fields.Char(string='Mã thuốc')
    cach_dung = fields.Selection([
        ('uong', 'Uống'),
        ('tiem', 'Tiêm'),
        ('ngoai_da', 'Ngoài da'),
        ('khac', 'Khác'),
    ], string='Cách dùng', default='uong')
    so_giay_dangky = fields.Char('Số giấy đăng ký')
    hoat_chat = fields.Text('Hoạt chất')
    nong_do = fields.Float('Nồng độ', default = 0)
    # import_date = fields.Date('Import date', required=True)
    quy_cach_dong_goi = fields.Text("Quy cách đóng gói")
    hang_sx = fields.Char("Hãng sản xuất", required=True)
    nha_sx = fields.Char("Nhà sản xuất")
    don_gia = fields.Float("Đơn giá (viên)")
    don_gia_hop = fields.Float("Đơn giá (hộp)")
    lieu_dung = fields.Integer("Liều dùng/ngày")
    anh_thuoc = fields.Binary("Hình ảnh", attachment=True, help="Hình ảnh") 

    @api.model
    def create(self, vals):
        #print("Successfull")
        c11 = ""
        c22 = ""
        c1 = vals.get('name')
        c2 = vals.get('hang_sx')
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
            vals['ma_thuoc'] = c11 +"-"+ c22

        return super(NhaThuoc, self).create(vals)
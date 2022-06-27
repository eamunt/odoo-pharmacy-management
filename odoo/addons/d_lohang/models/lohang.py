

# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
from datetime import datetime


class LoHang(models.Model):
    _name = "lo.hang"
    _description = "lo.hang"

    so_phieu = fields.Char('Số phiếu')
    ngay_nhap = fields.Date(string='Ngày nhập', default=datetime.today())
    nha_cung_cap = fields.Char("Nhà cung cấp", required=True)
    dia_chi = fields.Char("Địa chỉ", required=True)
    nguoi_nhap = fields.Many2one('res.users', string='Người nhập')
    nguoi_giaohang = fields.Char("Người giao hàng")
    ghi_chu = fields.Text("Ghi chú")

    hang = fields.Many2many('hanghoa.nhap', string = 'Hàng hóa nhập')

    tien_hang = fields.Float("Tiền hàng", compute='_compute_final_price', store=True) 
    thanh_toan = fields.Float("Thanh toán", store=True)

    @api.depends('hang.thanh_tien')
    def _compute_final_price(self):
        for record in self:
            t=0
            for i in record.hang:
                t += i.thanh_tien
            record.tien_hang = t

    hinh_thuc_tt = fields.Selection([
        ('t_mat', 'T.Mặt'),
        ('ck', 'CK'),
        ('the', 'Thẻ'),
    ], string='Hình thức TT', default='t_mat')

    tong_giam_gia = fields.Float("Tổng giảm giá", compute='_compute_final_price2', store=True)
    con_no = fields.Float("Còn nợ", compute='_compute_final_price1', store=True)

    @api.depends('tien_hang', 'thanh_toan')
    def _compute_final_price1(self):
        for record in self:
            record.con_no = record.tien_hang - record.thanh_toan

    @api.depends('tien_hang', 'hang.chiet_khau')
    def _compute_final_price2(self):
        t = 0
        for record in self:
            for i in record.hang:
                t += (i.so_luong*i.dongia_nhap)*(i.chiet_khau/100)
            record.tong_giam_gia = t

    @api.model
    def create(self, vals):
        #print("Successfull")
        c11 = ""
        c22 = ""
        c33 = ""
        c1 = vals.get('nha_cung_cap')
        c2 = vals.get('dia_chi')
        c3 = vals.get('ngay_nhap')
        if c1 or c2 or c3:
            c11 = ""
            c22 = ""
            c33 = ""
            if len(str(c1)) >=7:
                c11 += c1[len(str(c1))-7:len(str(c1))]
            else:
                c11 += c1[0:len(c1)]
                        
            if len(str(c2)) >=5:
                c22 += c2[len(str(c2))-5:len(str(c2))]
            else:
                c22 += c2[0:len(c2)]
            
            c33 += str(c3)
            vals['so_phieu'] = c11 +"-"+ c22  +"_"+ c33

        return super(LoHang, self).create(vals)
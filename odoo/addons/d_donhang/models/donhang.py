from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
import json

class DonHang(models.Model):
    _name = "don.hang" # new model.
    _inherits = {'don.thuoc': 'dh_id'} # Khóa ngoại trỏ đến model don.thuoc là dh_id.
    _description = "don.hang"

    # define drug_id
    # index: yêu cầu Odoo tạo index trong database
    # ondelete='cascade':tự động xóa dữ liệu ở bảng con khi xóa dữ liệu ở bảng cha
        # referential for foreign key
    dh_id = fields.Many2one(
        'don.thuoc', 'Đơn thuốc',
        auto_join = True, index = True, ondelete='cascade', required=True
    )

    phan_tram_giam_gia = fields.Float("Giảm giá (%)", default=0)
    tong_gia = fields.Float("Tổng", compute='_compute_final_price') 

    @api.depends('phan_tram_giam_gia')
    def _compute_final_price(self):
        for record in self:
            for i in record.thuoc_ids:
                record.tong_gia += i.tong_line 
        record.tong_gia = record.tong_gia - record.tong_gia*(record.phan_tram_giam_gia/100)

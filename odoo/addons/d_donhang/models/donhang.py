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

    phan_tram_giam_gia = fields.Float("Phần trăm giảm giá", default=0)
    tong_gia = fields.Float("Tổng", compute='_compute_final_price', store=True) 


    @api.depends('don_gia', 'phan_tram_giam_gia')
    def _compute_final_price(self):
        tong_gia_t = 0
        for record in self:
            tong_gia_t += record.thuoc.don_gia
        record.tong_gia = tong_gia_t - tong_gia_t*record.phan_tram_giam_gia


    @api.onchange('don_gia')
    def _check_basic_price(self):
        if self.don_gia < 0:
            raise ValidationError("Đơn giá không được âm!")
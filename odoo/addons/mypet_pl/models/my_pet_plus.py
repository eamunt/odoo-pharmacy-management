from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class MyPetPlus(models.Model):
    _name = "my.pet"
    _inherit = 'my.pet'
    _description = "My Pet Plus model: extend mypet model"

    # add new field: toy field
    toy = fields.Char("Pet's Toy", required = False)

    # modify age field: defaule age = 1 up to 2
    age = fields.Integer("Pet Age", default = 2)

    # add more selection for gender
    gender = fields.Selection(selection_add=[('gioitinh3', 'GioiTinh3')])

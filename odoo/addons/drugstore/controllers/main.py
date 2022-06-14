import odoo
import logging
import json
_logger = logging.getLogger(__name__)

class MyDrugstoreAPI(odoo.http.Controller):
    # đường dẫn đến method sẽ đón nhận xử lý.
    @odoo.http.route('/foo', auth='public')
    def foo_handler(self):
        return "Welcome to 'foo' API!"
    
    # bar API trả về dạng chuỗi json, để client có thể parse và xử lý ở frontend.
    @odoo.http.route('/bar', auth='public')
    def bar_handler(self):
        return json.dumps({
            "content": "Welcome to 'bar' API!"
        })

    # API đọc dữ liệu từ model
    @odoo.http.route(['/drugstore/<dbname>/<id>'], type='http', auth="none", sitemap=False, cors='*', csrf=False)
    def drug_handler(self, dbname, id, **kw):
        model_name = "my.drugstore"
        try:
            registry = odoo.modules.registry.Registry(dbname)
            with odoo.api.Environment.manage(), registry.cursor() as cr:
                env = odoo.api.Environment(cr, odoo.SUPERUSER_ID, {})
                rec = env[model_name].search([('id', '=', int(id))], limit=1)
                response = {
                    "status": "ok",
                    "content": {
                        "name": rec.name,
                        "shortname": rec.shortname,
                        "description": rec.description,
                        "exp": rec.exp,
                        "weight": rec.weight,
                        "import_date": rec.import_date.strftime('%d/%m/%Y'),
                        "type": rec.type,
                        "product_ids": rec.product_ids.display_name
                    }
                }
        except Exception:
            response = {
                "status": "error",
                "content": "not found"
            }
        return json.dumps(response)
        
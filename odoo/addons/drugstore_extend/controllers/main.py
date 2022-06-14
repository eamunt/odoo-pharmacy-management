import odoo
import logging
import json
_logger = logging.getLogger(__name__)

class MyDrugstoreAPIInherit(odoo.addons.drugstore.controllers.main.MyDrugstoreAPI):
    # không đặc tả tham số trong route => sẽ sử dụng tham số gốc
    @odoo.http.route()
    def foo_handler(self):
        return "Welcome to 'foo' inherit"
    
    # override vào tham số gốc
    @odoo.http.route('/bar2')
    def bar_handler(self):
        return json.dumps({
            "content": "Welcome to 'bar' inherit"
        })

    @odoo.http.route()
    def drug_handler(self, dbname, id, **kw):
        _logger.warning("drug handler called")
        print("hahahha")
        # call phương thức gốc trong class cha (superclass)
        result = super(MyDrugstoreAPIInherit, self).drug_handler(dbname, id)
        _logger.warning("post processing...")
        return result
    
    # API đọc dữ liệu từ model
    @odoo.http.route(['/drugstore_delegation/<dbname>/<id>'], type='http', auth="none", sitemap=False, cors='*', csrf=False)
    def drug_handler_new(self, dbname, id, **kw):
        model_name = "product.drugs"
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
                        "cus_id": rec.cus_id.display_name,
                        "side_effect": rec.side_effect,
                        "drowsy": rec.drowsy,
                        "color": rec.color,
                        "country": rec.country.display_name,
                        "storage_environment": rec.storage_environment,
                        "location": rec.location,
                        "basic_price": rec.basic_price,
                        "bonus_price": rec.bonus_price,
                        "drug_image": rec.drug_image,
                    }
                }
        except Exception:
            response = {
                "status": "error",
                "content": "not found"
            }
        return json.dumps(response)

    
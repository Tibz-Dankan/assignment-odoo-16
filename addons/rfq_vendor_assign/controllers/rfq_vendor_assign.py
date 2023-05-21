from odoo import http
from odoo.http import request

class PurchaseRequestController(http.Controller):
    @http.route('/purchase_request/create', type='http', auth='user', website=True)
    def create_purchase_request(self, **post):
        # Get logged in user
        user = request.env.user

        # Create purchase request
        purchase_request = request.env['purchase.request'].sudo().create({
            'name': post.get('name'),
            'description': post.get('description'),
            'user_id': user.id,
        })

        # Redirect to purchase request page
        return request.redirect('/purchase_request/%s' % purchase_request.id)

    @http.route('/purchase_request/<model("purchase.request"):purchase_request>', type='http', auth='user', website=True)
    def view_purchase_request(self, purchase_request, **post):
        # Get purchase request vendors
        vendor_ids = purchase_request.vendor_ids.ids

        # Render purchase request view
        return request.render('purchase_request.view_purchase_request', {
            'purchase_request': purchase_request,
            'vendor_ids': vendor_ids,
        })

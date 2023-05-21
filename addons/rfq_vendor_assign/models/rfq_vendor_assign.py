from odoo import fields, models

class PurchaseRFQ(models.Model):
    _inherit = 'purchase.order'

    vendor_ids = fields.Many2many('res.partner', string='Vendors')

class PurchaseRFQBid(models.Model):
    _name = 'purchase.order.bid'
    _description = 'Purchase RFQ Bid'

    order_id = fields.Many2one('purchase.order', string='RFQ', ondelete='cascade')
    vendor_id = fields.Many2one('res.partner', string='Vendor', required=True)
    price = fields.Float(string='Price', required=True)

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    bid_ids = fields.One2many('purchase.order.bid', 'order_id', string='Bids')
    winning_bid_id = fields.Many2one('purchase.order.bid', string='Winning Bid')

    def set_winning_bid(self, bid_id):
        self.write({'winning_bid_id': bid_id})

class PurchaseRequest(models.Model):
    _name = 'purchase.request'
    _description = 'Purchase Request'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description', required=True)
    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    department_id = fields.Many2one('hr.department', string='Department', required=True)

    def create_purchase_rfq(self):
        PurchaseRFQ = self.env['purchase.order']
        vendor_ids = self.env['res.partner'].search([('supplier', '=', True)])
        for request in self:
            rfq_vals = {
                'partner_id': vendor_ids[0].id,
                'order_line': [(0, 0, {
                    'product_id': self.env.ref('product.product_product_3').id,
                    'product_qty': 1.0,
                    'product_uom': self.env.ref('uom.product_uom_unit').id,
                })],
            }
            rfq = PurchaseRFQ.create(rfq_vals)
            rfq.vendor_ids = [(6, 0, vendor_ids.ids)]
            for vendor in vendor_ids:
                bid_vals = {
                    'order_id': rfq.id,
                    'vendor_id': vendor.id,
                    'price': 0.0,
                }
                bid = self.env['purchase.order.bid'].create(bid_vals)
        return rfq.id

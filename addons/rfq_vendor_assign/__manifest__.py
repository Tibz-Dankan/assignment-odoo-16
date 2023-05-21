{
    'name': 'Custom RFQ',
    'summary': 'Custom RFQ for Purchases App',
    'description': 'Adds custom RFQ functionality to the Purchases app.',
    'version': '1.0',
    'category': 'Purchases',
    'author': 'Tibesigwa Dankan',
    'depends': ['base', 'purchase'],
    'data': [
        'views/purchase_rfq_vendor_selection_form_view.xml',
        'views/purchase_rfq_bids_tree_view.xml',
        'views/purchase_rfq_winning_bid_form_view.xml',
    ],
    'installable': True,    
    'auto_install': False,
}

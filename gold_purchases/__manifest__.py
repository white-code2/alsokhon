# -*- coding: utf-8 -*-
{
    'name': "Gold Purchases",
    'description': """
       Gold Purchases""",
    'author': "White-Code, Kalpesh Gajera",
    'website': "http://www.white-code.co.uk",
    'URL': "https://system.white-code.co.uk/web#id=1667&action=395&model=project.task&view_type=form&menu_id=263",
    'category': 'Purchase',
    'version': '13.0.0.1',
    'depends': ['purchase_stock', 'po_gold_form', 'purchase_order_type'],
    'data': [
        'security/ir.model.access.csv',
        'data/gold_purity_data.xml',
        'views/purchase_order_view.xml',
        'views/stock_picking_view.xml',
        'views/gold_purity_view.xml'
    ],

}

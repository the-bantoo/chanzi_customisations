from __future__ import unicode_literals
import frappe
from frappe import msgprint, _


def in_dictlist(key, value, my_dictlist):
    for i in my_dictlist:
        if i[key] == value:
            return i
    return {}

@frappe.whitelist()
def make_stock_entry(invoice_name):
	
	doc = frappe.get_doc('Purchase Invoice', invoice_name)
	src = ''
	items = []
	
	stock_items = frappe.get_list("Item", filters={
        'is_stock_item': 1
    })

	for item in doc.items:
		if in_dictlist('name', item.item_code, stock_items):
			items.append({
				'item_code': item.item_code,
				'item_name': item.item_name,
				'qty': item.stock_qty,
				'stock_uom': item.stock_uom,
				'basic_rate': item.base_rate,
				'basic_amount': item.base_amount,
				'expense_account': item.expense_account,
				'cost_center': item.cost_center,
				's_warehouse': item.warehouse
			})
			if src =='' :
				src = item.warehouse
			
		
	
	stock_entry = frappe.get_doc({
		'doctype': 'Stock Entry',
		'stock_entry_type': 'Material Issue',
		'purpose': 'Material Issue',
		'from_warehouse': src,
		'items': items,
		'remarks': 'Created from Purchase Invoice ' + doc.name,
		'reference_document': doc.name
		
	}).insert()
	
	return stock_entry.name
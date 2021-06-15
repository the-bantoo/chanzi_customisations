from __future__ import unicode_literals
import frappe
from frappe import msgprint, _

@frappe.whitelist()
def make_stock_entry(doc):
	#frappe.errprint("1");
	
	src = ''
	items = {}
	
	for item in doc.items:
		items.append({
			'item_code': item.item_code,
			'item_name': item.item_name,
			'qty': item.stock_qty,
			'stock_uom' = item.stock_uom,
			'basic_rate' = item.base_rate,
			'basic_amount' = item.base_amount,
			'expense_account' = item.expense_account,
			'cost_center' = item.cost_center,
			's_warehouse': item.warehouse,
			
		})
		
	
	frappe.get_doc({
		'doctype': 'Stock Entry',
		'stock_entry_type': 'Material Issue',
		'purpose': 'Material Issue',
		'from_warehouse': src,
		'items': items,
		'remarks': 'Created from Purchase Invoice'
		
	}).insert()
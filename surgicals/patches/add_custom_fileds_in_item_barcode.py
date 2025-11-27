import frappe

def execute():
    
    if not frappe.db.exists("Custom Field", "Item Barcode-serial_no"):
        frappe.get_doc({
            "doctype": "Custom Field",
            "dt": "Item Barcode",
            "fieldname": "serial_no",
            "label": "Serial No",
            "fieldtype": "Data",
            "insert_after": "item_name", 
            "in_list_view": 1,
            "read_only": 0,
            "reqd": 0,
            "translatable": 0
        }).insert(ignore_permissions=True)

    if not frappe.db.exists("Custom Field", "Item Barcode-expiry_date"):
        frappe.get_doc({
            "doctype": "Custom Field",
            "dt": "Item Barcode",
            "fieldname": "expiry_date",
            "label": "Expiry Date",
            "fieldtype": "Date",
            "insert_after": "serial_no",
            "in_list_view": 1,
            "read_only": 0,
            "reqd": 0
        }).insert(ignore_permissions=True)
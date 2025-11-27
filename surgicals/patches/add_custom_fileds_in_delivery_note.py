import frappe

def execute():
    
    if not frappe.db.exists("Custom Field", "Delivery Note-serial_no"):
        frappe.get_doc({
            "doctype": "Custom Field",
            "dt": "Delivery Note Item",
            "fieldname": "serial_nom",
            "label": "Serial No",
            "fieldtype": "Data",
            "insert_after": "item_name", 
            "in_list_view": 1,
            "read_only": 0,
            "reqd": 0,
            "translatable": 0
        }).insert(ignore_permissions=True)

    if not frappe.db.exists("Custom Field", "Delivery Note-expiry_date"):
        frappe.get_doc({
            "doctype": "Custom Field",
            "dt": "Delivery Note Item",
            "fieldname": "expiry_date",
            "label": "Expiry Date",
            "fieldtype": "Date",
            "insert_after": "serial_nom",
            "in_list_view": 1,
            "read_only": 0,
            "reqd": 0
        }).insert(ignore_permissions=True)
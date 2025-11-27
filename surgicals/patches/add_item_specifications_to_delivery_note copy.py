import frappe

def execute():
    if frappe.db.exists("Custom Field", "Delivery Note-item_specifications"):
        return

    frappe.get_doc({
        "doctype": "Custom Field",
        "dt": "Delivery Note",
        "fieldname": "item_specifications",
        "label": "Item Specifications",
        "fieldtype": "Table",
        "options": "Item Specification",
        "insert_after": "items"
    }).insert(ignore_permissions=True)
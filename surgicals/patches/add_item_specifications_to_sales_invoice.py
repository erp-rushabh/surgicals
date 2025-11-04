import frappe

def execute():
    if frappe.db.exists("Custom Field", "Sales Invoice-item_specifications"):
        return

    # Add checkbox first (so it appears before the table)
    frappe.get_doc({
        "doctype": "Custom Field",
        "dt": "Sales Invoice",
        "fieldname": "show_item_specifications",
        "label": "Show Item Specifications in Print",
        "fieldtype": "Check",
        "insert_after": "items",
        "default": "1"
    }).insert(ignore_permissions=True)

    # Then add the child table after the checkbox
    frappe.get_doc({
        "doctype": "Custom Field",
        "dt": "Sales Invoice",
        "fieldname": "item_specifications",
        "label": "Item Specifications",
        "fieldtype": "Table",
        "options": "Item Specification",
        "insert_after": "show_item_specifications"
    }).insert(ignore_permissions=True)
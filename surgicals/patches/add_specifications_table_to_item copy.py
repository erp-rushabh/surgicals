import frappe

def execute():
    # Check if field already exists
    if frappe.db.exists("Custom Field", "Item-specifications"):
        print("Custom field 'specifications' already exists in Item")
        return

    # Create the custom field
    frappe.get_doc({
        "doctype": "Custom Field",
        "dt": "Item",
        "fieldname": "specifications",
        "label": "Specifications",
        "fieldtype": "Table",
        "options": "Item Specification",
        "insert_after": "stock_uom",
        "collapsible": 1,
        "read_only": 0,
        "reqd": 0,
        "no_copy": 0,
        "print_hide": 0
    }).insert(ignore_permissions=True)

    print("✅ Added 'Specifications' table to Item after 'stock_uom'")
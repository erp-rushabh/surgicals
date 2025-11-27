import frappe

@frappe.whitelist()
def get_serial_expiry_from_barcode(barcode):
    data = frappe.db.get_value(
        "Item Barcode",
        {"barcode": barcode},
        ["parent as item_code", "serial_no", "expiry_date"],
        as_dict=True
    )

    if not data:
        return None

    item = frappe.db.get_value(
        "Item",
        data.item_code,
        ["item_name", "stock_uom"],
        as_dict=True
    )

    data.item_name = item.item_name
    data.uom = item.stock_uom

    return data


@frappe.whitelist()
def get_serial_expiry_from_barcode_nom(barcode):
    data = frappe.db.get_value(
        "Item Barcode",
        {"barcode": barcode},
        ["parent as item_code", "serial_no", "expiry_date"],
        as_dict=True
    )

    if not data:
        return None

    item = frappe.db.get_value(
        "Item",
        data.item_code,
        ["item_name", "stock_uom"],
        as_dict=True
    )

    data.item_name = item.item_name
    data.uom = item.stock_uom

    return data
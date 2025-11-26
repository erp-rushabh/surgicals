import frappe

def execute():
    """
    Permanently remove all mandatory fields in Sales Invoice and its child tables
    """
    doctypes = ["Sales Invoice", "Sales Invoice Item"]  # Add other child tables if needed

    for dt in doctypes:
        try:
            meta = frappe.get_doc("DocType", dt)
        except frappe.DoesNotExistError:
            frappe.log_error(f"{dt} does not exist", "remove_mandatory_fields")
            continue

        removed_fields = []
        for df in meta.fields:
            if df.reqd:
                df.reqd = 0
                removed_fields.append(f"{dt}.{df.fieldname}")

        if removed_fields:
            meta.save()
            frappe.clear_cache(doctype=dt)
            print(f"Removed mandatory fields: {', '.join(removed_fields)}")

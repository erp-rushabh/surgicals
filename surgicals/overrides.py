def ignore_sales_invoice_mandatory(doc, method):
    """
    Ignore all mandatory validation in Sales Invoice, including system-required fields.
    """
    # Ignore mandatory fields
    doc.flags.ignore_mandatory = True
    doc.flags.ignore_validate = True

    # Clear system-enforced mandatory fields
    doc.payment_due_date = None
    if doc.get("items"):
        for item in doc.items:
            item.income_account = None
            item.cost_center = None  # optional, depending on your setup

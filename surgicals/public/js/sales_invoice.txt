// Extend the ERPNext SalesInvoiceController
erpnext.accounts.SalesInvoiceController = class SalesInvoiceController extends erpnext.accounts.SalesInvoiceController {
	refresh(doc, dt, dn) {
		// Call the original refresh first
		super.refresh(doc, dt, dn);

		// 👇 OVERRIDE: Make due_date NEVER required (remove the condition)
		this.frm.toggle_reqd("due_date", 0); // always optional
	}
};
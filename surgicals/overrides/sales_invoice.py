import frappe
from erpnext.accounts.doctype.sales_invoice.sales_invoice import SalesInvoice

class CustomSalesInvoice(SalesInvoice):
    def validate(self):
        # Skip all standard validations
        self.flags.ignore_mandatory = True
        self.flags.ignore_validate = True
        self.flags.ignore_links = True
        # do not call super()
        pass

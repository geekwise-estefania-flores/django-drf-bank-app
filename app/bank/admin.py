from django.contrib import admin
from .models import Account, Branch, Customer, Product


# class AccountAdmin(admin.ModelAdmin):
#     list_display = (account_number)

# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ('customer_name', 'customer_email')

admin.site.register(Account)
admin.site.register(Branch)
admin.site.register(Customer)
admin.site.register(Product)

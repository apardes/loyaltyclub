from django.contrib import admin
from club.models import Member, Business, Credit

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
	fields = ['phone_number', 'created_on']

class BusinessAdmin(admin.ModelAdmin):
	fields = ['name', 'phone_number', 'created_on']
	list_display = ['name', 'phone_number']

class CreditAdmin(admin.ModelAdmin):
	fields = ['balance', 'created_on', 'business', 'member']


admin.site.register(Member, MemberAdmin)
admin.site.register(Business, BusinessAdmin)
admin.site.register(Credit, CreditAdmin)
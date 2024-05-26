from django.contrib import admin
from book.models import BookstoreModel 

# Register your models here.
#admin.site.register(BookstoreModel)
class BookStoreModelAdmin(admin.ModelAdmin):
    list_display =('id','book_name','author','category','frist_pub','last_pub')
admin.site.register(BookstoreModel,BookStoreModelAdmin)
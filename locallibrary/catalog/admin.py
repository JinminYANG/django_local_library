from django.contrib import admin

# Register your models here.
from catalog.models import Author, Genre, Book, BookInstance

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


# 연결된 모델에 관리자 클래스 등록
admin.site.register(Author, AuthorAdmin)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

# 데코레이터를 사용하여 Book의 Admin 클래스 등록
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

# 데코레이터를 사용하여 BookInstance에 대한 Admin 클래스 등록
# list_display 및 필드셋의 BookInstanceAdmin 클래스에 대여자 필드를 추가한다.
# 관리 섹션에 필드가 표시 되므로 필요에 따라 BookInstance에 사용자를 할당할 수 있다.
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )


from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Scope, Tag

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main_count = 0
        for form in self.forms:

            if form.cleaned_data and form.cleaned_data.get('is_main'):
                is_main_count += 1

        if is_main_count == 0:
            raise ValidationError("У этой статьи должен быть один основной раздел.")
        elif is_main_count > 1:
            raise ValidationError("У этой статьи может быть только один основной раздел.")

        return super().clean()

class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
    list_display = ('title', 'published_at')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


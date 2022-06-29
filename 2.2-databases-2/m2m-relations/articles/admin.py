from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main_counter = 0
        exist_tags = []
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            data = form.cleaned_data
            #print(data)
            tag = data.get('tag', None)
            if not tag:
                continue
            is_main = data.get('is_main', None)
            if is_main:
                is_main_counter += 1




            if tag in exist_tags:
                raise ValidationError("Повтор тематики")
            exist_tags .append(tag)
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            #raise ValidationError('Тут всегда ошибка')
        if is_main_counter == 0:
            raise ValidationError('Укажите основной раздел')
        elif is_main_counter > 1:
            raise ValidationError('Основной раздел может быть только один')

        return super().clean()  # вызываем базовый код переопределяемого метода



class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    #pass
    inlines = [ScopeInline]


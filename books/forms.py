from django.forms import ModelForm, Textarea, SelectDateWidget, ModelMultipleChoiceField
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Book, Author


class BookForm(ModelForm):
    authors = ModelMultipleChoiceField(queryset=Author.objects.all(), required=False,
                                       widget=FilteredSelectMultiple('Authors', is_stacked=False))

    class Media:
        css = {
            'all': ('/static/admin/css/widgets.css',),
        }
        js = ('/admin/jsi18n',)

    class Meta:
        model = Book
        fields = '__all__'

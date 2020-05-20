from django.forms import ModelForm, Textarea, SelectDateWidget, ModelMultipleChoiceField, DateField
from django.forms.models import inlineformset_factory
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Book, Author


class BookForm(ModelForm):
    authors = ModelMultipleChoiceField(queryset=Author.objects.all(), required=False,
                                       widget=FilteredSelectMultiple('Authors', is_stacked=False))

    date_of_release = DateField(label="Date of release (YYYY-MM-DD)", required=False)

    class Media:
        css = {
            'all': ('/static/admin/css/widgets.css',),
        }
        js = ('/admin/jsi18n',)

    class Meta:
        model = Book
        fields = '__all__'

from django.forms import ModelForm, Form
from django import forms
from .models import Contact, Task, Tag

class ContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

    def __init__(self, *args, **kwargs):
        ModelForm.__init__(self, *args, **kwargs)
        for k, v in self.fields.items():
            v.widget.attrs.update({'class' : 'form-control' })

class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ['content', 'status', 'time_priority', 'important_priority', 'tags']

    def __init__(self, *args, **kwargs):
        ModelForm.__init__(self, *args, **kwargs)
        for k, v in self.fields.items():
            v.widget.attrs.update({'class' : 'form-control' })
        if 'instance' in kwargs:
            self.fields['tags'] = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=kwargs['instance'].user.tag_list.all(), required=False)
        else:
            self.fields['tags'] = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=kwargs['initial']['user'].tag_list.all(), required=False)

    def readonly(self):
        for k, v in self.fields.items():
            v.disabled = True

class TagForm(ModelForm):

    class Meta:
        model = Tag
        fields = ['name']

    def __init__(self, *args, **kwargs):
        ModelForm.__init__(self, *args, **kwargs)
        for k, v in self.fields.items():
            v.widget.attrs.update({'class' : 'form-control' })

    def readonly(self):
        for k, v in self.fields.items():
            v.disabled = True


class TaskFilterForm(Form):

    status = forms.ChoiceField(choices=Task.STATUS_LIST + [('all', 'pas de filtre de status')])
    important_priority = forms.ChoiceField(choices=Task.IMPORTANT_PRIORITY_LIST + [('all', "pas de filtre de d'importance")])
    time_priority = forms.ChoiceField(choices=Task.TIME_PRIORITY_LIST + [('all', "pas de filtre d'urgence")])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        for k, v in self.fields.items():
            v.widget.attrs.update({'class' : 'form-control mr-2' })

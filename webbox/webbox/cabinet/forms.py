from django import forms

class HomeworkForm(forms.Form):
    answer = forms.CharField( required=True, label='', widget=forms.Textarea(attrs={'rows': 10, 'cols': 40, 'resize': 'none'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['answer'].widget.attrs['is'] = 'highlighted-code'
        self.fields['answer'].widget.attrs['language'] = 'python'
        self.fields['answer'].widget.attrs['theme'] = 'monokai'
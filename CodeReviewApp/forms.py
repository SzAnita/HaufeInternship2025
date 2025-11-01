from django import forms

from CodeReviewApp.models import CodeReview


class CodeReviewForm(forms.ModelForm):
    language = forms.CharField(label='Language', max_length=40, required=True, widget=forms.TextInput(attrs={'placeholder': 'e.g. Python, JavaScript'}))
    code = forms.CharField(label='Code to review', widget=forms.Textarea, required=True)
    description = forms.CharField(label='Description', max_length=200, required=False)

    class Meta:
        model = CodeReview
        fields = ('language', 'description', 'code')


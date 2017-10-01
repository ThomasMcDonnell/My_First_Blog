from django import forms
from pagedown.widgets import PagedownWidget
from .models import Post,Comment

class PostForm(forms.ModelForm):
    text = forms.CharField(widget=PagedownWidget(show_preview=False))
    published_date = forms.DateField(widget=forms.SelectDateWidget, required=False)
    class Meta:
        model = Post
        fields = ('author','title', 'text', 'published_date')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author','text')

        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }

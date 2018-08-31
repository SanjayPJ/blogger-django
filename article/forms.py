from django import forms
from article.models import Article

class ArticleForm(forms.ModelForm):
    """Form definition for Article."""

    class Meta:
        """Meta definition for Articleform."""

        model = Article
        fields = ("title", "slug", "body", "thumb")

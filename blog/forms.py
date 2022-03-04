from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # Fields that should be excluded
        exclude = ["post"]
        # Your Name and Your Email appears in form
        labels = {
          "user_name": "Your Name",
          "user_email": "Your Email",
          "text": "Your Comment"
        }

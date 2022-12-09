from django import forms
from .models import ImageUpload,NippoModel

class NippoFormClass(forms.Form):
    title = forms.CharField(max_length=100, label="タイトル", widget=forms.TextInput(attrs={'placeholder':'タイトル...'}),initial='title')
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'内容...'}), max_length=1000, label="内容",initial='content')
    def __init__(self, *args, **kwargs):
        for field in self.base_fields.values():
            field.widget.attrs.update({"class":"form-control"})
        super().__init__(*args, **kwargs)

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = "__all__"
'''
class NippoModelForm(forms.ModelForm):
    class Meta:
        model = NippoModel
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        for field in self.base_fields.values():
            field.widget.attrs["class"] = "form-control"
        super().__init__(*args, **kwargs)

#フィールド全て
fields = "__all__"
#フィールドの一部
fields = ["フィールド1", "フィールド2"]
#一部のフィールドを除く
exclude = "user"
'''
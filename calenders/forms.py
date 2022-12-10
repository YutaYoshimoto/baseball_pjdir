from django import forms
from .models import ImageUpload,NippoModel
#from bootstrap_datepicker_plus import DatePickerInput
#from django.contrib.admin.widgets import AdminDateWidget

class NippoFormClass(forms.Form):
    '''
    class Meta:
        date = forms.DateField(
            label="予定日:2022-01-01のように記入してください",
                #管理サイトの表示を流用
            #initial='2022-12-10',
        )
        widgets = {'date': AdminDateWidget(), }
        '''
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
    date = forms.DateField(
        label="作成日",
        widget=DatePickerInput(format='%Y-%m-%d')
    )

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
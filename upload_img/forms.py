from django import forms
from upload_img.models import upload_img

class ImageFileUploadForm(forms.ModelForm):
    class Meta:
        model = upload_img
        fields = ('請輸入員工編號', '簽名檔上傳')
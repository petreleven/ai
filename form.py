class ProductForm(forms.ModelForm):

    class Meta:
        model = Product

        fields = (
            "name",
            "image",
            "price",
            "description",
            "available",
            "category",
            "date",
        )
        widgets = {
            "name": TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px;",
                    "placeholder": "Name of product",
                }
            ),
            "image": FileInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px;",
                }
            ),
            "price": NumberInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px;",
                    "placeholder": "Price",
                }
            ),
            "description": TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px;",
                    "placeholder": "Description",
                }
            ),
            "available": CheckboxInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 15px;",
                }
            ),
        }
MEDIA_ROOT = os.path.join(BASE_DIR , "media/")
MEDIA_URL = "/media/"
urlpatterns = [
    path("admin/", admin.site.urls),
    path("" ,include("mainapp.urls"))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

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

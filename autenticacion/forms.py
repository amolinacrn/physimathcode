from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PermisosParaDocente


# class IniciarSesionForm(forms.ModelForm):

# usuario = forms.CharField(max_length=20, label="usuario:")
# contrasenya = forms.CharField(max_length=20, label="contraseña:")


# class Meta:
#     model = RegistrarUsuario
#     fields = "__all__"


class IniciarSesionForm(UserCreationForm):

    first_name = forms.CharField(label="Nombres", max_length=150)
    last_name = forms.CharField(label="Apellidos", max_length=150)
    email = forms.EmailField(label="Correo electrónico", max_length=100)

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
        fields = UserCreationForm.Meta.fields + (  # agrege metadatos adicionales
            "first_name",
            "last_name",
            "email",
        )

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for fieldname in ["username", "password1", "password2"]:
            self.fields[fieldname].help_text = None  # no muestre textos de advertencias


class PermisosParaDocentesForm(forms.ModelForm):
    class Meta:
        model = PermisosParaDocente
        fields = "__all__"

    cndsn = [None, True, False]

    PERMISOSDOCENTES = []

    for i in cndsn:

        if i == None:
            x = [i, "--------"]
        elif i:
            x = [i, "permitir"]
        else:
            x = [i, "No permitir"]

        PERMISOSDOCENTES.append(x)

    permiso_docente = forms.CharField(
        max_length=10,
        label="Permiso",
        required=False,
        widget=forms.Select(choices=PERMISOSDOCENTES, attrs={"required": "True"}),
    )

    usuario = forms.CharField(
        max_length=50,
        label="",
        required=True,
        initial="o",  # mi_user_name.id_usuario.username,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["usuario"].disabled = True

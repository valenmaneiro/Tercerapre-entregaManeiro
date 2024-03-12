from django import forms

class FutbolistaForm(forms.Form):
    nombreCompleto = forms.CharField(label="Nombre Completo", max_length=50, required=True)
    nacionalidad = forms.CharField(label="Nacionalidad", max_length=50, required=True)
    dorsal = forms.IntegerField(label="Dorsal", required=True)
    equipo = forms.CharField(label="Equipo", max_length=50, required=True)

class EntrenadorForm(forms.Form):
    nombreCompleto = forms.CharField(label="Nombre Completo", max_length=50, required=True)
    nacionalidad = forms.CharField(label="Nacionalidad", max_length=50, required=True)
    equipo = forms.CharField(label="Equipo", max_length=50, required=True)


class EquipoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=50, required=True)
    pais = forms.CharField(label="Pais", max_length=50, required=True)
    nroSocios = forms.IntegerField(label="Cantidad de Socios", required=True)
    fechaFundacion = forms.DateField(label="Fecha de Fundacion", required=True)
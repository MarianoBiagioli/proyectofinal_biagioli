from django import forms

class FamiliarFormulario(forms.Form):

    #Especificar los campos
    nombre = forms.CharField()
    apellido = forms.CharField()
    dni = forms.IntegerField()

class FamiliarBusqueda(forms.Form):
    criterio = forms.CharField()


    
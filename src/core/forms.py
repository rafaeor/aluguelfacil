from django import forms
from .models import Imovel, Aluguel
from accounts.models import CustomUser


class ImovelForm(forms.ModelForm):
    class Meta:
        model = Imovel
        exclude = ('proprietario',)
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 3, 'class': 'w-full bg-slate-50 border border-slate-200 rounded-xl py-3 px-4 focus:outline-none focus:border-emerald-500'}),
            'endereco': forms.Textarea(attrs={'rows': 2, 'class': 'w-full bg-slate-50 border border-slate-200 rounded-xl py-3 px-4 focus:outline-none focus:border-emerald-500'}),
            'nome': forms.TextInput(attrs={'class': 'w-full bg-slate-50 border border-slate-200 rounded-xl py-3 px-4 focus:outline-none focus:border-emerald-500'}),
            'valor_aluguel': forms.NumberInput(attrs={'class': 'w-full bg-slate-50 border border-slate-200 rounded-xl py-3 px-4 focus:outline-none focus:border-emerald-500'}),
            'valor_condominio': forms.NumberInput(attrs={'class': 'w-full bg-slate-50 border border-slate-200 rounded-xl py-3 px-4 focus:outline-none focus:border-emerald-500'}),
            'quartos': forms.NumberInput(attrs={'class': 'w-full bg-slate-50 border border-slate-200 rounded-xl py-3 px-4 focus:outline-none focus:border-emerald-500'}),
            'vagas': forms.NumberInput(attrs={'class': 'w-full bg-slate-50 border border-slate-200 rounded-xl py-3 px-4 focus:outline-none focus:border-emerald-500'}),
            'area': forms.NumberInput(attrs={'class': 'w-full bg-slate-50 border border-slate-200 rounded-xl py-3 px-4 focus:outline-none focus:border-emerald-500'}),
            'wifi_ssid': forms.TextInput(attrs={'class': 'w-full bg-slate-50 border border-slate-200 rounded-xl py-3 px-4 focus:outline-none focus:border-emerald-500'}),
            'wifi_senha': forms.TextInput(attrs={'class': 'w-full bg-slate-50 border border-slate-200 rounded-xl py-3 px-4 focus:outline-none focus:border-emerald-500'}),
            'foto_url': forms.URLInput(attrs={'class': 'w-full bg-slate-50 border border-slate-200 rounded-xl py-3 px-4 focus:outline-none focus:border-emerald-500', 'placeholder': 'https://...'}),
        }


class VincularInquilinoForm(forms.Form):
    inquilino = forms.ModelChoiceField(
        queryset=CustomUser.objects.filter(user_type='inquilino').order_by('username'),
        label='Inquilino',
        widget=forms.Select(attrs={'class': 'w-full bg-slate-50 border border-slate-200 rounded-xl py-3 px-4 focus:outline-none focus:border-emerald-500'}),
    )
    data_inicio = forms.DateField(
        label='Data de início',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'w-full bg-slate-50 border border-slate-200 rounded-xl py-3 px-4 focus:outline-none focus:border-emerald-500'}),
    )

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from .models import Imovel, Aluguel, Pagamento
from .forms import ImovelForm, VincularInquilinoForm


@login_required
def painel_proprietario(request):
    imoveis = Imovel.objects.filter(proprietario=request.user).prefetch_related('alugueis__inquilino', 'alugueis__pagamentos')

    hoje = timezone.now()
    total_recebido = 0
    total_esperado = 0
    imoveis_data = []

    for imovel in imoveis:
        aluguel_ativo = imovel.alugueis.filter(ativo=True).first()
        inquilino_nome = ''
        status_pagamento = 'sem_inquilino'
        pagamento_valor = 0
        pagamento_id = None

        if aluguel_ativo:
            inquilino_nome = aluguel_ativo.inquilino.get_full_name() or aluguel_ativo.inquilino.username
            pagamento = aluguel_ativo.pagamentos.filter(
                mes=hoje.month, ano=hoje.year
            ).first()

            if pagamento:
                pagamento_valor = pagamento.valor
                pagamento_id = pagamento.id
                status_pagamento = pagamento.status
                if pagamento.status == 'pago':
                    total_recebido += pagamento.valor
                total_esperado += pagamento.valor
            else:
                total_esperado += imovel.valor_aluguel

        imoveis_data.append({
            'imovel': imovel,
            'inquilino_nome': inquilino_nome,
            'status_pagamento': status_pagamento,
            'pagamento_valor': pagamento_valor,
            'pagamento_id': pagamento_id,
        })

    progresso = (total_recebido / total_esperado * 100) if total_esperado > 0 else 0

    return render(request, 'core/painel_proprietario.html', {
        'imoveis': imoveis_data,
        'total_recebido': total_recebido,
        'total_esperado': total_esperado,
        'progresso': progresso,
        'mes': hoje.strftime('%B').capitalize(),
    })


@login_required
def create_imovel(request):
    if request.method == 'POST':
        form = ImovelForm(request.POST)
        if form.is_valid():
            imovel = form.save(commit=False)
            imovel.proprietario = request.user
            imovel.save()
            return redirect('core:painel_proprietario')
    else:
        form = ImovelForm()
    return render(request, 'core/imovel_form.html', {'form': form})


@login_required
def painel_inquilino(request):
    aluguel_ativo = Aluguel.objects.filter(
        inquilino=request.user, ativo=True
    ).select_related('imovel').first()

    hoje = timezone.now()
    pagamento = None
    pagamentos_anteriores = []

    if aluguel_ativo:
        pagamento, created = Pagamento.objects.get_or_create(
            aluguel=aluguel_ativo,
            mes=hoje.month,
            ano=hoje.year,
            defaults={
                'valor': aluguel_ativo.imovel.valor_aluguel,
                'data_vencimento': hoje.replace(day=15),
            }
        )
        pagamentos_anteriores = Pagamento.objects.filter(
            aluguel=aluguel_ativo, status='pago'
        ).order_by('-ano', '-mes')[:10]

    return render(request, 'core/painel_inquilino.html', {
        'aluguel': aluguel_ativo,
        'pagamento': pagamento,
        'pagamentos_anteriores': pagamentos_anteriores,
        'mes': hoje.strftime('%B').capitalize(),
    })


@login_required
def pagar_pix(request, pagamento_id):
    pagamento = get_object_or_404(Pagamento, id=pagamento_id, aluguel__inquilino=request.user)
    if pagamento.status == 'pendente':
        pagamento.status = 'pago'
        pagamento.data_pagamento = timezone.now()
        pagamento.save()
    return redirect('core:painel_inquilino')
from django.contrib import messages


@login_required
def vincular_inquilino(request, imovel_id):
    imovel = get_object_or_404(Imovel, id=imovel_id, proprietario=request.user)
    if request.method == 'POST':
        form = VincularInquilinoForm(request.POST)
        if form.is_valid():
            Aluguel.objects.create(
                inquilino=form.cleaned_data['inquilino'],
                imovel=imovel,
                data_inicio=form.cleaned_data['data_inicio'],
                ativo=True,
            )
            messages.success(request, 'Inquilino vinculado com sucesso!')
            return redirect('core:painel_proprietario')
    else:
        form = VincularInquilinoForm()
    return render(request, 'core/vincular_inquilino.html', {
        'form': form, 'imovel': imovel
    })


def detalhe_imovel(request, imovel_id):
    imovel = get_object_or_404(Imovel, id=imovel_id)
    return render(request, 'core/detalhe_imovel.html', {'imovel': imovel})


def index(request):
    if request.user.is_authenticated:
        if request.user.user_type == "proprietario":
            return redirect("core:painel_proprietario")
        return redirect("core:painel_inquilino")
    return redirect("accounts:login")

from odoo import fields, models, api, _
import logging

_logger = logging.getLogger(__name__)

class ResPartnerCustom(models.Model):
    _inherit = "res.partner"

    currency_id = fields.Many2one("res.currency", related="company_id.currency_id")
    # GRUPO: CLIENTE
    _allss_fornecedor = fields.Char("Fornecedor")
    _allss_titular_inst = fields.Boolean("Copiar Cliente para Titular da Instalação?")
    # _allss_nome = fields.Char("Nome")
    _allss_cpf = fields.Char("CPF do Cliente")
    _allss_cnpj = fields.Char("CNPJ do Cliente")
    _allss_gps = fields.Char("GPS")
    _allss_respon = fields.Many2one('res.users', string='Responsável')
    _allss_met_pag = fields.Char("Método de Pagamento")
    _allss_origem = fields.Char("Origem")
    # GRUPO: DADOS DA INSTALAÇÃO
    _allss_concessionaria = fields.Char("Concessionaria")
    _allss_nome_titular_inst = fields.Char("Nome Titular da Instalação")
    _allss_sobr_titular_inst = fields.Char("Sobrenome Titular da Instalação")
    _allss_cpf_inst = fields.Char("CPF da Instalação")
    _allss_cnpj_inst = fields.Char("CNPJ da Instalação")
    _allss_end_inst = fields.Char("Endereço da Instalação")
    _allss_city_inst = fields.Char("Cidade da Instalação")
    _allss_est_inst = fields.Char("Estado da Instalação")
    _allss_cep_inst = fields.Char("CEP da Instalação")
    _allss_tp_estab_inst = fields.Char("Tipo de Estabelecimento")
    _allss_unid_consum_inst = fields.Char("Unidade Consumidora")
    _allss_class_inst = fields.Char("Classe da Instalação")
    _allss_gps_inst = fields.Char("GPS da Instalação")
    _allss_obs_inst = fields.Char("Observações da Instalação")
    # GRUPO: DADOS PARA DIMENSIONAMENTO
    _allss_tp_telhado_dimen = fields.Char("Tipo de Telhado")
    _allss_md_consu_dimen = fields.Char("Média Consumo KWh")
    _allss_qtd_mes_dimen = fields.Char("Quantidade Meses KWh")
    _allss_consu_dimen_1 = fields.Char("Consumo KWh Mês 1")
    _allss_consu_dimen_2 = fields.Char("Consumo KWh Mês 2")
    _allss_consu_dimen_3 = fields.Char("Consumo KWh Mês 3")
    _allss_consu_dimen_4 = fields.Char("Consumo KWh Mês 4")
    _allss_consu_dimen_5 = fields.Char("Consumo KWh Mês 5")
    _allss_consu_dimen_6 = fields.Char("Consumo KWh Mês 6")
    _allss_consu_dimen_7 = fields.Char("Consumo KWh Mês 7")
    _allss_consu_dimen_8 = fields.Char("Consumo KWh Mês 8")
    _allss_consu_dimen_9 = fields.Char("Consumo KWh Mês 9")
    _allss_consu_dimen_10 = fields.Char("Consumo KWh Mês 10")
    _allss_consu_dimen_11 = fields.Char("Consumo KWh Mês 11")
    _allss_consu_dimen_12 = fields.Char("Consumo KWh Mês 12")
    # GRUPO: FOTOS DA INSTALAÇÃO
    _allss_frente_fotos_inst = fields.Binary("RG-CPF-CNH - Frente da Instalação")
    _allss_verso_fotos_inst = fields.Binary("RG-CPF-CNH - Verso da Instalação")
    _allss_conta_fotos_inst_1 = fields.Binary("Conta de Luz - 1")
    _allss_conta_fotos_inst_2 = fields.Binary("Conta de Luz - 2")
    _allss_conta_fotos_inst_3 = fields.Binary("Conta de Luz - 3")
    _allss_conta_fotos_inst_4 = fields.Binary("Conta de Luz - 4")
    _allss_fachada_fotos_inst = fields.Binary("Fachada")
    _allss_telhado_fotos_inst = fields.Binary("Foto do Telhado")
    _allss_poste_fotos_inst = fields.Binary("Poste da Concessionária")
    _allss_medidor_fotos_inst = fields.Binary("Medidor da Concessionária")
    _allss_disjuntor_fotos_inst = fields.Binary("Foto do Disjuntor")
    _allss_quadro_fotos_inst = fields.Binary("Quadro de Distribuição")
    _allss_transformador_fotos_inst = fields.Binary("Foto Transformador Concessionária")
    _allss_paines_fotos_inst = fields.Binary("Painés Solares Instalados")
    _allss_inversores_fotos_inst = fields.Binary("Inversores Instalados")
    _allss_dps_fotos_inst = fields.Binary("Disjuntor e DPS Fotovoltaico")
    _allss_placa_fotos_inst_1 = fields.Binary("Placa de Advertência - 1")
    _allss_placa_fotos_inst_2 = fields.Binary("Placa de Advertência - 2")
    _allss_medidor_fotos_inst = fields.Binary("Medidor Bidirecional Trocado")
    _allss_checklist_fotos_inst = fields.Binary("Checklist de Instalação")
    _allss_relatorio_fotos_inst = fields.Binary("Relatório de Instalação")
    # GRUPO: DOCUMENTOS DE PROJETO CONCESSIONÁRIA
    _allss_crea_doc_proj = fields.Binary("ART CREA")
    _allss_unifilar_doc_proj = fields.Binary("Diagrama Unifilar")
    _allss_anexo_doc_proj_1 = fields.Binary("Anexo - 1")
    _allss_anexo_doc_proj_2 = fields.Binary("Anexo - 2")
    _allss_anexo_doc_proj_3 = fields.Binary("Anexo - 3")
    _allss_anexo_doc_proj_4 = fields.Binary("Anexo - 4")
    _allss_anexo_doc_proj_5 = fields.Binary("Anexo - 5")
    _allss_parecer_doc_proj = fields.Binary("Parecer de Acesso")
    # GRUPO: FOTOS DOCUMENTOS PESSOA FÍSICA
    _allss_frente_doc_pessoa_fisica = fields.Binary("RG-CPF-CNH - Frente")
    _allss_verso_doc_pessoa_fisica = fields.Binary("RG-CPF-CNH - Verso")
    _allss_vend_doc_pessoa_fisica = fields.Binary("Comprovante de Venda")
    _allss_ender_doc_pessoa_fisica = fields.Binary("Comprovante Endereço")
    # GRUPO: DADOS DE FINANCIAMENTO
    _allss_ficha_financ_1 = fields.Binary("Ficha Financiamento - 1")
    _allss_ficha_financ_2 = fields.Binary("Ficha Financiamento - 2")
    _allss_ficha_financ_3 = fields.Binary("Ficha Financiamento - 3")
    _allss_ficha_financ_4 = fields.Binary("Ficha Financiamento - 4")
    _allss_boleto_financ = fields.Binary("Boletos de Financiamento")
    # GRUPO: PEDIDOS DE COMPRA - NOTAS FISCAIS - BOLETOS
    _allss_equip_pedido_compra = fields.Binary("Pedido Equipamentos Distribuidor")
    _allss_nf_equip_pedido_compra = fields.Binary("NF Equipamentos Distribuidor")
    _allss_bl_equip_pedido_compra = fields.Binary("Boletos Equipamentos Distribuidor")
    _allss_cp_pag_pedido_compra = fields.Binary("Comprovante de Pagamento Distribuidor")
    _allss_fix_pedido_compra = fields.Binary("Pedidos Estruturas de Fixação")
    _allss_nf_fix_pedido_compra = fields.Binary("NF Estruturas de Fixação")
    _allss_bl_fix_pedido_compra = fields.Binary("Boletos Estruturas de Fixação")
    # GRUPO: PEDIDOS DE VENDA - NOTAS FISCAIS - BOLETOS
    _allss_proposta_pedido_venda_1 = fields.Binary("Proposta SOLARITIMA Assinada - 1")
    _allss_proposta_pedido_venda_2 = fields.Binary("Proposta SOLARITIMA Assinada - 2")
    _allss_proposta_pedido_venda_3 = fields.Binary("Proposta SOLARITIMA Assinada - 3")
    _allss_proposta_pedido_venda_4 = fields.Binary("Proposta SOLARITIMA Assinada - 4")
    _allss_nf_servicos_pedido_venda = fields.Binary("NF Serviços SOLARITIMA")
    _allss_bl_servicos_pedido_venda = fields.Binary("Boletos Serviços SOLARITIMA")
    # GRUPO: DADOS DE MONITORAÇÃO
    _allss_url_monitoracao = fields.Char("URL de Monitoração")
    _allss_login_monitoracao = fields.Char("Login de Monitoração")
    _allss_senha_monitoracao = fields.Char("Senha de Monitoração")
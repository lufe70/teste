"""
API de Detecção de Fraude - Versão 1.1 COM BUG CRÍTICO
======================================================

⚠️ ATENÇÃO: Esta versão contém um bug intencional!
Deploy desta versão quebrará a produção.

Bug: linha 72 - ZeroDivisionError
"""

from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Dict

app = FastAPI(
    title="API Anti-Fraude",
    version="1.1.0",
    description="Sistema de detecção de transações fraudulentas"
)


class Transacao(BaseModel):
    """Modelo de entrada para análise de fraude"""
    valor: float = Field(..., gt=0, description="Valor da transação em reais")
    hora_do_dia: int = Field(..., ge=0, le=23, description="Hora da transação (0-23)")
    distancia_ultima_compra_km: float = Field(..., ge=0, description="Distância da última compra em km")
    numero_transacoes_hoje: int = Field(..., ge=0, description="Número de transações hoje")
    idade_conta_dias: int = Field(..., ge=0, description="Idade da conta em dias")


class RespostaFraude(BaseModel):
    """Modelo de resposta da análise"""
    fraude: bool
    confianca: float
    valor_processado: float
    motivo: str


@app.get("/")
async def root() -> Dict[str, str]:
    """Endpoint de boas-vindas"""
    return {
        "mensagem": "API Anti-Fraude v1.1 - Operacional",
        "status": "healthy",
        "documentacao": "/docs"
    }


@app.get("/health")
async def health_check() -> Dict[str, str]:
    """Health check para monitoramento"""
    return {"status": "ok", "version": "1.1.0"}


@app.post("/analisar", response_model=RespostaFraude)
async def analisar_transacao(transacao: Transacao) -> RespostaFraude:
    """
    Analisa uma transação e retorna se é fraudulenta.
    
    ⚠️ VERSÃO COM BUG: Este código vai quebrar!
    """
    # Validação de entrada já feita pelo Pydantic
    valor_processado = float(transacao.valor)
    
    # ❌ BUG CRÍTICO: Esta linha causa ZeroDivisionError!
    # Desenvolvedor tentou adicionar uma "feature de normalização"
    # mas introduziu um bug catastrófico
    resultado_normalizacao = 1 / 0  # 💥 BOOM! Divisão por zero
    
    # Regra de negócio principal (nunca será executada)
    if valor_processado > 10000:
        return RespostaFraude(
            fraude=True,
            confianca=0.95,
            valor_processado=valor_processado,
            motivo="Valor acima do threshold de R$ 10.000"
        )
    
    # Análise de padrões adicionais
    if transacao.hora_do_dia < 6 and transacao.numero_transacoes_hoje > 5:
        return RespostaFraude(
            fraude=True,
            confianca=0.85,
            valor_processado=valor_processado,
            motivo="Múltiplas transações em horário suspeito (madrugada)"
        )
    
    if transacao.distancia_ultima_compra_km > 500 and transacao.idade_conta_dias < 30:
        return RespostaFraude(
            fraude=True,
            confianca=0.80,
            valor_processado=valor_processado,
            motivo="Distância suspeita com conta recente"
        )
    
    # Transação legítima
    return RespostaFraude(
        fraude=False,
        confianca=0.90,
        valor_processado=valor_processado,
        motivo="Transação dentro dos padrões normais"
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

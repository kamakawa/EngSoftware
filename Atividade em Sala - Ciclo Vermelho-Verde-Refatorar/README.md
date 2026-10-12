# Atividade em Sala - Ciclo Vermelho-Verde-Refatorar

Atividade assíncrona de TDD: um ciclo completo de **Red → Green → Refactor**, terminando com um padrão de projeto aplicado.

**Autor:** Eric Naoki Sugauara Kamakawa
**Curso:** Engenharia de Computação, UTFPR Apucarana
**Linguagem:** Python 3 com pytest

## O componente: calculadora de frete

Calcula o frete de uma loja virtual a partir da modalidade de entrega e do peso do pacote.

| Modalidade | Regra |
|---|---|
| `economico` | R$ 5,00 fixos + R$ 2,00 por kg |
| `expresso` | R$ 15,00 fixos + R$ 3,50 por kg |
| `retirada` | R$ 0,00 |

Erros: peso menor ou igual a zero e modalidade desconhecida levantam `ValueError`.

```python
from frete import calcular_frete

calcular_frete("economico", 2)   # 9.0
calcular_frete("expresso", 2)    # 22.0
calcular_frete("retirada", 10)   # 0.0
```

## Estrutura da pasta

| Arquivo | Conteúdo |
|---|---|
| `test_frete.py` | Plano da atividade (comentário no topo) e testes |
| `frete.py` | Código de produção (versão refatorada com Strategy) e autoavaliação no fim do arquivo |
| `saida_testes.txt` | Saída da execução da suíte após a refatoração |
| `README.md` | Este arquivo |

## Como executar

```bash
pip install pytest
python -m pytest -v
```

## Ciclo de TDD e commits

O histórico segue uma fase por commit, com a fase identificada na mensagem.

| Fase | Commit | O que contém |
|---|---|---|
| Red | `red: testes da calculadora de frete (economico, expresso, retirada)` | Somente `test_frete.py`. A suíte falha porque `frete.py` ainda não existe. |
| Green | `green: implementação direta do calculo de frete com if/elif` | `frete.py` com a solução mais direta, usando `if/elif`. Todos os testes passam. |
| Refactor | `refactor: aplica padrão Strategy no calculo de frete` | `frete.py` reestruturado com Strategy e `saida_testes.txt`. Os testes não foram alterados. |

## Padrão de projeto aplicado: Strategy

Cada modalidade de frete é uma regra de cálculo intercambiável. Na fase verde, todas conviviam em um `if/elif`. Na refatoração, cada regra virou uma classe própria.

| Participante do padrão | Classe no domínio |
|---|---|
| Strategy (interface) | `EstrategiaFrete` |
| ConcreteStrategy | `FreteEconomico`, `FreteExpresso`, `FreteRetirada` |
| Context | `CalculadoraFrete` |

A função `calcular_frete` foi mantida como fachada. Assim, os testes permaneceram idênticos e o comportamento observável não mudou. Para criar uma nova modalidade, basta escrever uma nova estratégia e registrá-la na `CalculadoraFrete`, sem modificar as existentes (princípio Aberto/Fechado).

## Casos de teste

1. Frete econômico: valor fixo mais valor por kg.
2. Frete expresso: valor fixo mais valor por kg.
3. Retirada na loja: sempre gratuita.
4. Peso inválido (0 e -1): `ValueError`.
5. Modalidade desconhecida: `ValueError`.


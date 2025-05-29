# Gestão de Consumo de Água, Energia e Gás.
Sistema com o objetivo de monitorar e gerenciar o consumo de água, energia elétrica e gás em residências.

Desenvolvido pelo Grupo 3:
David Duarte,
Danilson Gonçalves,
Wilker Lopes
e Rafael Fortes.

Displina: Metodologias Ágeis de Desenvolvimento de Software 

Curso: Tecnologias de informação, Web e Multimédia – 2º ano

Exemplos:
# Sistema de Monitoramento Residencial de Consumo

Este sistema permite o **registro, validação, monitoramento e geração de relatórios** sobre o consumo de **água, energia e gás** em diferentes residências. Ideal para análises de eficiência energética e sustentabilidade doméstica.

## 🔧 Funcionalidades

* Cadastro de casas com localização, morada e certificado energético;
* Registro de consumo por tipo ("agua", "energia", "gas"), com validação dos dados;
* Geração de relatórios gerais e individuais;
* Detecção de erros/inconsistências nos dados;
* Exibição em tabelas formatadas com `tabulate`;
* Informação sobre o período de maior gasto por tipo de consumo.

## ✨ Instalação

```bash
pip install tabulate
```

> Requer Python 3.7+

## ⚙️ Como usar

```python
from sistema import ControladorCasas

# Criar o sistema
data = ControladorCasas()

# Adicionar casas
data.adicionar_casa("001", 41.1578, -8.6299, "Rua do Porto 123", "A+", "Casa Central")

# Registrar consumo
data.registrar_consumo("001", "agua", "01/2025", 15000, 45.75)
data.registrar_consumo("001", "energia", "01/2025", 350, 120.50)

# Listar consumo
data.listar_consumo("001", "agua")

# Gerar relatórios gerais e individuais
data.gerar_relatorio_geral()
data.gerar_relatorio_individual()

# Verificar consistência dos dados
data.verificar_integridade()
```

## 🔹 Tipos de consumo válidos

* `agua`
* `energia`
* `gas`

## ⏳ Formato do período

* Sempre no formato `"MM/AAAA"` (ex: `"01/2025"`)

## 🔹 Certificados energéticos aceitos

```
"A+", "A", "B", "B-", "C", "D", "E", "F", "G"
```

## 📂 Estrutura do Projeto

* `Casa`: representa uma residência com atributos e consumos;
* `ControladorCasas`: gerencia o conjunto de casas e relatórios;
* `Validador`: garante que os dados inseridos sejam coerentes;
* `GeradorTabelas`: imprime dados formatados com `tabulate`.

## 🚫 Validações automáticas

* Certificados inválidos são rejeitados no cadastro;
* Coordenadas fora do intervalo geográfico válido são rejeitadas;
* Consumos com valores ou custos negativos são sinalizados;
* Períodos duplicados para o mesmo tipo de consumo são impedidos.

## ⚠️ Observações

* O sistema ainda aceita dados com erros *após aviso*, para fins de auditoria ou testes.
* Todos os relatórios são exibidos diretamente no terminal com formatação visual.

---

🚀 *Contribuições são bem-vindas! Sugestões, melhorias e pull requests podem ser enviados via GitHub.*

from .main import ControladorCasas

def main():
    sistema = ControladorCasas()
    sistema.adicionar_casa("001", 41.1578, -8.6299, "Rua do Porto 123", "A+", "Casa Central")
    sistema.gerar_relatorio_geral()

import colorama
from colorama import Fore, Style

# Inicializa o colorama para garantir compatibilidade no Windows
colorama.init()

def monitorar_reservatorio(nivel):
    """
    Define a cor e exibe a mensagem com base no nível do reservatório.
    """
    
    # Lista de situações conforme o enunciado
    situacoes = [
        "Nível 1: Muito baixo (crítico)",
        "Nível 2: Baixo",
        "Nível 3: Médio",
        "Nível 4: Alto",
        "Nível 5: Muito alto (alerta)"
    ]
    
    # Mapeamento de cores
    cores = {
        1: Fore.RED,
        2: Fore.YELLOW,
        3: Fore.GREEN,
        4: Fore.CYAN,
        5: Fore.BLUE
    }

    # Busca a cor correspondente ou mantém o padrão caso o nível seja inválido
    cor_selecionada = cores.get(nivel, Fore.WHITE)
    
    # Acessa a mensagem na lista (ajustando o índice para começar em 0)
    mensagem = situacoes[nivel - 1]

    # Exibição formatada
    print(f"{cor_selecionada}{mensagem}{Style.RESET_ALL}")

# Simulação do monitoramento
if __name__ == "__main__":
    print("--- Sistema de Monitoramento de Reservatório ---")
    
    # Simulando a leitura de todos os níveis
    niveis_para_testar = [1, 2, 3, 4, 5]
    
    for n in niveis_para_testar:
        monitorar_reservatorio(n)
        
    print("------------------------------------------------")

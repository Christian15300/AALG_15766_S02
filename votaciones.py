def contar_votos():
    # Inicializamos un diccionario para contar los votos de cada candidato
    votos = {1: 0, 2: 0, 3: 0, 4: 0}
    total_votos = 0

    print("Ingrese los votos de los candidatos y termine con un 0")

    while True:
        voto = int(input())
        if voto == 0:
            break
        elif voto in votos:
            votos[voto] += 1
            total_votos += 1
        else:
            print("Voto invávlido" + "" + "Por favor Ingrese un número entre 1 y 4")

    print("\nResultados de la elección:")
    for candidato in range(1, 5):
        if total_votos > 0:
            porcentaje = (votos[candidato] / total_votos) * 100
        else:
            porcentaje = 0
        print(f"Candidato {candidato}: {votos[candidato]} votos, {porcentaje:.2f}% del total")

contar_votos()



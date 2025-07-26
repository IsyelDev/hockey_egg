from pathlib import Path
import calendar

def crearCarpeta():
    anios = [2025, 2026, 2027]
    meses = ["Julio", "Agosto", "Setiembre", "Octubre", "Noviembre", "Diciembre"]

    for anio in anios:  # Año
        mes_numero = 7
        for mes in meses:  # Mes
            ruta_mes = Path(str(anio)) / mes
            ruta_mes.mkdir(parents=True, exist_ok=True)
            dias = calendar.monthrange(anio, mes_numero)[1]
            for dia in range(1, dias + 1):  #$DIA
                Path(ruta_mes / f"{dia}-{mes_numero}-{str(anio)[-2:]}").mkdir(exist_ok=True)
            mes_numero += 1

if __name__ == "__main__":
    crearCarpeta()







"""
Diseño de Software 2026-2 - Semana 1
Tema: Fundamentos del diseño: abstracción, modularidad, arquitectura y ocultamiento
Ejecute: python semana_01_base.py
"""

# Semana 1: mapa simple de módulos
modulos = {
    "usuarios": ["registrar", "autenticar"],
    "viajes": ["solicitar", "asignar_conductor"],
    "pagos": ["calcular_tarifa", "registrar_pago"]
}
for nombre, acciones in modulos.items():
    print(f"Módulo {nombre}: {', '.join(acciones)}")

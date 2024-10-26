import pytest
from datetime import datetime
from sapiencia.registro_horas import RegistroHoras, RegistroAsistencia, RegistroError


def test_agregar_horas():
    registro_horas = RegistroHoras()
    registro_horas.agregar_horas(5, "Tarea A")
    assert registro_horas.total_horas() == 5
    assert registro_horas.horas_registradas[0]["Horas"] == 5
    assert registro_horas.horas_registradas[0]["Info"] == "Tarea A"


def test_reducir_horas():
    registro_horas = RegistroHoras()
    registro_horas.agregar_horas(10)
    registro_horas.reducir_horas(3)
    assert registro_horas.total_horas() == 7


def test_reducir_horas_exceso():
    registro_horas = RegistroHoras()
    registro_horas.agregar_horas(5)
    with pytest.raises(RegistroError, match="No puedes reducir más horas de las que tienes registradas."):
        registro_horas.reducir_horas(10)


def test_agregar_horas_invalido():
    registro_horas = RegistroHoras()
    with pytest.raises(RegistroError, match="Las horas deben ser un número entero positivo."):
        registro_horas.agregar_horas(-5)


def test_registrar_asistencia():
    registro_asistencia = RegistroAsistencia()
    registro_asistencia.registrar_asistencia("Juan", "2024-10-25", "Presente")
    assert len(registro_asistencia.asistencias) == 1
    assert registro_asistencia.asistencias[0]["Nombre"] == "Juan"
    assert registro_asistencia.asistencias[0]["Estado"] == "Presente"


def test_registrar_asistencia_fecha_invalida():
    registro_asistencia = RegistroAsistencia()
    with pytest.raises(RegistroError, match="Formato de fecha inválido. Use 'YYYY-MM-DD'."):
        registro_asistencia.registrar_asistencia("Juan", "25-10-2024", "Presente")


def test_registrar_asistencia_estado_invalido():
    registro_asistencia = RegistroAsistencia()
    with pytest.raises(RegistroError, match="Estado no válido. Debe ser 'Presente' o 'Ausente'."):
        registro_asistencia.registrar_asistencia("Juan", "2024-10-25", "Desconocido")

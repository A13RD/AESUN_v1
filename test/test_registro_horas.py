import pytest
from sapiencia.registro_horas import RegistroHoras, RegistroAsistencia, RegistroError


# RegistroHoras
class TestRegistroHoras:
    def test_agregar_horas_valido(self):
        registro = RegistroHoras()
        registro.agregar_horas(5)
        assert registro.total_horas() == 5

    def test_agregar_horas_invalido(self):
        registro = RegistroHoras()
        with pytest.raises(RegistroError, match="Las horas deben ser un número entero positivo."):
            registro.agregar_horas(-3)

    def test_reducir_horas_valido(self):
        registro = RegistroHoras()
        registro.agregar_horas(5)
        registro.reducir_horas(3)
        assert registro.total_horas() == 2

    def test_reducir_horas_exceso(self):
        registro = RegistroHoras()
        registro.agregar_horas(2)
        with pytest.raises(RegistroError, match="No puedes reducir más horas de las que tienes registradas."):
            registro.reducir_horas(5)


# RegistroAsistencia
class TestRegistroAsistencia:
    def test_registrar_asistencia_valida(self):
        registro = RegistroAsistencia()
        registro.registrar_asistencia("Juan", "2023-10-10", "Presente")
        assert len(registro.asistencias) == 1
        assert registro.asistencias[0]["Nombre"] == "Juan"
        assert registro.asistencias[0]["Fecha"] == "2023-10-10"
        assert registro.asistencias[0]["Estado"] == "Presente"

    def test_registrar_asistencia_estado_invalido(self):
        registro = RegistroAsistencia()
        with pytest.raises(RegistroError, match="Estado no válido. Debe ser 'Presente' o 'Ausente'."):
            registro.registrar_asistencia("Ana", "2023-10-10", "Tarde")

    def test_registrar_asistencia_fecha_invalida(self):
        registro = RegistroAsistencia()
        with pytest.raises(RegistroError, match="Formato de fecha inválido. Use 'YYYY-MM-DD'."):
            registro.registrar_asistencia("Luis", "10-10-2023", "Ausente")

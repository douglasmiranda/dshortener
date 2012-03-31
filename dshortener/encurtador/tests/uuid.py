from django.test import TestCase
from encurtador.util import UUIDCurto


class UUIDCurtoTest(TestCase):
    def setUp(self):
        self.uuid = UUIDCurto()

    def test_deve_transformar_um_inteiro_em_uuid_e_retornar_ao_valor_original(self):
        inteiro = 11523562
        uuidcurto = self.uuid.codificar(inteiro)
        self.assertEqual(inteiro, self.uuid.decodificar(uuidcurto))
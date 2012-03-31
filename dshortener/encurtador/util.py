class UUIDCurto(object):
    def __init__(self, alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
        self.alfabeto = alfabeto

    def codificar(self, inteiro):
        if not inteiro: return self.alfabeto[0]
        uuid = ''
        while inteiro > 0:
            inteiro, r = divmod(inteiro, len(self.alfabeto))
            uuid = self.alfabeto[r] + uuid
        return uuid
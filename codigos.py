class Codigos:
    codigo = {'a': '0000', 'b': '0001', 'c': '0010', 'd': '0011','e':'0100','f':'0101','g':'0110','h':'0111',
              'i':'1000','j':'1001','k':'1010','l':'1011','m':'1100','n':'1101','o':'1110','p':'1111'}

    def getCodigo(self, cod):
        return self.codigo[cod]

    def getCodigoSecuencia(self, cod):
        primera = self.codigo[cod][0]
        segunda = self.codigo[cod][1]
        tercera= self.codigo[cod][2]
        cuarta= self.codigo[cod][3]
        return primera, segunda, tercera, cuarta

    def getCaracter(self, cod):
        for secuencia in self.codigo:
            if cod == self.codigo[secuencia]:
                return secuencia
        return "error"	
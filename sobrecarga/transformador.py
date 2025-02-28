class Transformador:
  def transformar(self, *args, factor = None):
    if factor:
      numeros = []

      for n in args:
        numeros.append(n * factor)

      return numeros

    else:
      numero = 0

      for n in args:
        numero += n

      return numero

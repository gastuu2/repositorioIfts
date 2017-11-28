import csv

def validate(archivo):
	CAMPOS=5
	
	class LongRegInvalidError(Exception):
		pass

	class CampoVacioError(Exception):
		pass
	try:
		with open(archivo) as archivo:
			archivo = csv.reader(archivo)
			registro = 1
			campo = 1
			for linea in archivo:
				if len (linea) == CAMPOS:
					x = 0
					for x in range(CAMPOS):
						campo = x + 1
						if linea[x] == '':
							error= 'Campo {} vacio en el registro {}'.format(campo, registro)
							raise CampoVacioError(error)
						else:
							pass
						if registro == 1:
							columna = linea[x]
							if columna == 'PRECIO':
								campo_precio = x
							elif columna =='CANTIDAD':
								campo_cantidad = x
							else:
								pass                 
						else:
							if x == campo_cantidad:
								val_columa = int(float(linea[x]))
							elif x == campo_precio:
								columna = linea[x]
								if columna.isdigit() == True:
									raise ValueError() 
								else:
									f = float(linea[x])
							else:
								pass
				else:
					raise LongRegInvalidError()
				registro = registro + 1
	
	except LongRegInvalidError:
		mensaje = '{} Longitud de registro invalido'.format(linea)
		print(mensaje)
		with open('error.log','w') as error_file:
			error_file.write(mensaje)
	except ValueError:
		if x == campo_precio:
			print('El campo CANTIDAD tiene un registro incorrecto {}'.format(registro))
		else:
			print('El campo PRECIO tiene un registro incorrecto {}'.format(registro, x))
	except FileNotFoundError:
		print('El archivo inexistente')
		
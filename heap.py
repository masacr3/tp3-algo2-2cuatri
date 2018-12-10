import os
def compare(a,b):
	return (a>b)-(a<b)

class Heap:
	def __init__(self,f_cmp):
		self.cant = 0
		self.datos = []
		self.cmp = f_cmp

	def __len__(self):
		return self.cant

	def cantidad(self):
		return self.cant

	def esta_vacio(self):
		return self.cant == 0

	def _upheap(self,pos):
		if pos==0: return
		pos_padre = (pos-1)//2
		if self.cmp(self.datos[pos],self.datos[pos_padre]) > 0: return
		self.datos[pos],self.datos[pos_padre] = self.datos[pos_padre],self.datos[pos]
		self._upheap(pos_padre)

	def _downheap(self,pos):
		if pos >= self.cant : return
		pos_h_izq = (2*pos)+1
		pos_h_der = (2*pos)+1
		pos_min = pos
		if pos_h_izq < self.cant and self.cmp(self.datos[pos_h_izq],self.datos[pos_min]) < 0 :
			pos_min = pos_h_izq
		if pos_h_der < self.cant and self.cmp(self.datos[pos_h_der],self.datos[pos_min]) < 0 :
			pos_min = pos_h_der
		if pos != pos_min:
			self.datos[pos],self.datos[pos_min]=self.datos[pos_min],self.datos[pos]
			self._downheap(pos_min)
		return

	def encolar(self,dato):
		if dato is None: return False
		self.datos.append(dato)
		self._upheap(self.cant)
		self.cant+=1
		return True

	def ver_min(self):
		if self.esta_vacio(): return None
		return self.datos[0]

	def desencolar(self):
		if self.esta_vacio(): return None
		elem = self.datos.pop(0)
		self.cant-=1
		self._downheap(0)
		return elem

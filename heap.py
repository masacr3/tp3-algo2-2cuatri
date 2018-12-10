import os
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

	def _upheap(self,datos,pos,cmp):
		if pos==0: return
		pos_padre = (pos-1)//2
		if cmp(datos[pos],datos[pos_padre]) > 0: return
		datos[pos],datos[pos_padre] = datos[pos_padre],datos[pos]
		self._upheap(datos,pos_padre,cmp)

	def _downheap(self,datos,n,pos,cmp):
		if pos >= n : return
		pos_h_izq = (2*pos)+1
		pos_h_der = (2*pos)+1
		pos_min = pos
		if pos_h_izq < n and cmp(datos[pos_h_izq],datos[pos_min]) < 0 :
			pos_min = pos_h_izq
		if pos_h_der < n and cmp(datos[pos_h_der],datos[pos_min]) < 0 :
			pos_min = pos_h_der
		if pos != pos_min:
			datos[pos],datos[pos_min]=datos[pos_min],datos[pos]
			self._downheap(datos,n,pos_min,cmp)
		return

	def heapify(self,arr,n,cmp):
		for x in range(n,0,-1):
			self._downheap(datos,x-1,cmp)

	def encolar(self,dato):
		if dato is None: return False
		self.datos.append(dato)
		self._upheap(self.datos,self.cant,self.cmp)
		self.cant+=1
		return True

	def ver_min(self):
		if self.esta_vacio(): return None
		return self.datos[0]

	def desencolar(self):
		if self.esta_vacio(): return None
		elem = self.datos.pop(0)
		self.cant-=1
		self._downheap(self.datos,self.cant,0,self.cmp)
		return elem

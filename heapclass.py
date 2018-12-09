import os

def upheap(datos,pos,cmp):
	if pos==0: return
	pos_padre = (pos-1)//2
	if cmp(datos[pos],datos[pos_padre]) < 0: return
	datos[pos],datos[pos_padre] = datos[pos_padre],datos[pos]
	upheap(datos,pos_padre,cmp)

def downheap(datos,n,pos,cmp):
	if pos >= n : return
	pos_h_izq = (2*pos)+1
	pos_h_der = (2*pos)+1
	pos_max = pos
	if pos_h_izq < n and cmp(datos[pos_h_izq],datos[pos_max]) > 0 :
		pos_max = pos_h_izq
	if pos_h_der < n and cmp(datos[pos_h_der],datos[pos_max]) > 0 :
		pos_max = pos_h_der
	if pos != pos_max:
		datos[pos],datos[pos_max]=datos[pos_max],datos[pos]
		downheap(datos,n,pos_max,cmp)
	return

def heapify(arr,n,cmp):
	for x in range(n,0,-1):
		downheap(datos,x-1,cmp)

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

	def encolar(self,dato):
		if dato is None: return False
		self.datos.append(dato)
		upheap(self.datos,self.cant,self.cmp)
		self.cant+=1
		return True

	def ver_max(self):
		if self.esta_vacio(): return None
		return self.datos[0]

	def desencolar(self):
		if self.esta_vacio(): return None
		elem = self.datos.pop(0)
		self.cant-=1
		downheap(self.datos,self.cant,0,self.cmp)
		return elem

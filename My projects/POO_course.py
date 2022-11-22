class Personne(object):
	"""ce programme est une simulation d'un homme"""
	def __init__(self, nom= "Kassi",age= 19,taille= 1.65,fonction="Etudiant"):
		self.nom = str(nom)
		self.age = int(age)
		self.taille = float(taille)
		self.fonction = str(fonction)

	def se_presenter(self):
		print("Je m'appelle {} et j'ai {} je mésure {} et je suis {}".format(self.nom,self.age,self.taille,self.fonction))



b = Personne(nom="kennel",age=19,taille=1.65,fonction="Etudiant")
a = Personne.se_presenter(self="n")

		
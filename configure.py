from json import load,dump

class Config:
	def __init__(self):
		self.title = "Library"
		self.data_place = "data_stock.json"
		self.data_satuan = 'satuan.json'

		#WINDOW CONF
		base = 100
		ratio = (9, 6)
		self.width = base*ratio[0]
		self.height = base*ratio[1]
		self.screen = f"{self.width}x{self.height}+350+100"
		self.Read_data()
		self.Read_satuan_data()

	def Read_data(self):
		with open(self.data_place,'r') as data_place:
			self.data = load(data_place)

	def Write_Data(self,place,data):	
		with open(place,'w') as data_place:
			dump(data,data_place)

	def Read_satuan_data(self):
		with open(self.data_satuan,'r') as data_place:
			self.satuan = load(data_place)


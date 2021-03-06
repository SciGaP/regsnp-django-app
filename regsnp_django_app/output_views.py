##IMPORTS FOR LOGOS START######################
import pandas
from collections import OrderedDict
from collections import Counter
import numpy
import matplotlib.pyplot as plt
import logomaker
import io


##IMPORTS FOR LOGOS ENDING####################



import io
import os


import numpy as np
#import pandas


from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from urllib.parse import quote
from django.urls import reverse
from django.template.loader import render_to_string

#getting files loaded
#from airavata_django_portal_sdk import user_storage

from airavata_django_portal_sdk import urls
#urls.get_download_url()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class SplicePredLink:
	display_type = "link"
	immediate = True
	name = "Splicing Output"
	
	#print("FILE URL",link)
	def generate_data(self, request, experiment_output, experiment, output_file=None):
		link = urls.get_download_url(experiment_output.value)
		return {
			"label": "Output Visualization",
			"url": "https://regsnps.ccbb.iupui.edu/regsnp_django_app/expviz/?=https://regsnps.ccbb.iupui.edu"+link,
		}
		
		
class SplicePredTable:
	display_type = 'html'
	name = 'Splicing Table'
	# Optionally provide path to a file to test with when data isn't available
	# locally
	# fixture_output_file = ""

	def generate_data(self, request, experiment_output, experiment, output_file=None):
		link = urls.get_download_url(experiment_output.value)
		print("FILE URL",link)
		return {
			'output': render_to_string(
				
				'regsnp_django_app/splicetable.html', {'outputFilePath' : link}),
			'js':"/static/js/datatable.js"
			}
			
class irneoOut:
	display_type = 'html'
	name = 'irneoOut'
	# Optionally provide path to a file to test with when data isn't available
	# locally
	# fixture_output_file = ""

	def generate_data(self, request, experiment_output, experiment, output_file=None):
		link = urls.get_download_url(experiment_output.value)
		print("FILE URL",link)
		return {
			'output': render_to_string(
				
				'regsnp_django_app/irneoView.html'),
			'js':"/static/js/irneo.js"
			}
			
			
class SplicePlot:
	display_type = 'image'
	name = "SplicePlot"
	def generate_data(self, request, experiment_output, experiment, output_file=None):
		#print('THIS IS MY TYPE',type(experiment_output.value))
		#print('value',experiment_output.value)
		#print('directory',os.getcwd())
		#df=pandas.read_csv(output_file)
		#print('HEY THERE IM HERE',df.columns)
		
		#plt.plot([0,1,2],[1,1.25,1.7])

		# Export plot as image buffer
		#buffer = io.BytesIO()
		#plt.savefig(buffer, format='png')
		#image_bytes = buffer.getvalue()
		#buffer.close()

		# return dictionary with image data
		return {
			'image': image_bytes,
			'mime-type': 'image/png'
		}
		
class irneoSeq:
	display_type = 'image'
	name = "irneoSeq"
	def generate_data(self, request, experiment_output, experiment,output_file=None):
		#print('output_file type',type(output_file))
		df=pandas.read_csv(output_file.read().decode())
		#os.path.join(os.path.dirname(output_file.name)
		#df=pandas.read_csv(experiment_output.value)
		#print('value',experiment_output.value)
		#link = urls.get_download_url(experiment_output.value)
		#print("FILE URL",link)
		#print('directory',os.getcwd())
		#dfTest=pandas.read_json(output_file.read().decode())
		#print(dfTest.head())
		#print('contents',os.listdir('django_airavata/static'))
		
		#os.system('wget localhost:8000/api/download?data-product-uri=airavata-dp%3A%2F%2Fa4d1e8cf-3879-469e-b391-bac0d953f72e')
		

		
		plt.plot(x,y)
		
		buffer = io.BytesIO()
		plt.savefig(buffer, format='png')
		image_bytes = buffer.getvalue()
		buffer.close()
		return {
			'image': image_bytes,
			'mime-type': 'image/png'
		}
		




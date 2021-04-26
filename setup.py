import setuptools

setuptools.setup(
	name="regsnp_django_app",
	version="0.0.1",
	description="Custom output viewer and django app for regsnp_django_app",
	packages=setuptools.find_packages(),
	install_requires=[
		'django>=1.11.16',
		'cclib',
		'numpy',
		'matplotlib',
		'psycopg2',
		'periodictable',
		'scipy',
		'dash',
		'pandas',
		'cclib',
		'logomaker'

	],
	entry_points="""
[airavata.output_view_providers]
splice-pred-table = regsnp_django_app.output_views:SplicePredTable
splice-pred-link = regsnp_django_app.output_views:SplicePredLink
splice-plot = regsnp_django_app.output_views:SplicePlot
irneo-plot = regsnp_django_app.output_views:irneoOut
irneo-seq = regsnp_django_app.output_views:irneoSeq
[airavata.djangoapp]
regsnp_django_app = regsnp_django_app.apps:RegSnpAppConfig
""",
)

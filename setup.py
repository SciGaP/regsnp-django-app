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
		'periodictable',
		'scipy',
		'dash',
		'pandas',
		'logomaker'

	],
	entry_points="""
[airavata.output_view_providers]
splice-pred-link = regsnp_django_app.output_views:SplicePredLink
irneo-seq = regsnp_django_app.output_views:irneoSeq
[airavata.djangoapp]
regsnp_django_app = regsnp_django_app.apps:RegSnpAppConfig
""",
)




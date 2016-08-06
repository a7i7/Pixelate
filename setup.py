from setuptools import setup

setup(
	name='Pixelate',
	version='1.0',
	author='Afif Ahmed',
	author_email='getafif22@gmail.com',
	url='https://github.com/a7i7/Pixelate',
	packages=['pixelate'],
	description='Pixelate will distort images and pixelate them with various effects of your choice.',
	install_requires=['click','tqdm'],
	entry_points={
		'console_scripts': [
			'pixelate = pixelate.cli:main'
		]
	},
)
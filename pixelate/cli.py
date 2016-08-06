import click
import pixelate
import os

@click.command()
@click.argument('image_path', required=True, type=click.Path(dir_okay=False,
                                                        exists=True,
                                                        resolve_path=True))
@click.argument('effect', required=True, type=str)
@click.option('--size', default=10, type=int,
              help='Length of side of each square in pixelated image')
@click.option('--output',default=None, type=click.Path(dir_okay=False),
			   help='specify output file')

def main(image_path,effect,size,output):
	"""
	Pixelate will distort images and pixelate it with various effects.
	Choose from the following effects:
	fill, mushy, lumen-center, lumen-side, mushy, smoke, 256-colors
	"""
	image_path = os.path.realpath(image_path)
	if output==None:
		dot_index = image_path.rfind('.')
		output = image_path[0:dot_index]+'_pixelated'+image_path[dot_index:]
	output = os.path.realpath(output)
	pixelate.main(image_path,size,effect,output)


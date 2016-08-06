# Pixelate

### What is it?
Pixelate is a python program that will make your image look like it has been broken up into pixels. There are are a variety of effects that you can choose from.

### Requirements
* Python 2
* Python modules: click,tqdm

### Installation
Install from source
```shell
git clone https://github.com/a7i7/Pixelate.git
cd Pixelate
python setup.py install
```

### Usage
```
Usage: pixelate [OPTIONS] IMAGE_PATH EFFECT

  Pixelate will distort images and pixelate it with various effects. Choose
  from the following effects: fill, mushy, lumen-center, lumen-side, mushy,
  smoke, 256-colors

Options:
  --size INTEGER  Length of side of each square in pixelated image
  --output PATH   specify output file
  --help          Show this message and exit.
```

### Examples
#### Original Pic
![Original Pic](http://www.wallpapermania.eu/images/lthumbs/2012-07/3233_Small-red-fruits-close-up-HD-wallpaper.jpg)
#### Pixelate with fill effect 
```shell
pixelate image.jpg fill
```
![After pixelating with fill effect](http://i64.tinypic.com/34y8opl.jpg)

#### Pixelate with lumen-center effect 
```shell
pixelate image.jpg lumen-center
```
![After pixelating with lumen-center effect](http://i66.tinypic.com/dep4s1.jpg)

#### Pixelate with lumen-side effect 
```shell
pixelate image.jpg lumen-side
```
![After pixelating with lumen-side effect](http://i65.tinypic.com/2qbrnvb.jpg)

#### Pixelate with smoke effect 
```shell
pixelate image.jpg smoke
```
![After pixelating with smoke effect](http://i66.tinypic.com/2n17x4g.jpg)

#### Pixelate with 256-colors effect 
```shell
pixelate image.jpg 256-colors
```
![After pixelating with 256-colors effect](http://i65.tinypic.com/2r4ixea.jpg)


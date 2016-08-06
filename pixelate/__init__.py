import sys
from Pixelator import Pixelator
import PixelEffect
class EffectType:
    plain_fill = "fill"
    mushy_effect = "mushy"
    lumen_center = "lumen-center"
    lumen_side = "lumen-side"
    colors_256_effect = "256-colors"
    smoke_effect = "smoke"

def main(image_path, pixel_size, pixel_effect_name, output):
    
    if pixel_effect_name==EffectType.plain_fill:
        pixel_effect = PixelEffect.PixelEffect(
                        PixelEffect.PlainFill(pixel_size) )

    elif pixel_effect_name==EffectType.mushy_effect:
        pixel_effect = PixelEffect.PixelEffect(
                        PixelEffect.MushyEffect(pixel_size) )

    elif pixel_effect_name==EffectType.lumen_center:
        pixel_effect = PixelEffect.PixelEffect(
                        PixelEffect.LumenCenterEffect(pixel_size) )

    elif pixel_effect_name==EffectType.lumen_side:
        pixel_effect = PixelEffect.PixelEffect(
                        PixelEffect.LumenSideEffect(pixel_size) )

    elif pixel_effect_name==EffectType.colors_256_effect:
        pixel_effect = PixelEffect.PixelEffect(
                        PixelEffect.Colors256Effect(pixel_size) )

    elif pixel_effect_name==EffectType.smoke_effect:
        pixel_effect = PixelEffect.PixelEffect(
                        PixelEffect.SmokeEffect(pixel_size) )

    else:
        print "No such effect as %s" %pixel_effect_name
        sys.exit(0)

    pixelator = Pixelator(image_path,pixel_size,pixel_effect)
    print "Pixelating image and applying effects..."
    pixelated_image = pixelator.get_pixelated_image()
    print "Writing to %s" %output
    try:
        pixelated_image.save(output)
    except IOError:
        print "Could not save to %s. Invalid path" %output

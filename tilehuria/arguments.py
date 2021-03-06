#!/usr/bin/python3
"""
Set of arguments and defaults for creation of MBTiles. In separate file to 
ensure that the arguments and defaults are consistent in all scripts.
"""
# Ivan Buendia Gayton, Humanitarian OpenStreetMap Team/Ramani Huria, 2018

def argumentlist():
    """Returns a list with a set of global arguments and defaults"""
    arguments = [ # shortarg, longarg, action, helpstring, defaultvalue
    ('minz', 'minzoom', None,
     'Minimum tile level desired.',
     16),
    ('maxz', 'maxzoom', None,
     'Maximum tile level desired.',
     20),
    ('z', 'zoom', None,
     'tile zoom level if only one level desired.',
     16),
    ('url', 'url_template', None,
     'JOSM-style URL template for tileserver.',
     None),
    ('ts', 'tileserver', None,
     'A server where the tiles can be downloaded:'
     ' osm, maxar_standard, maxar_premium, bing, etc.',
     'osm'),
    ('f', 'format', None,
     'Output tile format: PNG, JPEG, or JPG',
     'JPG'),
    ('cs', 'colorspace', None,
     'Color space of tile format: RGB or YCBCR.',
     'RGB'),
    ('q', 'quality', None,
     'JPEG compression quality setting.', None),
    ('t', 'type', None,
     'Layer type: overlay or baselayer.',
     'overlay'),
    ('d', 'description', None,
     'Describe it however you like!',
     'An MBTiles tileset'),
    ('a', 'attribution', None,
     'Should state data origin.',
     'Copyright of the tile creator'),
    ('ver', 'version', None,
     'The version number of the tileset (the actual data, not the program)',
     1.0),
    ('v', 'verbose', 'store_true',
     'Use if you want to see a lot of command line output flash by!',
     None),
    ('c', 'clean', 'store_true',
     'Delete intermediate files.',
     None),
    ('yr', 'y-reverse', 'store_false',
     'Y tile coordinate counts from bottom up, rather than default top down.',
     None),
    ('od', 'output_dir', None,
     'Output directory for read or downloaded tiles',
     None)
    ]
    return arguments

def set_defaults(opts):
    """Set sensible default options for MBTile creation. Does not modify 
       any values passed in, only uses defaults if values are None or absent.
       Operates on a dict.
    """
    # DEBUGGING OPTS
    # print('\nOpts received by set_defaults: {}\n'.format(opts))
    
    arguments = argumentlist()
    for shortarg, longarg, action, helpstring, defaultvalue in arguments:
        opts[longarg] = defaultvalue if not opts.get(longarg) else opts[longarg]
    return opts

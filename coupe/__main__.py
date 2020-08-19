import sys

from textx.exceptions import TextXSemanticError, TextXSyntaxError

from . import model_from_file, Model

if __name__ == '__main__':
    try:
        model: Model = model_from_file('examples/test1.cue')
    except (TextXSemanticError, TextXSyntaxError) as error:
        print(error.message)
        sys.exit(1)

    for info in model.infos:
        print(f'{info} {model.infos[info].value}')
    for _file in model.files:
        print(f'FILE {_file} {model.files[_file].filetype}')
        for track in model.files[_file].tracks:
            print(f' * TRACK {track.number} {track.datatype}')
            for info in track.infos:
                print(f'  - {info.name} {info.value}')

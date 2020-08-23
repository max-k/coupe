from textx import metamodel_from_str
from textx.metamodel import TextXMetaModel

from .grammar import GRAMMAR
from .model_processors import _check_unicity
from .object_processors import OBJECT_PROCESSORS


class Model:
    def __init__(self, model) -> None:
        self.model = model
        self.files = {}
        self.infos = {}
        self._split_album_infos_from_files()

    def _split_album_infos_from_files(self) -> None:
        for command in self.model.commands:
            if command.__class__.__name__ == 'File':
                self.files[command.name] = command
            else:
                self.infos[command.name] = command


def model_from_file(model_path: str) -> Model:
    metamodel: TextXMetaModel = metamodel_from_str(GRAMMAR)

    for command_name in ['catalog', 'cdtextfile']:
        metamodel.register_model_processor(_check_unicity(command_name))
    metamodel.register_obj_processors(OBJECT_PROCESSORS)

    return Model(metamodel.model_from_file(model_path))

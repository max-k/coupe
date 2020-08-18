from textx.exceptions import TextXSemanticError


def _check_unicity(command_name):
    command_name = command_name.upper()

    def processor_function(model, metamodel):
        entries = filter(
                        lambda x: x.name == command_name,
                        [*model.infos, *model.commands]
                    )
        if len(list(entries)) > 1:
            error_text = f"{command_name} command can appear only once."
            raise TextXSemanticError(error_text)
    return processor_function

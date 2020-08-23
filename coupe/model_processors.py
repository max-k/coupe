from textx.exceptions import TextXSemanticError


def _check_unicity(command_name):
    command_name = command_name.upper()

    def processor_function(model, metamodel):
        if [x.name for x in model.commands].count(command_name) > 1:
            error_text = f"{command_name} command can appear only once."
            raise TextXSemanticError(error_text)
    return processor_function

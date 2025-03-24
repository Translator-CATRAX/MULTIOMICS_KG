from copy import deepcopy
import yaml
import sys
import os


def fast_extension(filename: str) -> str:
    """
    Returns the file extension of the given filename (last 4 characters,
    converted to lower case).
    """
    return filename[-4:].lower()


def exit_with_error(msg: str) -> None:
    print(msg)
    sys.exit(1)

def nice_it() -> None:
    os.nice(8)


def get_sections(section_config: dict) -> list:
    """
    Gets all sections from a configuration dictionary.

    If the configuration dictionary contains a "sections" key, it is
    assumed to be a list of dictionaries, where each dictionary is a
    configuration for one section. The function will return a list of
    these section configurations, with appropriate merging.

    If the configuration dictionary does not contain a "sections" key,
    it is assumed to be a configuration for one section, and the
    function will return a list with this one section configuration.

    :param section_config: The configuration dictionary
    :return: A list of section configurations
    """
    if "sections" not in section_config:
        return [section_config]

    sections = []
    for section in section_config["sections"]:
        section_copy = deepcopy(section_config)

        # Merge the current section with the base configuration
        updates = {
            key: (
                value if key not in section_copy else (
                    section_copy[key] + value
                    if isinstance(section_copy[key], list) else (
                        section_copy[key].update(value) or section_copy[key]
                        if isinstance(section_copy[key], dict) else value)))
            for key, value in section.items()}

        section_copy.update(updates)
        sections.append(section_copy)

    return sections


def read_config(filename: str) -> dict:
    try:
        with open(filename) as opened_yaml:
            return yaml.load(opened_yaml, Loader=yaml.CSafeLoader)
    except yaml.YAMLError as e:
        exit_with_error("YAML Error: " + str(e))

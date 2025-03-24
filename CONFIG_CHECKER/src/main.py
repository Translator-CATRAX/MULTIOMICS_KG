from src.utils import (
    toolkit, kg_config_parser,
    table_config_parser, arguments)
import sys


def table_config_main() -> None:
    """
    Main function to parse and validate table configuration.

    This function enforces correct script usage, reads the table
    configuration from a YAML file, and validates each section of
    the configuration.

    :raises IndexError: If the number of arguments is invalid.
    :raises ValueError: If the configuration file is invalid.
    """
    # Ensure the correct number of script arguments were provided
    arguments.enforce_usage(sys.argv[1:])

    # Read the table configuration from the specified YAML file
    table_config = toolkit.read_config(sys.argv[1])

    # Extract sections from the table configuration
    sections = toolkit.get_sections(table_config)

    # Validate each section in the configuration
    for i, section in enumerate(sections, start=1):
        table_config_parser.parse_section(i, section)
    

def kg_config_main() -> None:
    """
    Main function to parse and validate knowledge graph configuration.

    This function enforces correct script usage, reads the knowledge graph
    configuration from a YAML file, and validates the configuration.

    :raises IndexError: If the number of arguments is invalid.
    :raises ValueError: If the configuration file is invalid.
    """
    # Ensure the correct number of script arguments were provided
    arguments.enforce_usage(sys.argv[1:])

    # Read the knowledge graph configuration from the specified YAML file
    kg_config = toolkit.read_config(sys.argv[1])

    # Validate the knowledge graph configuration
    kg_config_parser.parse_kg_config(kg_config)

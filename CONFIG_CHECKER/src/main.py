from src.utils import (
    toolkit, kg_config_parser,
    table_config_parser, arguments)


def table_config_main() -> None:
    arguments.enforce_usage(sys.argv[1:])
    table_config = toolkit.read_config(sys.argv[1])
    sections = toolkit.get_sections(table_config)
    for i, section in enumerate(sections, start=1):
        table_config_parser.parse_section(i, section)
    

def kg_config_main() -> None:
    arguments.enforce_usage(sys.argv[1:])
    kg_config = toolkit.read_config(sys.argv[1])
    kg_config_parser.parse_kg_config(kg_config)

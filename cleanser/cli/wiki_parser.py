import argparse


def add_wiki_parser(subparsers) -> argparse.ArgumentParser:
    """
    Add parser for Atlassian Confluence
    :param subparsers:
    :return: parser
    """
    print("Adding Atlassian Confluence parser")
    parser = subparsers.add_parser("wiki", help="Atlassian Confluence cleanup tool")
    parser.add_argument("-u", "--username", required=True, help="Username for Confluence")
    parser.add_argument("-p", "--password", required=True, help="Password for Confluence")
    parser.add_argument("-d", "--dry-run", action="store_true", help="Dry run mode")
    return parser

import argparse

from cleanser.cli.ado_parser import add_ado_parser
from cleanser.cli.jira_parser import add_jira_parser
from cleanser.cli.wiki_parser import add_wiki_parser


def get_parser():
    parser = argparse.ArgumentParser(description="Karol`s hefty tool to tidy up QA leftovers")
    subparsers = parser.add_subparsers(dest="tool")
    subparsers.required = True  # required subparser

    # parser registration
    add_ado_parser(subparsers)
    add_jira_parser(subparsers)
    add_wiki_parser(subparsers)

    return parser

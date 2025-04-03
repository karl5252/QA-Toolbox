import argparse


def add_jira_parser(subparsers) -> argparse.ArgumentParser:
    """
    Add parser for Atlassian Jira
    :param subparsers:
    :return: parser
    """
    print("Adding Atlassian Jira Cloud parser")
    parser = subparsers.add_parser("jira", help="Jira Cloud cleanup tool")
    parser.add_argument("-t", "--token", required=True, help="Personal access token")
    parser.add_argument("-d", "--dry-run", action="store_true", help="Dry run mode")
    return parser

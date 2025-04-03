import argparse


def add_ado_parser(subparsers) -> argparse.ArgumentParser:
    """
    Add parser for Azure DevOps
    :param subparsers:
    :return: parser
    """
    print("Adding Azure) DevOps parser")
    parser = subparsers.add_parser("ado", help="Azure DevOps cleanup tool")
    parser.add_argument("-t", "--token", required=True, help="Personal access token")
    parser.add_argument("-o", "--organization", help="Organization to clean up")
    parser.add_argument("-a", "--all", action="store_true", help="Run for all organizations")
    parser.add_argument("-d", "--dry-run", action="store_true", help="Dry run mode")
    return parser

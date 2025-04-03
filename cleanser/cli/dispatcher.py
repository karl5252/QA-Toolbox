from cleanser.cli.parser import get_parser
from cleanser.core.ado.run_ado_cleanup import run_cleanup
from cleanser.core.jira.run_jira_cleanup import run_jira_cleanup
from cleanser.core.wiki.run_wiki_cleanup import run_wiki_cleanup


def run_cli():
    parser = get_parser()
    args = parser.parse_args()
    print(args)  # debug

    if args.tool == "ado":
        run_cleanup(args.token, args.organization, args.dry_run)
    elif args.tool == "jira":
        run_jira_cleanup(args.token, args.dry_run)
    elif args.tool == "wiki":
        run_wiki_cleanup(args.username, args.password, args.dry_run)

import argparse


# noinspection PyProtectedMember
# pylint: disable=protected-access
def remove_help_tip(parser: argparse.ArgumentParser):
    for action in parser._actions:
        if action.dest == 'help':
            action.help = None
            break

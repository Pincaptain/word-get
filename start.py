import sys

from core.exect import exect


def run(argv):
    """
    Begins the execution of the program.
    Made into a separate file because of simplicity.

    :param argv:
    :return void:
    """

    exect.execute(argv)

if __name__ == '__main__':
    run(sys.argv)
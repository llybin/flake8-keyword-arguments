import ast

from flake8_keyword_arguments.utils import FlakeError

DEFAULT_MAX_POS_ARGS = 2


class KeywordArgumentsChecker:
    version = '1.0.0'
    name = 'flake8-keyword-arguments'

    max_pos_args = DEFAULT_MAX_POS_ARGS

    MESSAGE_TEMPLATE = "FKA01 {function_name}'s call uses {number_of_args} positional arguments, use keyword arguments."

    def __init__(self, tree, filename):
        self.filename = filename
        self.tree = tree

    @classmethod
    def add_options(cls, parser):
        parser.add_option(  # pragma: no cover
            '--max-pos-args',
            type='int',
            metavar='n',
            default=DEFAULT_MAX_POS_ARGS,
            parse_from_config=True,
            help='How many positional arguments are allowed (default: 2)',
        )

    @classmethod
    def parse_options(cls, options):
        cls.max_pos_args = int(options.max_pos_args)

    def run(self):
        errors = []

        for node in ast.walk(self.tree):
            if not isinstance(node, ast.Call):
                continue

            if len(node.args) > self.max_pos_args:
                function_name = self._get_name(node.func)
                message = self.MESSAGE_TEMPLATE.format(function_name=function_name, number_of_args=len(node.args))
                error = FlakeError(line=node.lineno, column=node.col_offset, message=message)
                errors.append(error)

        for error in errors:
            yield error.line, error.column, error.message, type(self)

    @staticmethod
    def _get_name(node):
        if hasattr(node, 'id'):
            return node.id

        if hasattr(node, 'attr'):
            return node.attr

        return 'unknown'

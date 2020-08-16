import re
from textwrap import dedent

from pytablewriter import TableWriterFactory
from pytablewriter.style import list_themes


regexp_ansi_escape = re.compile(
    r"(?:\x1B[@-Z\\-_]|[\x80-\x9A\x9C-\x9F]|(?:\x1B\[|\x9B)[0-?]*[ -/]*[@-~])"
)


class Test_loaded_as_plugin:
    def test_normal(self):
        assert "pytablewriter_altrow_theme" in list_themes()


class Test_set_theme:
    def test_normal(self):
        writer = TableWriterFactory.create_from_format_name("md")
        writer.headers = ["AAA", "BBB"]
        writer.value_matrix = [["aa", "bb"], ["cc", "dd"]]
        writer.margin = 1
        writer.set_theme("altrow", color="white")

        expected = dedent(
            """\
            | AAA | BBB |
            |-----|-----|
            | aa  | bb  |
            | cc  | dd  |
            """
        )

        lhs = writer.dumps()
        assert regexp_ansi_escape.search(lhs)
        assert regexp_ansi_escape.sub("", lhs) == expected

        writer.set_theme("altrow", color="yellow")
        rhs = writer.dumps()
        assert lhs != rhs

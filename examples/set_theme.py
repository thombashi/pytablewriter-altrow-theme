#!/usr/bin/env python3

from pytablewriter import TableWriterFactory


def main():
    writer = TableWriterFactory.create_from_format_name("md")
    writer.headers = ["INT", "STR"]
    writer.value_matrix = [[1, "hoge"], [2, "foo"], [3, "bar"]]
    writer.margin = 1
    writer.set_theme("altrow", color="yellow")

    writer.write_table()


if __name__ == "__main__":
    main()

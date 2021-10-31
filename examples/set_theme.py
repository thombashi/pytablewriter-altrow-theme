#!/usr/bin/env python3

import pytablewriter as ptw


def main() -> None:
    writer = ptw.TableWriterFactory.create_from_format_name(
        "markdown",
        table_name="altrow theme example",
        headers=["INT", "STR"],
        value_matrix=[
            [1, "hoge"],
            [2, "foo"],
            [3, "bar"],
        ],
        margin=1,
        theme="altrow",
    )
    writer.write_table()

    print()
    writer.set_theme("altrow", color="yellow")
    writer.write_table()


if __name__ == "__main__":
    main()

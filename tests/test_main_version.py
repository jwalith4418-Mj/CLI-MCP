"""Version reporting must exit before loading config or starting the server."""

from importlib.metadata import version
from unittest.mock import patch

import pytest

from cli_mcp.main import main


def test_version_uses_installed_distribution_and_does_not_start(capsys):
    with (
        patch("sys.argv", ["cli-mcp", "--version"]),
        patch("cli_mcp.main.load_config") as config,
        patch("cli_mcp.main.create_server") as server,
    ):
        with pytest.raises(SystemExit) as error:
            main()
    assert error.value.code == 0
    assert capsys.readouterr().out == f"cli-mcp {version('cli-mcp')}\n"
    config.assert_not_called()
    server.assert_not_called()

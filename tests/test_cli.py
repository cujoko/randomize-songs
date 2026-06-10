import pytest

from randomize_songs.cli import get_argparser


def test_version_argument(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as exc_info:
        get_argparser().parse_args(["--version"])

    assert exc_info.value.code == 0
    assert capsys.readouterr().out.startswith("randomize-songs ")

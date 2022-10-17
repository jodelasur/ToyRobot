import fileinput

from cli import main


def test_example_a(monkeypatch, capsys):
    monkeypatch.setattr(
        fileinput, "input", open("tests/example_inputs/a.txt").readlines
    )
    main()
    captured = capsys.readouterr()
    assert captured.out == "0,1,NORTH\n"


def test_example_b(monkeypatch, capsys):
    monkeypatch.setattr(
        fileinput, "input", open("tests/example_inputs/b.txt").readlines
    )
    main()
    captured = capsys.readouterr()
    assert captured.out == "0,0,WEST\n"


def test_example_c(monkeypatch, capsys):
    monkeypatch.setattr(
        fileinput, "input", open("tests/example_inputs/c.txt").readlines
    )
    main()
    captured = capsys.readouterr()
    assert captured.out == "3,3,NORTH\n"

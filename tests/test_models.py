from models.products import X, Source, Storage


def test_source_name(source: Source) -> None:
    assert source.name == "source1"


def test_source_plastic(source: Source) -> None:
    assert source.plastic == 100


def test_source_glass(source: Source) -> None:
    assert source.glass == 50


def test_source_biowaste(source: Source) -> None:
    assert source.biowaste == 70


def test_storage_name(storage: Storage) -> None:
    assert storage.name == "storage1"


def test_storage_plastic(storage: Storage) -> None:
    assert storage.plastic == 20


def test_storage_glass(storage: Storage) -> None:
    assert storage.glass == 10


def test_storage_biowaste(storage: Storage) -> None:
    assert storage.biowaste == 0


def test_x_key(x: X) -> None:
    assert x.key == "x"


def test_x_val(x: X) -> None:
    assert x.val == 1000

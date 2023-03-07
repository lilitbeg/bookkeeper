from bookkeeper.repository.sqlite_repository import SqliteRepository

import pytest


def test_cannot_create_sqlite_repository():
    with pytest.raises(TypeError):
        SqliteRepository()

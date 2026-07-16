from app.domain.entities.file_change import FileChange


def test_python_file():
    file = FileChange(
        filename="backend/app/main.py",
        status="modified",
        additions=10,
        deletions=2,
        changes=12,
        patch="@@ ...",
    )

    assert file.is_python


def test_deleted_file():
    file = FileChange(
        filename="README.md",
        status="removed",
        additions=0,
        deletions=15,
        changes=15,
        patch=None,
    )

    assert file.is_deleted


def test_added_file():
    file = FileChange(
        filename="new.py",
        status="added",
        additions=20,
        deletions=0,
        changes=20,
        patch="...",
    )

    assert file.is_added


def test_modified_file():
    file = FileChange(
        filename="service.py",
        status="modified",
        additions=4,
        deletions=2,
        changes=6,
        patch="...",
    )

    assert file.is_modified
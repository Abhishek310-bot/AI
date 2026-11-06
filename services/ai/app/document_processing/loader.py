from pathlib import Path


class DocumentLoader:

    def load(self, file_path: str) -> bytes:
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(
                f"File not found: {file_path}"
            )

        if not path.is_file():
            raise ValueError(
                f"Path is not a file: {file_path}"
            )

        return path.read_bytes()
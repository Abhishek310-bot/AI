from pathlib import Path

from pypdf import PdfReader


class DocumentExtractor:

    def extract(self, file_path: str) -> str:

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(
                f"File not found: {file_path}"
            )

        extension = path.suffix.lower()

        if extension == ".txt":
            return self._extract_text(path)

        if extension == ".pdf":
            return self._extract_pdf(path)

        raise ValueError(
            f"Unsupported file type: {extension}"
        )

    def _extract_text(self, path: Path) -> str:
        return path.read_text(
            encoding="utf-8"
        )

    def _extract_pdf(self, path: Path) -> str:

        reader = PdfReader(str(path))

        pages = []

        for page in reader.pages:
            text = page.extract_text()

            if text:
                pages.append(text)

        return "\n".join(pages)
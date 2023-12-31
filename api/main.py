from api.bootstrap import make_app  # noqa
from uvicorn import run


def main() -> None:
    run(app="api.main:make_app", host="0.0.0.0", port=8000, factory=True, workers=1, reload=True)

FROM python:3.11-slim

WORKDIR /app

# Install poetry
RUN pip install poetry

# Copy project files
COPY pyproject.toml poetry.lock* ./
COPY meditly ./meditly
COPY README.md ./

# Install dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

ENTRYPOINT ["poetry", "run", "meditly"]

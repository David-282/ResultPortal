# 1. Base image
FROM python:3.12-slim

# 2. Install uv (copies the uv binary from its official image)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# 3. Copy dependency files first (for build caching)
COPY pyproject.toml uv.lock ./

# 4. Install dependencies exactly as locked
RUN uv sync --frozen --no-install-project

# 5. Copy the rest of the project
COPY . .

RUN uv sync --frozen

# Expose Django's dev server port
EXPOSE 8000

# 6. Run the server
CMD ["uv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
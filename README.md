# Benchmark MarkItDown vs PyMuPDF

A simple benchmarking tool to compare performance between MarkItDown and PyMuPDF PDF processing libraries.

## Setup

### Install Hyperfine (Benchmarking Tool)

```bash
wget https://github.com/sharkdp/hyperfine/releases/download/v1.19.0/hyperfine_1.19.0_amd64.deb
sudo dpkg -i hyperfine_1.19.0_amd64.deb
```

### Install UV (Python Package Manager)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Running Benchmarks

First, sync dependencies:

```bash
uv sync
```

Run benchmarks:

```bash
# Normal mode benchmarks
hyperfine --warmup 3 --prepare true --runs 10 \
  'uv run src/serial/with_pdfminer.py' \
  'uv run src/serial/with_pymupdf.py' \
  'uv run src/serial/with_pymupdf4llm.py' \
  'uv run src/serial/with_markitdown.py'

# Parallel mode benchmarks
hyperfine --warmup 3 --prepare true --runs 10 \
  'uv run src/parallel/with_pymupdf.py' \
  'uv run src/parallel/with_pymupdf4llm.py' \
  'uv run src/parallel/with_pdfminer.py'
```

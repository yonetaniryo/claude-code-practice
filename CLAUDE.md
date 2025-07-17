# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Environment

This is a Python project that uses **uv** for dependency management and virtual environment handling.

- **Python Version**: Requires Python >=3.10
- **Package Manager**: uv (version 0.7.20)
- **Lock File**: uv.lock (tracks exact dependency versions)

### Installing uv

First, install uv via pip:
```bash
pip install uv
```

## Common Commands

### Running Code
```bash
# Run the main detection script
uv run detect.py

# Run a specific Python module
uv run -m module_name

# Run with additional dependencies
uv run --with package_name script.py
```

### Dependency Management
```bash
# Install dependencies from pyproject.toml
uv sync

# Add a new dependency
uv add package_name

# Remove a dependency
uv remove package_name

# Update dependencies
uv lock --upgrade
```

### Virtual Environment
```bash
# Activate virtual environment
uv shell

# Check environment status
uv info
```

## Project Structure

This is a simple object detection project with the following structure:

- `detect.py`: Main detection script using HuggingFace transformers
- `pyproject.toml`: Project configuration and dependencies
- `uv.lock`: Lock file for reproducible builds
- `README.md`: Japanese tutorial documentation

## Key Dependencies

- **torch**: PyTorch with CPU-only configuration
- **torchvision**: Computer vision library
- **transformers**: HuggingFace transformers library
- **timm**: PyTorch image models

Note: PyTorch is configured to use CPU-only wheels from the PyTorch index.

## Architecture Overview

The project consists of a single main script `detect.py` that:
1. Loads an image from "test.jpg"
2. Uses HuggingFace's DETR (Detection Transformer) model for object detection
3. Outputs detected objects with labels, confidence scores, and bounding boxes

The code uses the `facebook/detr-resnet-50` model through the HuggingFace transformers pipeline interface.

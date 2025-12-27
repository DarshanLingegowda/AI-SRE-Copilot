#!/usr/bin/env python3
"""Wrapper runner that sets warning filters before importing the application.

Run this instead of `python -m app.main` to ensure filters apply early.
"""
import warnings

# Suppress all UserWarning (broad)
warnings.filterwarnings("ignore", category=UserWarning)

# Suppress the specific Vertex AI deprecation message (regex)
warnings.filterwarnings("ignore", message=r".*deprecated as of June 24, 2025.*")

# Now run the app module as __main__ so imports happen after filters
import runpy
runpy.run_module("app.main", run_name="__main__")

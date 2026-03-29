# Web Application Security Research Case Study

## Overview
Technical analysis of security vulnerabilities and privacy implementations found in a production-grade social networking platform (referred to as "Target Platform").

## Key Findings
- **Broken Access Control (High):** Identified an unauthenticated POST endpoint allowing actions without session validation.
- **Image Metadata Sanitization (Success):** Verified that the backend correctly strips EXIF/GPS metadata, protecting user privacy.
- **Information Leakage (Low):** Analysis of JS bundles revealed excessive internal logic and comments.

## Tools
Python 3, Chrome DevTools, Regex.

# Web Application Security Research Case Study

A cybersecurity case study analyzing security and privacy behavior in a production-grade social networking platform. The platform is intentionally anonymized as **Target Platform** to keep the write-up responsible and focused on methodology rather than exposure.

This project demonstrates practical security analysis, ethical documentation, and the ability to reason about real-world web application risks.

## Project Focus

- Web application security analysis
- Access-control testing
- Privacy and metadata handling
- JavaScript bundle review
- Responsible reporting and anonymized documentation

## Key Findings

| Finding | Severity | Summary |
| --- | --- | --- |
| Broken access control | High | Identified an unauthenticated POST endpoint that appeared to allow sensitive actions without session validation. |
| Image metadata sanitization | Positive security control | Verified that uploaded images were stripped of EXIF/GPS metadata, reducing privacy risk. |
| Information leakage | Low | Reviewed client-side JavaScript bundles and found internal implementation details that could expose unnecessary context. |

## Methodology

1. Mapped visible application flows and network requests.
2. Used browser developer tools to inspect request structure and session behavior.
3. Tested whether sensitive actions required authenticated state.
4. Uploaded and inspected image metadata handling.
5. Reviewed JavaScript bundles for exposed comments, routes, and internal logic.
6. Documented findings with severity, risk, and suggested mitigation.

## Tools Used

- Chrome DevTools
- Python 3
- Regex-based static inspection
- HTTP request analysis
- Metadata inspection workflow

## Security Skills Demonstrated

- Understanding of OWASP-style access-control risks
- Ability to distinguish vulnerabilities from successful security controls
- Privacy-oriented thinking around image metadata and user uploads
- Clear technical documentation of risk, evidence, and impact
- Responsible anonymization of sensitive target details

## Responsible Use Note

This repository is written as an educational and portfolio case study. It avoids naming the target, exposing exploit details, or encouraging unauthorized testing. Security work should always be performed only in authorized environments or through responsible disclosure programs.

## What I Learned

This project strengthened my understanding of how real web applications can fail in small but important ways. I practiced looking beyond the UI, reading network behavior, thinking like an attacker, and documenting findings in a way that is useful for engineering teams.

I also learned that security analysis is not only about finding vulnerabilities. Verifying that a system correctly protects privacy, such as stripping image metadata, is also an important part of a complete assessment.

## Status

Portfolio case study in web security and privacy analysis.
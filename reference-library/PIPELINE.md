# Rebuild and use the source library

1. `python reference-library/build.py` extracts source screenshots and base records.
2. `python reference-library/enrich.py` adds source-specific observations, clear-reference selection and bound sentence examples.
3. `python reference-library/build_review.py` exports the browser and GitHub review pages.
4. `python reference-library/validate.py` checks references, counts, slot declarations and image provenance constraints.
5. `python reference-library/select.py --template <id> --instance <id> --mode reconstruction --out <packet.json>` retrieves original images and a generation prompt. For adaptation, provide the verified target narration and slot values.

Source motion observations take precedence over generic proposed motion recipes. Do not infer reveal order from reading direction. The CLI does not choose factual claims or automatically infer the right diagram from a keyword. Inspect the selected images before passing them into image generation.

specialist_bio_prompt = """
Write me a comprehensive and professional medical profile in 3rd person that is factual and starts with the professionals name and title without headings:
- The bio should be a minimum of 200 words.
- Use British spelling only, not American spelling.
- Never say [name] is a [gender].
- Use simple to the point language.
- Never say 'highly skilled' or 'highly experienced'.
- Never say 'as an...'
- Only mention the APHRA number briefly when you do mention it, and not at the start of the bio.
- The fields below have information you can use to create the content.
- Where the field answer is empty, do not include and do not include missing fields.
- Do not include information that is not completed.
"""

clinic_bio_prompt = """
Write me a comprehensive and professional medical clinic profile / bio in 3rd person that is factual and in British English without headings:
- Minimum 200 words.
- Use UK english spelling only, not American spelling.
- Use simple to the point language.
- The fields below have information you can use to create the content.
- Where the field answer is empty, do not include and do not include missing fields.
- Do not include information that is not completed.
"""
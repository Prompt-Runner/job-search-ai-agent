import json

from App.services.gemini_service import generate_response


def match_resume_with_job(resume_text: str, job_description: str):

    prompt = f"""
You are an expert ATS and job matching system.

Compare the candidate's resume with the provided job description.

====================
RESUME
====================
{resume_text}

====================
JOB DESCRIPTION
====================
{job_description}

====================

Analyze how well the resume matches the job.

Return ONLY valid JSON using exactly this structure:

{{
    "match_score": 0,

    "matching_skills": [],

    "missing_skills": [],

    "matching_keywords": [],

    "missing_keywords": [],

    "experience_alignment": "",

    "education_alignment": "",

    "strengths_for_this_job": [],

    "gaps_for_this_job": [],

    "recommendations": []
}}

IMPORTANT:
- match_score must be between 0 and 100.
- Use only information present in the resume and job description.
- Do not invent candidate experience or skills.
- "missing_skills" means the skill is required or mentioned in the job description
  but is NOT explicitly found in the resume.
- Do not assume the candidate does not know a missing skill.
- Keep recommendations specific to this job.
- Return JSON only.
- Do not use Markdown.
- Do not add explanations outside the JSON.
"""

    response = generate_response(prompt)

    cleaned_response = response.strip()

    if cleaned_response.startswith("```json"):
        cleaned_response = cleaned_response[7:]

    elif cleaned_response.startswith("```"):
        cleaned_response = cleaned_response[3:]

    if cleaned_response.endswith("```"):
        cleaned_response = cleaned_response[:-3]

    cleaned_response = cleaned_response.strip()

    try:
        return json.loads(cleaned_response)

    except json.JSONDecodeError:
        return {
            "success": False,
            "error": "Gemini returned an invalid JSON response.",
            "raw_response": response
        }
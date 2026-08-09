import json

from App.services.gemini_service import generate_response


def analyze_resume(resume_text: str):

    prompt = f"""
You are an expert ATS resume analyzer.

Analyze the resume below.

RESUME:
====================
{resume_text}
====================

Calculate an ATS score out of 100 using:

1. Contact & Basic Information: 10
2. Skills & Keywords: 20
3. Education: 10
4. Work Experience: 20
5. Projects: 15
6. Resume Structure & Formatting: 10
7. Achievements & Certifications: 5
8. Overall Job Readiness: 10

For each strength:
- point: identify the strength.
- explanation: explain why it is a strength based on the resume.
- impact: explain how it helps the candidate in recruitment.

For each weakness:
- point: identify the weakness.
- explanation: explain what is missing or weak.
- impact: explain how it may affect ATS screening or recruiter evaluation.

SKILLS GAP ANALYSIS:

Analyze the resume for skills and keywords that are NOT explicitly mentioned.

Separate the results into:

1. missing_technical_skills:
   Technical skills commonly relevant to the candidate's field that are not found in the resume.

2. missing_tools_frameworks:
   Tools, libraries, frameworks, platforms, or technologies relevant to the candidate's field that are not found in the resume.

3. recommended_skills:
   Skills that could strengthen the candidate's profile based on the technologies and experience already present in the resume.

IMPORTANT:
- "Missing" means NOT FOUND in the uploaded resume.
- Do NOT assume the candidate does not actually know a missing skill.
- Do not invent experience or qualifications.
- Recommendations should be relevant to the candidate's existing technical profile.

Return ONLY valid JSON using exactly this structure:

{{
    "ats_score": 0,

    "category_scores": {{
        "contact_information": 0,
        "skills_keywords": 0,
        "education": 0,
        "work_experience": 0,
        "projects": 0,
        "resume_structure": 0,
        "achievements_certifications": 0,
        "job_readiness": 0
    }},

    "skills": {{
        "technical": [],
        "soft": []
    }},

    "strengths": [
        {{
            "point": "",
            "explanation": "",
            "impact": ""
        }}
    ],

    "weaknesses": [
        {{
            "point": "",
            "explanation": "",
            "impact": ""
        }}
    ],

    "missing_keywords": [],

    "skills_gap": {{
        "missing_technical_skills": [],
        "missing_tools_frameworks": [],
        "recommended_skills": []
    }},

"improvement_suggestions": [
    {{
        "area": "",
        "issue": "",
        "suggestion": "",
        "priority": ""
    }}
]
}}

FINAL REQUIREMENTS:
- Return JSON only.
- Do not use Markdown.
- Do not use ```json.
- Do not add explanations before or after the JSON.
- Use only information supported by the resume.
- Do not invent skills, experience, education, certifications, or achievements.
- Each category score must stay within its maximum.
- Category scores must add up to the ATS score.
"""

    response = generate_response(prompt)

    cleaned_response = response.strip()

    # Remove Markdown code fences if Gemini still returns them
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
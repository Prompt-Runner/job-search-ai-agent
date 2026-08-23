from App.services.parser_service import extract_text

file_path = "Assets/resumes/Pranavi_Datta_Kasbe.pdf"

text = extract_text(file_path)

print("=" * 50)
print("Resume Text:")
print("=" * 50)
print(text)
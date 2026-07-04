from app.extraction.extractor import FieldExtractor

sample = """
Applications are invited for 25 vacancies.
Scale of pay of Rs.56,100 - 1,77,500.
Maximum age of 42 years.
"""

print(FieldExtractor.extract_vacancies(sample))
print(FieldExtractor.extract_salary(sample))
print(FieldExtractor.extract_age(sample))
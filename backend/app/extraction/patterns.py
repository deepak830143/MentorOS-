SALARY_PATTERNS = [

    r"scale of pay\s+of\s+Rs\.?\s*([\d,]+)\s*[–-]\s*([\d,]+)",

    r"pay scale\s*:\s*Rs\.?\s*([\d,]+)\s*[–-]\s*([\d,]+)",

    r"salary\s*:\s*Rs\.?\s*([\d,]+)\s*[–-]\s*([\d,]+)",

]

VACANCY_PATTERNS = [

    r"for\s+(\d+)\s+vacancies",

    r"(\d+)\s+vacancies",

    r"number of vacancies\s*[:\-]?\s*(\d+)",

]

AGE_PATTERNS = [

    r"maximum age of\s+(\d+)",

    r"upper age limit\s*[:\-]?\s*(\d+)",

    r"age limit\s*[:\-]?\s*(\d+)",

]
from app.extraction.cleaner import TextCleaner

sample = """



PAGE 1



Applications      are invited.



Scale    of pay Rs.56100 – 177500



2



"""

clean = TextCleaner.clean(sample)

print(clean)
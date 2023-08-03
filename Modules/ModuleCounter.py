from collections import Counter

cnt = Counter()

with open ("survey_results_public.csv") as data:
    for response in data:
        cnt.update(response.split(","))

print(cnt)



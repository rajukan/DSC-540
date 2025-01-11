from fuzzywuzzy import fuzz, process
import warnings
warnings.filterwarnings("ignore")

alias_name='gyan r kannur'
full_name='gyaneshwar raju kannur '

# print(
#
#     f'ratio {
#     fuzz.ratio(alias_name,full_name)
#     } , partial {fuzz.partial_ratio(alias_name,full_name)} , token {fuzz.token_sort_ratio(full_name,alias_name)}'
#
# )

grps = ["USA", 'usa','usaa', 'united states', 'united states of america','america']
print(process.extract("usa",grps,scorer=fuzz.ratio))
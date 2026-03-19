from typing import List

numbers = str(input())
prefix = input()


def join_prefix_to_numbers(list_of_numbers: List[str], prefix: str) -> List[str]:
    joined_numbers = []

    for number in list_of_numbers:
        joined_numbers.append(prefix + number)

    return joined_numbers


list_of_numbers = numbers.split()
result = join_prefix_to_numbers(list_of_numbers, prefix)
final_result = " ".join(result)
print(final_result)

"""
numbers = (input()) prefix = input() # Write your code below # Many thanks for the casting function advice: JaviLazaro1 def join_prefix_to_numbers(list_of_numbers:list, prefix: str): joined_numbers = [] for number in list_of_numbers: joined_numbers.append(prefix + number) return joined_numbers list_of_numbers = (numbers.split()) result = join_prefix_to_numbers(list_of_numbers, prefix) final_result = " ".join(result) print(final_result)

"""

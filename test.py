import random
import os

def prompt_explorer_tag(prompt, tag, fragments, num_select):
  if tag in prompt:
    if num_select == 0:
      return prompt.replace(tag, "")
    else:
      split_fragments = fragments.split(", ")
      select_fragments = random.sample(split_fragments, k=num_select)
      replace = ", ".join(select_fragments)
      return prompt.replace(tag, replace)

def prompt_explorer(prompt: str, fragments: list, num_select: list):
  for i in range(1, 8):
    prompt = prompt_explorer_tag(prompt, f"<PE{i}>", fragments[i], num_select[i])
  return prompt

prompt = "I like <PE1> and <PE2> and <PE3> and <PE4> and <PE5> and <PE6> and <PE7>."
pe1 = "apple, banana, orange"
pe2 = "cat, dog, bird"
pe3 = "red, blue, green"
pe4 = "car, bike, bus"
pe5 = "computer, phone, tablet"
pe6 = "book, magazine, newspaper"
pe7 = "coffee, tea, milk"
fragments = [None, pe1, pe2, pe3, pe4, pe5, pe6, pe7]
num_select = [None, 1, 1, 1, 1, 1, 1, 1]
prompt = prompt_explorer(prompt, fragments, num_select)
print(prompt)


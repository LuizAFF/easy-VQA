from shape import Shape
from color import Color
from location import Location
from random import randint

def create_questions(shape, color, location, image_id):
  shape_name = shape.name.lower()
  color_name = color.name.lower()
  location_name = location.name.lower()

  questions = [
    (f'what shape is in the image?', shape_name),
    (f'what shape is present?', shape_name),
    (f'what shape does the image contain?', shape_name),
    (f'what is the {color_name} shape?', shape_name),

    (f'what color is the {shape_name}?', color_name),
    (f'what is the color of the {shape_name}?', color_name),
    (f'what color is the shape?', color_name),
    (f'what is the color of the shape?', color_name),

    (f'what is the position of the shape?', location_name),
    (f'where is the shape?', location_name),
    (f'where is the {shape_name}?', location_name),
    (f'where is the {color_name} shape?', location_name),
  ]

  yes_no_questions = []

  for s in Shape:
    cur_shape_name = s.name.lower()
    pos_answer = 'yes' if s is shape else 'no'
    yes_no_questions.append((f'is there a {cur_shape_name}?', pos_answer))
    yes_no_questions.append((f'is there a {cur_shape_name} in the image?', pos_answer))
    yes_no_questions.append((f'does the image contain a {cur_shape_name}?', pos_answer))
    yes_no_questions.append((f'is a {cur_shape_name} present?', pos_answer))

    neg_answer = 'no' if s is shape else 'yes'
    yes_no_questions.append((f'is there not a {cur_shape_name}?', neg_answer))
    yes_no_questions.append((f'is there not a {cur_shape_name} in the image?', neg_answer))
    yes_no_questions.append((f'does the image not contain a {cur_shape_name}?', neg_answer))
    yes_no_questions.append((f'is no {cur_shape_name} present?', neg_answer))

  for c in Color:
    cur_color_name = c.name.lower()
    pos_answer = 'yes' if c is color else 'no'
    yes_no_questions.append((f'is there a {cur_color_name} shape?', pos_answer))
    yes_no_questions.append((f'is there a {cur_color_name} shape in the image?', pos_answer))
    yes_no_questions.append((f'does the image contain a {cur_color_name} shape?', pos_answer))
    yes_no_questions.append((f'is a {cur_color_name} shape present?', pos_answer))

    neg_answer = 'no' if c is color else 'yes'
    yes_no_questions.append((f'is there not a {cur_color_name} shape?', neg_answer))
    yes_no_questions.append((f'is there not a {cur_color_name} shape in the image?', neg_answer))
    yes_no_questions.append((f'does the image not contain a {cur_color_name} shape?', neg_answer))
    yes_no_questions.append((f'is no {cur_color_name} shape present?', neg_answer))


  for l in Location:
    cur_location_name = l.name.lower()
    pos_answer = 'yes' if l is location else 'no'
    yes_no_questions.append((f'is there a shape in the {cur_location_name}?', pos_answer))
    yes_no_questions.append((f'is there a shape in the {cur_location_name} in the image?', pos_answer))
    yes_no_questions.append((f'does the image contain a shape in the {cur_location_name}?', pos_answer))
    yes_no_questions.append((f'is a shape present in the {cur_location_name}?', pos_answer))

    neg_answer = 'no' if s is shape else 'yes'
    pos_answer = 'yes' if l is location else 'no'
    yes_no_questions.append((f'is there not a shape in the {cur_location_name}?', pos_answer))
    yes_no_questions.append((f'is there not a shape in the {cur_location_name} in the image?', pos_answer))
    yes_no_questions.append((f'does the image not contain a shape in the {cur_location_name}?', pos_answer))
    yes_no_questions.append((f'is a shape not present in the {cur_location_name}?', pos_answer))


  questions = list(filter(lambda _: randint(0, 99) < 48, questions))
  yes_no_questions = list(filter(lambda _: randint(0, 99) < 12, yes_no_questions))

  all_questions = questions + yes_no_questions
  return (list(map(lambda x: x + (image_id,), all_questions)), len(yes_no_questions))

class LoveCalculator:

  def __init__(self, name1, name2):
    self.name1 = name1
    self.name2 = name2
    self.combined_names = self.name1.lower() + self.name2.lower()

  def calculate_love_score(self):
    # Count occurrences of letters
    self.t_count = self.combined_names.count("t")
    self.r_count = self.combined_names.count("r")
    self.u_count = self.combined_names.count("u")
    self.e_count = self.combined_names.count("e")
    self.l_count = self.combined_names.count("l")
    self.o_count = self.combined_names.count("o")
    self.v_count = self.combined_names.count("v")

    # Calculate first and second digits
    self.first_digit = self.t_count + self.r_count + self.u_count + self.e_count
    self.second_digit = self.l_count + self.o_count + self.v_count + self.e_count

    # Combine digits into score
    self.score = int(str(self.first_digit) + str(self.second_digit))

    return self.score

  def get_compatibility_message(self):
    if self.score < 10 or self.score > 90:
      return f"Your score is {self.score}, you go together like coke and mentos!"
    elif 40 <= self.score <= 50:
      return f"Your score is {self.score}, you are alright together."
    else:
      return f"Your love score is {self.score}."

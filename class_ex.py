class Student:

    perc_rise = 1.05

    def __init__(self, first, last,  marks):

        self.first = first
        self.last = last
        self.marks = marks
        self.email = first + '.' + last + '@school.com'

    def full_name(self):

        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):

        self.marks = int(self.marks * 1.05)


class Dumb(Student):

    perc_rise = 1.10

    def __init__(self, first, last, marks, prog_lang):

        super().__init__(first, last, marks)
        self.prog_lang = prog_lang


std_1 = Dumb('Neel', 'Verma', 60, 'Python')

print(std_1.prog_lang)


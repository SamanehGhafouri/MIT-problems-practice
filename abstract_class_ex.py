from abc import ABC, abstractmethod


class Employee(ABC):

    @abstractmethod
    def calculate_salary(self, sal):

        pass


class Developer(Employee):

    def calculate_salary(self, sal):

        final_salary = sal * 1.10

        return final_salary

    def position_1(self, position):

        self.position = position
        return position


emp_1 = Developer()
print(emp_1.calculate_salary(10000))
print(emp_1.position_1('Web Developer'))

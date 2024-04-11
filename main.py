import os

from Perceptron import Perceptron

def get_file_data(file_name, data_list):
    file = open(file_name, 'r')
    for line in file:
        line = line.strip()
        line_data = line.split(",")
        for i in range(len(line_data)-1):
            line_data[i] = float(line_data[i])
        data_list.append(line_data)
    file.close()

def choose_option():
    option = -1
    while option not in range(1, 4):
        print("1. Zapewnij gatunek testowy")
        print("2. Przeczytaj gatunki testowe z zestawu szkoleniowego plików.csv")
        print("3. Wyjdź")
        try:
            option = input("Proszę wybrać opcję:")
            option = int(option)
            if option not in range(1, 4):
                print("Złe wejście. Proszę spróbować ponownie.")
        except ValueError as e:
            print("Złe wejście. Proszę spróbować ponownie.")
            option = -1
    return option


def provide_alpha():
    alpha = -1
    while  alpha > 1 or alpha <= 0:
        try:
            alpha = input("Zapewnij Alfa:")
            alpha = float(alpha)
            if 0 >= alpha or alpha > 1:

                print("Nieprawidłowa wartość dla Alfa. Proszę spróbować ponownie.")
        except ValueError:
            print("Nieprawidłowa wartość dla Alfa. Proszę spróbować ponownie.")
            alpha = -1
    return alpha
def provide_vector(length):
    vector = []
    for i in range(length):
        vector.append(float(input("")))
    return vector



training_species_list = []
get_file_data('data/training-set.csv', training_species_list)
is_end = False
alpha = provide_alpha()
while not is_end:
    option = choose_option()
    perceptron = Perceptron(len(training_species_list[0]) - 1, alpha)
    perceptron.train(training_species_list)
    match option:
        case 1:
            iris = provide_vector(len(perceptron.weights))
            perceptron.test_one(iris)
        case 2:
            testing_species_list = []
            get_file_data('data/testing-set.csv', testing_species_list)
            perceptron.test(testing_species_list)
        case 3:
            is_end = True

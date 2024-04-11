import random


class Perceptron:
    def __init__(self, num_of_weights, learning_rate):
        self.weights = []
        for i in range(num_of_weights):
            self.weights.append(random.uniform(-1, 1))
        self.threshold = random.uniform(-1, 1)
        self.learning_rate = learning_rate

    def train(self, training_data):
        dict_iris_count = {"Iris-setosa": 0, "Iris-virginica": 0}
        dict_iris_correct = {"Iris-setosa": 0, "Iris-virginica": 0}
        while True:
            for i in range(10):
                for data in training_data:
                    weighted_sum = 0
                    curr_result = 0
                    expected_result = 1 if data[-1] == "Iris-setosa" else 0
                    dict_iris_count[data[-1]] += 1
                    for i in range(len(self.weights)):
                        weighted_sum += data[i] * self.weights[i]
                    curr_result += weighted_sum >= self.threshold
                    if curr_result == expected_result:
                        dict_iris_correct[data[-1]] += 1
                    self.change_weights_and_threshold(data, expected_result, curr_result)
            if (dict_iris_correct["Iris-setosa"] / dict_iris_count["Iris-setosa"] > 0.95 and
                    dict_iris_correct["Iris-virginica"] / dict_iris_count["Iris-virginica"] > 0.95):
                break

    def test_one(self, testing_data):
        weighted_sum = 0
        curr_result = 0
        for i in range(len(self.weights)):
            weighted_sum += testing_data[i] * self.weights[i]
        curr_result += weighted_sum >= self.threshold
        calculated_class = "Iris-setosa" if curr_result == 1 else "Iris-virginica"
        print("calculated class: ", calculated_class, end="\n\n")

    def test(self, testing_data):
        dict_iris_count = {"Iris-setosa": 0, "Iris-virginica": 0}
        dict_iris_correct = {"Iris-setosa": 0, "Iris-virginica": 0}
        for data in testing_data:
            weighted_sum = 0
            curr_result = 0
            expected_result = 1 if data[-1] == "Iris-setosa" else 0
            dict_iris_count[data[-1]] += 1
            for i in range(len(self.weights)):
                weighted_sum += data[i] * self.weights[i]
            curr_result += weighted_sum >= self.threshold
            if curr_result == expected_result:
                dict_iris_correct[data[-1]] += 1
            real_class = data[-1]
            calculated_class = "Iris-setosa" if curr_result == 1 else "Iris-virginica"
            print("prawdziwa klasa: ", real_class, end="\n")
            print("obliczona klasa: ", calculated_class, end="\n\n")
        print("Iris-setosa dokładność:", dict_iris_correct["Iris-setosa"] / dict_iris_count["Iris-setosa"])
        print("Iris-virginica dokładność:", dict_iris_correct["Iris-virginica"] / dict_iris_count["Iris-virginica"])

    def change_weights_and_threshold(self, data, expected_result, current_result):
        data_copy = data[:]
        for i in range(len(data) - 1):
            data_copy[i] *= self.learning_rate * (expected_result - current_result)
            self.weights[i] += data_copy[i]
        self.threshold += (expected_result - current_result) * self.learning_rate * (-1)

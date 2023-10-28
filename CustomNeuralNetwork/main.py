import json
from math import exp, log
from typing import Literal
from enum import Enum, auto
import pprint
from cryptography.fernet import Fernet


class LayerTypes(Enum):
    INPUT = auto()
    OUTPUT = auto()
    HIDDEN = auto()


class ActivationFunctions(Enum):
    STEP_UNIPOLAR = auto()
    STEP_BIPOLAR = auto()
    SIGMOID_UNIPOLAR = auto()
    SIGMOID_BIPOLAR = auto()
    IDENTITY = auto()
    RELU = auto()
    RELU_LEAKY = auto()
    RELU_PARAMETRIC = auto()
    SOFTPLUS = auto()


class Layer:
    def __init__(self,
                 layer_type: LayerTypes,
                 left_layer: 'Layer' = None,
                 right_layer: 'Layer' = None) -> None:
        self.id = 'L/?/?/'
        self.children: list = []
        self.layer_type: LayerTypes = layer_type
        self.right_layer: Layer = right_layer
        self.left_layer: Layer = left_layer
        self.__children_functions: list[ActivationFunctions] = []
        self.__layer_num: int = None

    def get_child_count(self) -> int:
        return len(self.children)

    def get_children(self) -> list:
        return self.children

    def add_child(self, child) -> None:
        if self.layer_type == LayerTypes.INPUT and not isinstance(child, NetworkInput):
            raise ValueError(
                f"Incorrect child argument. Got {type(child)}. Expected: {NetworkInput}")
        elif self.layer_type == LayerTypes.OUTPUT and not isinstance(child, NetworkOutput):
            raise ValueError(
                f"Incorrect child argument. Got {type(child)}. Expected: {NetworkOutput}")
        elif self.layer_type == LayerTypes.HIDDEN and not isinstance(child, Perceptron):
            raise ValueError(
                f"Incorrect child argument. Got {type(child)}. Expected: {Perceptron}")
        self.children.append(child)
        if isinstance(child, Perceptron):
            self.__children_functions.append(child.activation_function)
        child.set_id(self.__layer_num, len(self.children))
        self.__update_id()

    def set_id(self, layer: int) -> None:
        self.__layer_num = layer
        l_type = 'I' if self.layer_type == LayerTypes.INPUT\
            else 'H' if self.layer_type == LayerTypes.HIDDEN else 'O'
        self.id: str = f'L/{l_type}/{layer}/{len(self.children)}'

    def __update_id(self):
        if self.__layer_num is None:
            return
        l_type: Literal['I', 'H', 'O'] = 'I' if self.layer_type == LayerTypes.INPUT\
            else 'H' if self.layer_type == LayerTypes.HIDDEN else 'O'
        self.id: str = f'L/{l_type}/{self.__layer_num}/{len(self.children)}'

    def set_children_ids(self) -> None:
        for i, child in enumerate(self.children):
            child.set_id(self.__layer_num, i + 1)

    def get_sums(self) -> list[float]:
        return [item.calc_sum() for item in self.children]

    def set_children_functions(self, activation_function: ActivationFunctions) -> None:
        self.__children_functions = [
            activation_function for _ in range(len(self.children))]
        for child in self.children:
            child.activation_function = activation_function

    def set_child_weights(self, index: int, weights: list[float]) -> None:
        if index >= len(self.children) or index < 0:
            raise ValueError(
                f"Index out of range. Got {index} | Expected 0 - {len(self.children) - 1}")
        if len(weights) != len(self.left_layer.children) + 1:
            raise ValueError(
                f"Weights count mismatch. Got {len(weights)} | Expected {len(self.left_layer.children)} + 1 (own weight)")
        self.children[index].weights = weights

    def set_children_weights(self, weights: list[list[float]]) -> None:
        if len(weights) != len(self.children):
            raise ValueError(
                f"Weights count mismatch. Got {len(weights)} | Expected {len(self.children)}")
        for i, weight in enumerate(weights):
            self.set_child_weights(i, weight)

    def set_children_functions_by_list(self, activation_functions: list[ActivationFunctions]) -> None:
        if len(activation_functions) != len(self.children):
            raise ValueError(
                f"Activation functions count mismatch. Got {len(activation_functions)} | Expected {len(self.children)}")
        self.__children_functions = [
            ActivationFunctions(i) for i in activation_functions]
        for child, activation_function in zip(self.children, activation_functions):
            child.activation_function = ActivationFunctions(
                activation_function)

    def set_child_function(self, index: int, activation_function: ActivationFunctions) -> None:
        if index >= len(self.children) or index < 0:
            raise ValueError(
                f"Index out of range. Got {index} | Expected 0 - {len(self.children) - 1}")
        self.__children_functions[index] = activation_function
        self.children[index].activation_function = activation_function

    def get_children_functions(self) -> list[ActivationFunctions]:
        return self.__children_functions

    def debug_indepth(self) -> None:
        print(f"Layer {self.id}")
        print(f"Layer type: {self.layer_type}")
        print(f"Left layer: {self.left_layer}")
        print(f"Right layer: {self.right_layer}")
        print(f"Children count: {len(self.children)}")
        print(f"Children: {self.children}")
        print(f"Children functions: {self.__children_functions}")
        print("Children analysis:")
        for child in self.children:
            print('=' * 20)
            print(f"Child {child.id}")
            print(child.activation_function)
            print("Weights: ", child.weights)
            print("Output with activation function: ", child.get_output())
            print("On left side: ", child.left_neightbours)
            print(
                "Note to self: first item on left side is inner value to get inner weight * inner value (Bias)")

    def validate(self) -> None:
        if not isinstance(self.layer_type, LayerTypes):
            raise ValueError(
                f"Incorrect layer_type. Expected {LayerTypes}. Got {type(self.layer_type)}")

        if self.layer_type == LayerTypes.INPUT:
            if self.left_layer is not None:
                raise ValueError(
                    f"Input layer doesn't have left side layer. Got {self.left_layer}")
            if self.right_layer is None:
                raise ValueError(
                    "Input layer can't have empty right side layer")
        elif self.layer_type == LayerTypes.OUTPUT:
            if self.left_layer is None:
                raise ValueError("Output layer needs left side layer.")
            if self.right_layer is not None:
                raise ValueError(
                    f"Output layer doesn't have right side layer. Got {self.right_layer}")
        elif self.layer_type == LayerTypes.HIDDEN:
            if self.left_layer is None:
                raise ValueError("Hidden layer needs left side layer.")
            if self.right_layer is None:
                raise ValueError("Hidden layer needs right side layer.")

        if not isinstance(self.left_layer, Layer) and self.left_layer is not None:
            raise ValueError(
                f"Incorrect left layer. Expected {Layer}. Got {type(self.left_layer)}")
        elif not isinstance(self.right_layer, Layer) and self.right_layer is not None:
            raise ValueError(
                f"Incorrect right layer. Expected {Layer}. Got {type(self.right_layer)}")

    def get_dict(self) -> dict:
        obj_dict = {}
        obj_dict['id'] = self.id
        obj_dict['layer-type'] = self.layer_type
        obj_dict['left-layer'] = self.left_layer
        obj_dict['right_layer'] = self.right_layer
        obj_dict['children'] = self.children
        return obj_dict

    def __repr__(self) -> str:
        return self.id


class NetworkOutput:
    def __init__(self, res: float = 0) -> None:
        self.id = 'O/?/?'
        self.previous_outputs: 'list[float]' = []
        self.output: float = res

    def set_id(self, layer: int, position: int) -> None:
        self.id: str = f'O/{layer}/{position}'

    @property
    def output(self) -> float:
        return self.__output

    @output.setter
    def output(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise ValueError(f"Incorrect data detected {self.id} | {value}")
        self.__output = value
        self.previous_outputs.append(self.__output)
        if len(self.previous_outputs) > 50:
            self.previous_outputs.pop(0)

    def __repr__(self) -> str:
        return self.id


class NetworkInput:
    def __init__(self, res: float = 0) -> None:
        self.id = 'I/?/?'
        self.previous_outputs: 'list[float]' = []
        self.output: float = res

    def set_id(self, layer: int, position: int) -> None:
        self.id: str = f'I/{layer}/{position}'

    @property
    def output(self) -> float:
        return self.__output

    @output.setter
    def output(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise ValueError(f"Incorrect data detected {self.id} | {value}")
        self.__output = value
        self.previous_outputs.append(self.__output)
        if len(self.previous_outputs) > 50:
            self.previous_outputs.pop(0)

    def __repr__(self) -> str:
        return self.id


class Perceptron:
    def __init__(self,
                 activation_function: int,
                 inner_weight=0,
                 step_bipolar_threshold=0,
                 identity_a=1,
                 parametric_a=0.1) -> None:
        self.id = 'P/?/?'
        self.activation_function = activation_function
        self.__inner_weight = inner_weight
        self.__weights: list = [self.__inner_weight]
        self.previous_weights: list[list[float]] = []
        self.__output: float = 0
        self.previous_outputs: list[float] = []
        self.inner_neighbour = NetworkInput(1)
        self.__step_bipolar_threshold = step_bipolar_threshold
        self.__identity_a = identity_a
        self.__parametric_a = parametric_a
        self.left_neightbours: 'list[Perceptron]' = [self.inner_neighbour]
        self.validate()

    @property
    def output(self):
        return self.__output

    @output.setter
    def output(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError(f"Incorrect output. {self.id} | {value}")
        self.__output = value
        self.previous_outputs.append(value)
        if len(self.previous_outputs) > 50:
            self.previous_outputs.pop(0)

    @property
    def weights(self):
        return self.__weights

    @weights.setter
    def weights(self, value):
        if not isinstance(value, (list)):
            raise ValueError(f"Incorrect weights. {self.id} | {value}")
        if len(value) != len(self.__weights):
            raise ValueError("Mismatch between size of weights."
                             f"Prev: {len(self.__weights)} | New: {len(value)}")
        self.__weights = value
        self.__inner_weight = value[0]
        self.previous_weights.append(value)
        if len(self.previous_weights) > 50:
            self.previous_weights.pop(0)

    def __add_weight(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError(f"Incorrect weight. {self.id} | {value}")
        self.__weights.append(value)
        self.previous_weights = [self.weights]

    def validate(self, explicit=False):
        if len(self.weights) != len(self.left_neightbours):
            raise Exception(f'Perceptron id: {self.id}')
        if explicit:
            print(
                f"Weight count and Neigbour count match {len(self.left_neightbours)} | {len(self.weights) - 1}")

    def add_neightbour(self, neightbour, weight: float = 0):
        if not isinstance(neightbour, (Perceptron, NetworkInput)):
            raise ValueError("Neighbour is not instance "
                             "of Perceptron or Network Input. "
                             f"Instead {type(neightbour)}")
        self.left_neightbours.append(neightbour)
        self.__add_weight(weight)

    def set_neighbours(self, neighbours):
        self.left_neightbours = [self.inner_neighbour]
        self.weights = [self.__inner_weight]
        self.previous_weights = []
        for neighbour in neighbours:
            self.add_neightbour(neighbour)

    def calc_sum(self) -> float:
        sum = 0
        for perc, weight in zip(self.left_neightbours, self.weights):
            sum += perc.output * weight
        return sum

    def set_id(self, layer: int, position: int) -> None:
        self.id: str = f'P/{layer}/{position}'
        self.inner_neighbour.set_id(layer, position)

    def calc_step_unipolar(self) -> Literal[1, 0]:
        if self.calc_sum() > 0:
            return 1
        return 0

    def calc_step_bipolar(self, threshold: float) -> Literal[1, -1]:
        if self.calc_sum() >= threshold:
            return 1
        return -1

    def calc_identity(self, a) -> float:
        return a * self.calc_sum()

    def calc_sigmoid_unipolar(self) -> float:
        return 1 / (1 + exp(-self.calc_sum()))

    def calc_sigmoid_bipolar(self) -> float:
        return -1 + 2 / (1 + exp(self.calc_sum()))

    def calc_relu(self) -> float:
        return max(0, self.calc_sum())

    def calc_relu_leaky(self) -> float:
        sum_ = self.calc_sum()
        return max(0.1 * sum_, sum_)

    def calc_relu_parametric(self) -> float:
        sum_ = self.calc_sum()
        if sum_ > 0:
            return sum_
        return self.__parametric_a * sum_

    def calc_softplus(self) -> float:
        return log(1 + exp(self.calc_sum()))

    def get_output(self) -> float | Literal[1, -1, 0]:
        if self.activation_function == ActivationFunctions.IDENTITY:
            return self.calc_identity(self.__identity_a)
        elif self.activation_function == ActivationFunctions.RELU:
            return self.calc_relu()
        elif self.activation_function == ActivationFunctions.SIGMOID_BIPOLAR:
            return self.calc_sigmoid_bipolar()
        elif self.activation_function == ActivationFunctions.SIGMOID_UNIPOLAR:
            return self.calc_sigmoid_unipolar()
        elif self.activation_function == ActivationFunctions.SOFTPLUS:
            return self.calc_softplus()
        elif self.activation_function == ActivationFunctions.STEP_BIPOLAR:
            return self.calc_step_bipolar(self.__step_bipolar_threshold)
        elif self.activation_function == ActivationFunctions.STEP_UNIPOLAR:
            return self.calc_step_unipolar()
        else:
            raise ValueError("Could not match activation function")

    def set_output(self, value):
        self.output = value

    def get_dict(self) -> dict:
        obj_dict = {}
        obj_dict['id'] = self.id
        obj_dict['output'] = self.output
        obj_dict['activation-function'] = self.activation_function
        obj_dict['weights'] = self.__weights
        obj_dict['inner-weight'] = self.__inner_weight
        obj_dict['left-side-U'] = len(self.left_neightbours) - 1
        obj_dict['inner-U'] = self.inner_neighbour.output
        obj_dict['U-id'] = [item.id for item in self.left_neightbours]
        return obj_dict

    def __repr__(self) -> str:
        return self.id


class NeuralNetwork:
    def __init__(self) -> None:
        self.id = 'N/I/?/H/?/P/?/O/?'
        self.layer_count: int = 0
        self.layers: list[Layer] = []
        self.__hidden_layers: list[Layer] = []
        self.__input_layer: Layer = None
        self.__output_layer: Layer = None
        self.perceptrons_per_layer: list[int] = []
        self.input_count: int = 0
        self.output_count: int = 0
        self.__mov_layer_i: int = 1

    def __update_id(self):
        self.id = f'N/I/{self.__input_layer.get_child_count()}/H/{len(self.__hidden_layers)}/P/{self.get_perceptron_count()}/O/{self.__output_layer.get_child_count()}'

    def get_perceptron_count(self) -> int:
        return sum(self.perceptrons_per_layer)

    def get_input_values(self) -> list[float]:
        return [item.output for item in self.__input_layer.get_children()]

    def set_input_values(self, values: list[float]) -> None:
        if len(values) != self.__input_layer.get_child_count():
            raise ValueError(
                f"Input values mismatch. Got {len(values)} | Expected {self.__input_layer.get_child_count()}")
        for value, input in zip(values, self.__input_layer.get_children()):
            input.output = value

    def get_output_values(self) -> list[float]:
        return [item.output for item in self.__output_layer.get_children()]

    def validate_network(self) -> None:
        for layer in self.layers:
            layer.validate()

    def calc_softmax(self) -> list[float]:
        self.__output_layer.get_sums()
        # implement softmax, linear and sigmoid as output functions

    def setup(self, inputs: int = 1, outputs: int = 1, hidden_layers: int = 1):
        layer = Layer(LayerTypes.INPUT)
        layer.set_id(self.__mov_layer_i)
        self.__mov_layer_i += 1
        self.layers.append(layer)
        for i in range(hidden_layers):
            layer = Layer(LayerTypes.HIDDEN)
            layer.set_id(self.__mov_layer_i)
            self.__mov_layer_i += 1
            self.layers.append(layer)
            self.__hidden_layers.append(layer)
        layer = Layer(LayerTypes.OUTPUT)
        layer.set_id(self.__mov_layer_i)
        self.__mov_layer_i += 1
        self.layers.append(layer)
        self.__input_layer = self.layers[0]
        self.__output_layer = self.layers[len(self.layers) - 1]
        for i in range(inputs):
            self.layers[0].add_child(NetworkInput())
        for i in range(outputs):
            self.layers[len(self.layers) - 1].add_child(NetworkOutput())
        for index in range(len(self.layers)):
            if index == 0:
                self.layers[index].right_layer = self.layers[index + 1]
            elif index == len(self.layers) - 1:
                self.layers[index].left_layer = self.layers[index - 1]
            else:
                self.layers[index].left_layer = self.layers[index - 1]
                self.layers[index].right_layer = self.layers[index + 1]
        self.validate_network()
        self.__update_id()

    def set_perceptrons_per_layer(self, perceptrons_per_layer: list[int]) -> None:
        if len(perceptrons_per_layer) != len(self.__hidden_layers):
            raise ValueError(
                f"Got perceptrons for incorrect number of layers. Got {len(perceptrons_per_layer)} | Expected {len(self.__hidden_layers)}")
        self.perceptrons_per_layer = perceptrons_per_layer
        for layer, perceptron_count in zip(self.__hidden_layers, perceptrons_per_layer):
            for i in range(perceptron_count):
                layer.add_child(Perceptron(ActivationFunctions.STEP_UNIPOLAR))
            layer.set_children_ids()

        for layer in self.layers:
            for child in layer.get_children():
                if isinstance(child, Perceptron):
                    child.set_neighbours(layer.left_layer.get_children())
        self.__update_id()

    def set_layer_activation_function(self, id, activation_function: ActivationFunctions) -> None:
        layer = self.get_layer_by_index(id)
        layer.set_children_functions(activation_function)

    def get_layer_by_index(self, index: int) -> Layer:
        # check if index is in range
        if index >= 1 and index < len(self.layers) - 1:
            return self.layers[index]
        raise ValueError(
            f"Index out of range. Got {index} | Expected 1 - {len(self.layers) - 1}")

    def get_dict(self) -> dict:
        obj_dict = {}
        obj_dict['id'] = self.id
        obj_dict['input-layer'] = self.__input_layer
        obj_dict['input-count'] = self.__input_layer.get_child_count()
        obj_dict['input_values'] = self.get_input_values()
        obj_dict['hidden-layers'] = self.__hidden_layers
        obj_dict['perceptrons-per-layer'] = self.perceptrons_per_layer
        obj_dict['output-layer'] = self.__output_layer
        obj_dict['output-count'] = self.__output_layer.get_child_count()
        obj_dict['output-values'] = self.get_output_values()
        return obj_dict

    def save_network(self, path):
        perc_dict = {}
        for i, layer in enumerate(self.__hidden_layers):
            perc_dict[f'{i + 1}'] = {
                'perceptons_activation_functions': [item.value for item in layer.get_children_functions()],
                'perceptons_weights': [item.weights for item in layer.get_children()]}

        save_dict = {
            'network': {
                'id': self.id,
                'input-count': self.__input_layer.get_child_count(),
                'hidden-layer_count': len(self.__hidden_layers),
                'perceptrons-per-layer': self.perceptrons_per_layer,
                'output-count': self.__output_layer.get_child_count(),
                'input-values': self.get_input_values(),
                'output-values': self.get_output_values(),
                'perceptrons_data': perc_dict
            }
        }
        json_string = json.dumps(save_dict)

        cipher_suite = Fernet('iy2hgPRYISdrCh11bmHUPa5yQKCHy7EmR4dgzhh1unE=')
        json_string = cipher_suite.encrypt(json_string.encode('utf-8'))
        with open(path, 'wb') as file:
            file.write(json_string)

    def load_network(self, path):
        with open(path, 'rb') as file:
            data_bytes = file.read()

        cipher_suite = Fernet('iy2hgPRYISdrCh11bmHUPa5yQKCHy7EmR4dgzhh1unE=')
        data_bytes = cipher_suite.decrypt(data_bytes)

        self.__init__()
        json_string = data_bytes.decode('utf-8')
        data = json.loads(json_string)
        network_data = data.get('network', {})
        self.id = network_data.get('id', self.id)
        self.setup(network_data.get('input-count', 1),
                   network_data.get('output-count', 1),
                   network_data.get('hidden-layer_count', 1))
        self.set_input_values(network_data.get('input-values', [0]))
        self.set_perceptrons_per_layer(
            network_data.get('perceptrons-per-layer', [1]))
        for line in network_data.get('perceptrons_by_hidden_layer', []):
            func_in_line = network_data['perceptrons_data'][line]['perceptons_activation_functions']
            weights_in_line = network_data['perceptrons_data'][line]['perceptons_weights']
            layer = self.get_layer_by_index(int(line))
            layer.set_children_functions_by_list(func_in_line)
            layer.set_children_weights(weights_in_line)

    def __repr__(self) -> str:
        return self.id


network = NeuralNetwork()
# network.setup(2, 1, 2)
# network.set_input_values([0.7, 1.3])
# network.set_perceptrons_per_layer([2,1])
# network.get_layer_by_index(1).set_child_function(
#     1, ActivationFunctions.SIGMOID_BIPOLAR)
# # print(network.get_layer_by_index(3).get_children_functions())
# network.get_layer_by_index(1).set_children_weights([[1, 0.5, 0.5], [-0.5, 0.3, 0.2]])
# # network.get_layer_by_index(1).set_child_weights(0, [1, 0.5, 0.5])
# # network.get_layer_by_index(1).set_child_weights(1, [-0.5, 0.3, 0.2])
# network.get_layer_by_index(1).debug_indepth()
# network.get_layer_by_index(2).debug_indepth()
# # pprint.pprint(network.get_dict())
# # network.save_network('CustomNeuralNetwork/network.nn')

# network.get_layer_by_index(1).set_children_weights([[0, 0, 0], [0, 0, 0]])
# network.get_layer_by_index(1).debug_indepth()
# network.set_layer_activation_function(1, ActivationFunctions.RELU)
# print(network.get_layer_by_index(1).get_children_functions())
# pprint.pprint(network.get_dict())
network.load_network('CustomNeuralNetwork/network.nn')
network.get_layer_by_index(1).debug_indepth()
pprint.pprint(network.get_dict())
# print(network.get_layer_by_index(1).get_children_functions())
# pprint.pprint(network.get_dict())
# pprint.pprint(network.get_dict())


# TODO: Implement backpropagation
# TODO: Implement softmax
# TODO: Implement linear
# TODO: Implement sigmoid

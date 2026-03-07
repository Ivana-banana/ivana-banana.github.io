import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def create_vector() -> np.ndarray:
    """
    Создает одномерный массив из 10 элементов

    Returns:
        np.ndarray: Массив чисел от 0 до 9
    """
    return np.arange(10)


def create_matrix() -> np.ndarray:
    """
    Создает матрицу 5x5 со случайными значениями от 0 до 1

    Returns:
        np.ndarray: Матрица размером 5x5
    """
    return np.random.rand(5, 5)


def reshape_vector(vec: np.ndarray) -> np.ndarray:
    """
    Изменяет форму вектора на матрицу 2x5

    Args:
        vec (np.ndarray): Исходный одномерный массив

    Returns:
        np.ndarray: Массив формой 2x5
    """
    return vec.reshape(2, 5)


def transpose_matrix(mat: np.ndarray) -> np.ndarray:
    """
    Транспонирует матрицу

    Args:
        mat (np.ndarray): Исходная матрица

    Returns:
        np.ndarray: Транспонированная матрица
    """
    return np.transpose(mat)


def vector_add(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Выполняет поэлементное сложение двух векторов

    Args:
        a (np.ndarray): Первый вектор
        b (np.ndarray): Второй вектор

    Returns:
        np.ndarray: Результат сложения
    """
    return a + b


def scalar_multiply(vec: np.ndarray, scalar: float) -> np.ndarray:
    """
    Умножает вектор на скаляр

    Args:
        vec (np.ndarray): Исходный вектор
        scalar (float): Скалярное значение

    Returns:
        np.ndarray: Результат умножения
    """
    return vec * scalar


def elementwise_multiply(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Выполняет поэлементное умножение двух массивов

    Args:
        a (np.ndarray): Первый массив
        b (np.ndarray): Второй массив

    Returns:
        np.ndarray: Результат поэлементного умножения
    """
    return a * b


def dot_product(a: np.ndarray, b: np.ndarray) -> float:
    """
    Вычисляет скалярное произведение двух векторов

    Args:
        a (np.ndarray): Первый вектор
        b (np.ndarray): Второй вектор

    Returns:
        float: Скалярное произведение
    """
    return np.dot(a, b)


def matrix_multiply(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Выполняет матричное умножение

    Args:
        a (np.ndarray): Первая матрица
        b (np.ndarray): Вторая матрица

    Returns:
        np.ndarray: Результат матричного умножения
    """
    return np.matmul(a, b)


def matrix_determinant(a: np.ndarray) -> float:
    """
    Вычисляет определитель матрицы

    Args:
        a (np.ndarray): Квадратная матрица

    Returns:
        float: Определитель матрицы
    """
    return np.linalg.det(a)


def matrix_inverse(a: np.ndarray) -> np.ndarray:
    """
    Вычисляет обратную матрицу

    Args:
        a (np.ndarray): Квадратная матрица

    Returns:
        np.ndarray: Обратная матрица
    """
    return np.linalg.inv(a)


def solve_linear_system(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Решает систему линейных уравнений Ax = B

    Args:
        a (np.ndarray): Матрица коэффициентов
        b (np.ndarray): Вектор правых частей

    Returns:
        np.ndarray: Вектор решения
    """
    return np.linalg.solve(a, b)


def load_dataset(path: str = "data/students_scores.csv") -> np.ndarray:
    """
    Загружает датасет из CSV-файла и преобразует в NumPy-массив

    Args:
        path (str): Путь к CSV-файлу

    Returns:
        np.ndarray: Массив данных
    """
    return pd.read_csv(path).to_numpy()


def statistical_analysis(data: np.ndarray) -> dict[str, float]:
    """
    Выполняет статистический анализ данных

    Args:
        data (np.ndarray): Массив данных для анализа

    Returns:
        dict[str, float]: Словарь со статистическими метриками
    """
    return {
        "mean": float(np.mean(data)),
        "median": float(np.median(data)),
        "std": float(np.std(data)),
        "min": float(np.min(data)),
        "max": float(np.max(data)),
        "percentile25": float(np.percentile(data, 25)),
        "percentile75": float(np.percentile(data, 75)),
    }


def normalize_data(data: np.ndarray) -> np.ndarray:
    """
    Нормализует данные к диапазону [0, 1]

    Args:
        data (np.ndarray): Исходный массив данных

    Returns:
        np.ndarray: Нормализованный массив
    """
    a = float(np.max(data))
    b = float(np.min(data))
    return np.array([(float(elem) - b) / (a - b) for elem in data])


def plot_histogram(data: np.ndarray) -> None:
    """
    Строит и сохраняет гистограмму распределения данных

    Args:
        data (np.ndarray): Массив данных для визуализации
    """
    plt.hist(data)
    plt.xlabel("Значения") # Подпись горизонтальной оси
    plt.ylabel("Частота") # Подпись вертикальной оси
    plt.title("Распределение данных") # Установка заголовка
    plt.savefig("plots/histogram.png") # Сохранение картинки


def plot_heatmap(matrix: np.ndarray) -> None:
    """
    Строит и сохраняет тепловую карту матрицы

    Args:
        matrix (np.ndarray): Матрица для визуализации
    """
    sns.heatmap(matrix)
    plt.title("Тепловая карта данных")
    plt.savefig("plots/heatmap.png")


def plot_line(x: np.ndarray, y: np.ndarray) -> None:
    """
    Строит и сохраняет линейный график

    Args:
        x (np.ndarray): Значения по оси X
        y (np.ndarray): Значения по оси Y
    """
    plt.plot(x, y)
    plt.xlabel("Номер студента")
    plt.ylabel("Оценки")
    plt.title("Распределение оценок")
    plt.savefig("plots/line.png")
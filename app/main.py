import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import time


def test():
  # Número de repetições para a medição de tempo
  num_repeats = 1000

  # Crie duas matrizes para multiplicação
  matrix_size = 1000
  matrix_a = tf.random.normal((matrix_size, matrix_size))
  matrix_b = tf.random.normal((matrix_size, matrix_size))

  # Use 'with' para definir o dispositivo (CPU ou GPU)
  start_time = time.time()
  for _ in range(num_repeats):
    result = tf.matmul(matrix_a, matrix_b)
  end_time = time.time()

  # Calcule o tempo médio por repetição
  average_time = (end_time - start_time) / num_repeats

  print(f'Tempo médio para multiplicação de matrizes ({matrix_size}x{matrix_size}) no dispositivo: {average_time} segundos')

import tensorflow as tf

print(tf.config.list_physical_devices('GPU'))

with tf.device('/cpu:0'):
  print('cpu')
  test()

with tf.device('/gpu:0'):
  print('gpu')
  test()
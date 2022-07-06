from __future__ import unicode_literals
import math
import wave
import numpy as np

DATA_START_VALUE = 0.025
DATA_END_VALUE = 0.025

class Wave_USEFUL_DATA(object):

    def __init__(self, filepath):
        wave_file = wave.open(filepath, 'rb')
        params = wave_file.getparams()
        self.framesra = params[2]
        self.frameswav = params[3]
        wave_data = wave_file.readframes(self.frameswav)
        self.datause = np.fromstring(wave_data, dtype = np.short) #16位，-32767~32767

    def get_data_length(self):
        return len(self.datause)

    def get_normalization_data(self):
        max_index = np.argmax(abs(self.datause))
        max_value = abs(self.datause[max_index])
        self.datause = self.datause / (1.0 * max_value)

    def get_wave_filtering(self):
        datause_n_2_list = [0.00] + list(self.datause[:-1])
        datause_n_2 = np.array(datause_n_2_list)

        self.datause = self.datause * 1.0 + (-0.9375) * datause_n_2
        self.get_normalization_data()

    @staticmethod
    def get_generate_hamming_windows(row, column):
        hammin_windows = [0] * row * column
        for index in range(row * column):
            hammin_windows[index] = 0.54 - 0.46 * (math.cos(2 * math.pi * index / (row * column - 1)))
        return np.array(hammin_windows)

    def get_short_time_energy(self):
        self.datause = self.datause * self.datause
        hammin_windows = self.get_generate_hamming_windows(32, 16)

        self.datause = np.convolve(self.datause, hammin_windows, 'full')
        self.get_normalization_data()

    def get_data_start_index(self):
        for index in range(len(self.datause)):
            if self.datause[index] > DATA_START_VALUE:
                return index
        return -1

    def get_data_end_index(self):
        for index in range(len(self.datause))[::-1]:
            if self.datause[index] > DATA_START_VALUE:
                return index
        return -1

    def get_useful_short_time_energy(self):
        start_index = self.get_data_start_index()
        end_index = self.get_data_end_index()
        self.datause = np.array(list(self.datause)[start_index:end_index])

    def get_compare_useful_short_time_energy(self, stand_length):
        start_index = self.get_data_start_index()
        end_index = start_index + stand_length
        if end_index <= len(self.datause):
            self.datause = np.array(list(self.datause)[start_index:end_index])
        else:
            zero_arr = [0] * (end_index - len(self.datause))
            self.datause = np.array(list(self.datause)[start_index:] + zero_arr)

    def get_compare_score(self, compare_useful_data):
        dot = (self.datause * compare_useful_data).sum()
        normStandard = (self.datause * self.datause).sum()
        normCompare = (compare_useful_data * compare_useful_data).sum()
        #print (dot,normStandard,normCompare)
        print("Success ratio: \n")
        print(100 * (dot / (math.sqrt(normStandard) * math.sqrt(normCompare))))
        return 100 * (dot / (math.sqrt(normStandard) * math.sqrt(normCompare)))

    def auto_get_usrful_data(self):
        self.get_normalization_data()
        self.get_wave_filtering()
        self.get_short_time_energy()
        self.get_useful_short_time_energy()

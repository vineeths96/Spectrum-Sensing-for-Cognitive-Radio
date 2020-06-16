import numpy as np
from scipy.stats import chi2
import matplotlib.pyplot as plt
from parameters import *


def generate_statistic_H0(NUM_STATISTICS, sigma_w, N):
    T_y = np.zeros(NUM_STATISTICS)

    for ind in range(NUM_STATISTICS):
        w = sigma_w * np.random.randn(N)

        y = w
        T_y[ind] = np.sum(np.square(y))

    return T_y


def generate_statistic_H1(NUM_STATISTICS, sigma_w, N):
    T_y = np.zeros(NUM_STATISTICS)

    for ind in range(NUM_STATISTICS):
        x = sigma_s * np.random.randn(N)
        w = sigma_w * np.random.randn(N)

        y = x + w
        T_y[ind] = np.sum(np.square(y))

    return T_y


def main():
    SNR_list = np.arange(SNR_LOW, SNR_UP, SNR_STEP)
    N = (K + 1) * (N_c + N_d)

    GAMMA_NP = np.zeros(len(SNR_list))
    GAMMA_BD = np.zeros(len(SNR_list))

    for ind, SNR in enumerate(SNR_list):
        sigma_w = np.sqrt(sigma_s ** 2 / 10 ** (SNR / 10))
        gamma_NP = chi2.isf(q=P_FA, df=N) * (sigma_w ** 2)
        gamma_BD = 2 * (sigma_s ** 2 + sigma_w ** 2) * sigma_w ** 2 / sigma_s ** 2 * (N / 2 * np.log(1 + sigma_s ** 2 / sigma_w ** 2) + np.log(1 - P_H1) - np.log(P_H1))

        GAMMA_NP[ind] = gamma_NP
        GAMMA_BD[ind] = gamma_BD

    plt.figure()
    plt.plot(SNR_list, GAMMA_NP, label="NP Threshold")
    plt.plot(SNR_list, GAMMA_BD, label="Bayes Threshold")
    plt.xlabel("SNR")
    plt.ylabel("Threshold")
    plt.title("Energy detector threshold")
    plt.legend()
    plt.savefig('./results/energy_detector_c.png')
    plt.show()


if __name__ == '__main__':
    main()

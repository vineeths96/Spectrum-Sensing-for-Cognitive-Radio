import numpy as np
from scipy.stats import chi2
import matplotlib.pyplot as plt
from cyclostationary_detector.parameters import *


def generate_statistic_H0(NUM_STATISTICS, sigma_w, N):
    """
    Generate H0 test statistics
    :param NUM_STATISTICS: Number of statistics to be produced
    :param sigma_w: Std deviation of noise
    :param N: Length of observation vector
    :return: H0 test statistics
    """

    T_y = np.zeros(NUM_STATISTICS, dtype=np.complex)

    for ind in range(NUM_STATISTICS):
        w = sigma_w * np.random.randn(N, 2).view(np.complex128)

        y = w

        # Calculate test statistic
        val = np.complex(0)
        for n in range(N_c):
            for k in range(K):
                val += y[n + k * (N_c + N_d)] * np.conjugate(y[n + k * (N_c + N_d) + N_d])

        T_y[ind] = 1 / K * val

    return T_y


def generate_statistic_H1(NUM_STATISTICS, sigma_w, N):
    """
    Generate H1 test statistics
    :param NUM_STATISTICS: Number of statistics to be produced
    :param sigma_w: Std deviation of noise
    :param N: Length of observation vector
    :return: H1 test statistics
    """

    T_y = np.zeros(NUM_STATISTICS, dtype=np.complex)

    for ind in range(NUM_STATISTICS):
        x = sigma_s * np.random.randn(N, 1)
        for k in range(K):
            x[k * (N_c + N_d): k * (N_c + N_d) + N_c] = x[k * (N_c + N_d) + N_d: (k + 1) * (N_c + N_d)]

        w = sigma_w * np.random.randn(N, 2).view(np.complex128)

        y = x + w

        # Calculate test statistic
        val = np.complex(0)
        for n in range(N_c):
            for k in range(K):
                val += y[n + k * (N_c + N_d)] * np.conjugate(y[n + k * (N_c + N_d) + N_d])

        T_y[ind] = 1 / K * val

    return T_y


def main():
    # Define the SNR where performance has to be evaluated
    SNR_list = np.arange(SNR_LOW, SNR_UP, SNR_STEP)
    N = (K + 1) * (N_c + N_d)

    P_FA_THEO = np.zeros(len(SNR_list))

    P_FA_CALC = np.zeros(len(SNR_list))
    P_D_CALC = np.zeros(len(SNR_list))

    # Evaluate the performance on H0 and H1
    for ind, SNR in enumerate(SNR_list):
        NUM_FALSE_ALARM = 0
        NUM_DETECTION = 0

        sigma_w = np.sqrt(sigma_s ** 2 / 10 ** (SNR / 10))
        gamma = chi2.isf(q=P_FA, df=2) * N_c / K * (sigma_w ** 4)

        T_y_0 = generate_statistic_H0(NUM_STATISTICS, sigma_w, N)
        T_y_1 = generate_statistic_H1(NUM_STATISTICS, sigma_w, N)

        for T in T_y_0:
            if np.square(np.abs(T)) >= gamma:
                NUM_FALSE_ALARM += 1

        for T in T_y_1:
            if np.square(np.abs(T)) >= gamma:
                NUM_DETECTION += 1

        P_FA_CALC[ind] = NUM_FALSE_ALARM / NUM_STATISTICS
        P_D_CALC[ind] = NUM_DETECTION / NUM_STATISTICS

        P_FA_THEO[ind] = P_FA

    # Plot and save the results
    plt.figure()
    plt.plot(SNR_list, P_FA_CALC, label="Calculated $P_{FA}$")
    plt.plot(SNR_list, P_D_CALC, label="Calculated $P_{D}$")
    plt.plot(SNR_list, P_FA_THEO, label="Theoretical $P_{FA}$")
    plt.xlabel("SNR")
    plt.ylabel("Probability")
    plt.title("Cyclostationary detector")
    plt.legend()
    plt.savefig('./results/cyclostationary_detector_b.png')
    plt.show()


if __name__ == '__main__':
    main()

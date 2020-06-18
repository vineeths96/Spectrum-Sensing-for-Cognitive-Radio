import numpy as np
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
    N = (K + 1) * (N_c + N_d)
    sigma_w = np.sqrt(sigma_s ** 2 / 10 ** (SNR / 10))

    T_y_0 = generate_statistic_H0(NUM_STATISTICS, sigma_w, N)
    T_y_1 = generate_statistic_H1(NUM_STATISTICS, sigma_w, N)

    # Plot and save the results
    plt.figure()
    plt.subplot(211)
    plt.hist(np.real(T_y_0), bins=125)
    plt.title("$H_{0}$ Statistic distribution - Real component")
    plt.subplot(212)
    plt.hist(np.imag(T_y_0), bins=125)
    plt.title("$H_{0}$ Statistic distribution - Imaginary component")
    plt.tight_layout()
    plt.savefig('./results/cyclostationary_detector_a_H0.png')
    plt.show()

    plt.figure()
    plt.subplot(211)
    plt.hist(np.real(T_y_1), bins=125)
    plt.title("$H_{1}$ Statistic distribution - Real component")
    plt.subplot(212)
    plt.hist(np.imag(T_y_1), bins=125)
    plt.title("$H_{1}$ Statistic distribution - Imaginary component")
    plt.tight_layout()
    plt.savefig('./results/cyclostationary_detector_a_H1.png')
    plt.show()


if __name__ == '__main__':
    main()

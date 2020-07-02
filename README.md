 ![Language](https://img.shields.io/badge/language-python--3.7-blue) [![Contributors][contributors-shield]][contributors-url] [![Forks][forks-shield]][forks-url] [![Stargazers][stars-shield]][stars-url] [![Issues][issues-shield]][issues-url] [![MIT License][license-shield]][license-url] [![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />

<p align="center">
  <a href="https://github.com/vineeths96/Spectrum-sensing-for-cognitive-radio">
    <img src="results/logo.png" alt="Logo" width="250" height="125">
  </a>
  <h3 align="center">Spectrum sensing for cognitive radio</h3>
  <p align="center">
    Spectrum sensing for cognitive radio
    <br />
    <a href=https://github.com/vineeths96/Spectrum-sensing-for-cognitive-radio><strong>Explore the repository»</strong></a>
    <br />
    <br />
    <a href=https://github.com/vineeths96/Spectrum-sensing-for-cognitive-radio/blob/master/Problem%20statement.pdf>View Problem Statement</a>
    <a href=https://github.com/vineeths96/Spectrum-sensing-for-cognitive-radio/blob/master/results/report.pdf>View Report</a>
  </p>



</p>

> tags : spectrum sensing, cognitive radio, energy detector, cyclostationary detector, ofdm, detection



<!-- ABOUT THE PROJECT -->
## About The Project

This project deals with developing an energy detector and a detector based on cyclostationarity for an OFDM based cognitive radio system and implementing and evaluating the performance of these detectors. The concept of cognitive radio is to exploit the underutilized spectral resources by reusing unused spectrum in an opportunistic manner. A cognitive radio system generally involves primary users of the spectrum, who are incumbent licensees, and secondary users who seek to opportunistically use the spectrum when the primary users are idle. The cognitive radios must sense the spectrum to detect whether it is available or not.

We derive, implement and evaluate the energy detector and the cyclostationary detector. We evaluate the performance of the detectors by plotting the Receiver Operating Characteristics (ROC) under clean and noisy conditions.

### Built With
This project was built with 

* python v3.7
* The list of libraries used for developing this project is available at [requirements.txt](requirements.txt).



<!-- GETTING STARTED -->

## Getting Started

Clone the repository into a local machine using

```shell
git clone https://github.com/vineeths96/Spectrum-sensing-for-cognitive-radio
```

### Prerequisites

Please install required libraries by running the following command (preferably within a virtual environment).

```shell
pip install -r requirements.txt
```



### Instructions to run

The `energy_detector.py` acts as an interface to the Energy detector implementations in `energy_detector` package. The `cyclostationary_detector.py` acts as an interface to the Cyclostationary detector implementations in `cyclostationary_detector` package. The python files take care of the generating the test statistics, implementation of hypothesis testing and the plotting of the results.

The respective program can be executed by

```shell
python <file_name>.py
```



<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Vineeth S - vs96codes@gmail.com

Project Link: [https://github.com/vineeths96/Spectrum-sensing-for-cognitive-radio](https://github.com/vineeths96/Spectrum-sensing-for-cognitive-radio)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/vineeths96/Spectrum-sensing-for-cognitive-radio.svg?style=flat-square
[contributors-url]: https://github.com/vineeths96/Spectrum-sensing-for-cognitive-radio/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/vineeths96/Spectrum-sensing-for-cognitive-radio.svg?style=flat-square
[forks-url]: https://github.com/vineeths96/Spectrum-sensing-for-cognitive-radio/network/members
[stars-shield]: https://img.shields.io/github/stars/vineeths96/Spectrum-sensing-for-cognitive-radio.svg?style=flat-square
[stars-url]: https://github.com/vineeths96/Spectrum-sensing-for-cognitive-radio/stargazers
[issues-shield]: https://img.shields.io/github/issues/vineeths96/Spectrum-sensing-for-cognitive-radio.svg?style=flat-square
[issues-url]: https://github.com/vineeths96/Spectrum-sensing-for-cognitive-radio/issues
[license-shield]: https://img.shields.io/badge/License-MIT-yellow.svg
[license-url]: https://github.com/vineeths96/Spectrum-sensing-for-cognitive-radio/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/vineeths


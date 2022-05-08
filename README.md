# Mimicry_
## A ML-app that detects malicious URL addresses by mimicking the language expertise of humans. Deployed API with Flask and Docker. Frontend Jquery.
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)

Screenshot:
<p align="center">
  <img src="https://github.com/henningstud/mimic_url_classifier/blob/main/screenshot1.jpeg" style="height:250px;">
</p>

The RF mimics the behaviour of an experienced professional by assessing the potential threat of the URL simply by evaluating its language. Each time another char of the URL is being typed in the field above an AJAX-call is sent to a Flask-API, which governs the trained RF.

Note: This is a POC that utilizes public blacklists and the most used websites (worldwide). If an URL you condemn harmful (e.g. NSF) is not recognized as malicious by the RF-mode, it is because these kinds of websites are not thouroughly included in most blacklists. If you want to add these websites to the detection capabilities of this project, you need to train the RF-model on corresponding dataset.

For a detailed explanation visit: <a href="https://www.researchgate.net/publication/358724855_Einsatz_von_Machine_Learning_bei_der_Abwehr_webbasierter_Angriffe_am_Beispiel_von_URL-Blacklists">https://www.researchgate.net/publication/...</a>

## Key-Features
- Trained on 500.000 URLs
- Classification-Accuracy of up to 96% (malicious or normal): Backtested in multiple scenarios against a classical blacklist
- Novel approach to detect malicious URLs
- Design, Training and Test completely documented in a publication (see below)

## Quick Start with **[Docker](https://www.docker.com)**

```shell
# 1. First, clone the repo
$ git clone https://github.com/henningstud/mimic_url_classifier.git
$ cd mimicry
# 2. Build Docker image
$ docker build -t mimicry .
# 3. Run
$ docker run -it --rm -p 5000:5000 mimicry
```
Open http://localhost:5000 and the app should appear.

## My publication for this project

[Application of machine learning for the defense against web-based attacks by example of DNS-Blacklists](https://www.researchgate.net/publication/358724855_Einsatz_von_Machine_Learning_bei_der_Abwehr_webbasierter_Angriffe_am_Beispiel_von_URL-Blacklists)

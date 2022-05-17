# Mimicry_
## ML-app to detect malicious URL addresses by mimicking the language expertise of humans. Deployed API with Flask, Scikit and Docker. Frontend JQuery.
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)

<p align="center">
  <img src="https://github.com/henningorlowski/mimic_url_classifier/blob/main//static/images/logo.svg" style="height:250px;">
</p>

The RF mimics the behaviour of an experienced professional by assessing the potential threat of the URL simply by evaluating its language. Each time another char of the URL is being typed in the classification_field an AJAX-call is sent to a Flask-API, which governs the trained RF.

Note: This is a POC that utilizes public blacklists and the most used websites (worldwide). If an URL you condemn harmful (e.g. NSFW) is not recognized as malicious by the RF-mode, it is because these kinds of websites are not thouroughly included in most blacklists. If you want to add these websites to the detection capabilities of this project, you need to train the RF-model on a corresponding dataset.

For a detailed explanation visit: https://www.researchgate.net/publication/358724855_Einsatz_von_Machine_Learning_bei_der_Abwehr_webbasierter_Angriffe_am_Beispiel_von_URL-Blacklists

## Key-Features
- Trained on 500.000 URLs
- Classification-Accuracy of up to 92% (malicious or normal): Backtested in multiple scenarios against a classical blacklist
- Novel approach to detect malicious URLs
- Design, Training and Test completely documented in a publication (see below)
- Fully Unittested

## Quick Start with **[Docker](https://www.docker.com)**

```shell
# 1. First, clone the repo
git clone https://github.com/henningorlowski/mimic_url_classifier.git
cd mimic_url_classifier
# 2. Build Docker image
docker build -t mimicry .
# 3. Run
docker run -it --rm -p 5000:5000 mimicry
```
Open http://localhost:5000 and the app should appear.


## Test API from CLI
```shell
curl -X POST localhost:5000/prediction -H 'Content-Type: application/json' -d '{"url":"google.de"}'
```
Which should lead to the response:
{"prediction":"secure","probability_malicious":"0","probability_normal":"100"}
<br /><br />
Alternatively run all Unittests (100% coverage)
```shell
python app_test.py
```


## ToDo
- Add Selenium Frontend test to unittests
- Implement Anomaly Detection (Source Code <-> WebsiteRendering) with CNN
- Add support for protocol validation (HTTP, HTTPS), GET-Requests

## Publication for this project

[Application of machine learning for the defense against web-based attacks by example of DNS-Blacklists](https://www.researchgate.net/publication/358724855_Einsatz_von_Machine_Learning_bei_der_Abwehr_webbasierter_Angriffe_am_Beispiel_von_URL-Blacklists)

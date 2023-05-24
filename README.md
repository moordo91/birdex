# Birdex: Your Personal Bird Index

This is the project for the more enjoyable world.

## Introduction

Birdex is a pioneering mobile web application that merges Computer Vision and Machine Learning technologies to recognize bird species and share fascinating descriptions about them. Simply snap a photo of a bird, and Birdex will not only identify the species but also register it to your own personal encyclopedia. This project provides an exciting blend of exploration and learning, instilling the joy of discovering and collecting an array of avian species.

Birdex used EfficientNet and Tensorflow.js to build a bespoke model capable of identifying birds.

---

## Under Deveolopment

Please note that this project is a work in progress and does not yet offer the complete range of features that we aim to implement. Aspects such as code stability, user interface design, and comprehensive feature implementation are currently undergoing active development. Additionally, much more novel and attractive features will be included in the near future. I am also planning a transition towards using Flutter and Dart, moving away from the current webpage structure. 

---

## Process
![Capture process](/screenshots/homepage.png)

![Birdex Process](/screenshots/recognition.png)

*Figures: Screenshots from Birdex application.*

---

## Working Video

A working video demonstration of the Birdex application can be found here: [[YouTube]]([your-link-to-the-video](https://www.youtube.com/watch?v=V4dmQvzKQ8E))

*Note: Initially, the image is out of focus, but it will soon be normalized. Also, please be aware that the application of the image is a prototype and is somewhat different from the current UI/UX.*

---

## Features

1. **Bird Recognition:** Utilizes Deep Learning (EfficientNet and MobileNet) and Computer Vision to identify bird species from images.
2. **Birdex Encyclopedia:** Upload your own personal bird photograph with each new discovery.
3. **Educational Content:** Provides detailed insights about each bird species upon recognition.
4. **Mobile Friendly:** The website is fully optimized for smartphones, using your cellphone camera and making bird spotting an enjoyable mobile activity.

As I said before, more fun and brilliant ideas will be implemented soon!

---

## Tech Stack

* **Tensorflow:** Used for creating the custom machine learning model for bird recognition.
* **TensorFlow.js:** Responsible for handling the machine learning tasks in the browser.
* **Flask:** serves different webpages, handles data updates, and interacts with a database.
* **Web Technologies:** HTML, CSS, and JavaScript are used to build the user interface and manage web interactions.
* In addition, **Teachable Machine** was referred to implement the interworking between the deep learning model and JavaScript. **Bootstrap** was used to architect the main page. The pop-up boxes are designed by the **SweetAlert2 library**. The database was created using **MySQL**.

---

## Dataset and Model

Dataset was crawled from the Google image search.
**MobileNet** and **EfficientNet** with basic data augmentation methods are used to train Birdex. You can refer to the following papers:

- [MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications](https://arxiv.org/abs/1704.04861)
- [EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks](https://arxiv.org/abs/1905.11946)


---

## Usage

Unfortunately, you have to run the application locally because I don't have enough money to run the server in real time 24/7.

```bash
git clone https://github.com/moordo91/birdex.git
```

---

## Contact
If you have any queries or suggestions, feel free to reach out to us.
You can contact me at [moordo91@gmail.com](mailto:moordo91@gmail.com).
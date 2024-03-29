# Birdex: Your Own Bird Index

This is the project for the more enjoyable world.

## Introduction

Birdex is a pioneering mobile web application that merges Computer Vision and Machine Learning technologies to recognize bird species and share fascinating descriptions about them. Simply snap a photo of a bird, and Birdex will not only identify the species but also register it to your own personal encyclopedia. This project provides an exciting blend of exploration and learning, instilling the joy of discovering and collecting an array of avian species.

---

## Under Deveolopment

Please note that this project is a work in progress and does not yet offer the complete range of features that we aim to implement. Aspects such as code stability, user interface design, and comprehensive feature implementation are currently undergoing active development. Additionally, much more novel and attractive features will be included in the near future. I am also planning a transition towards using Flutter and Dart, moving away from the current webpage structure. 

---

## Process

![Capture process](https://github.com/moordo91/birdex/assets/82254758/c7abf27b-45f6-46e8-8501-211558cd0f2b)

![Birdex Process](https://github.com/moordo91/birdex/assets/82254758/6e6a2244-38ce-4c12-8549-2b0af532337b)

*Figures: Screenshots from Birdex application.*

---

## Working Video

A basic working video demonstration of the Birdex application can be found here: [[YouTube]](https://www.youtube.com/watch?v=V4dmQvzKQ8E)

*Note: Initially, the video is out of focus, but it will soon be normalized. Also, please be aware that the application of the video is a prototype and is somewhat different from the current UI/UX.*

---

## Features

1. **Bird Recognition:** Utilizes Deep Learning Computer Vision model (EfficientNet and MobileNet) to identify bird species from images.
2. **Birdex Encyclopedia:** Upload your own personal bird photograph with each new discovery.
3. **Educational Content:** Provides detailed insights about each bird species upon recognition.
4. **Mobile Friendly:** The website is fully optimized for smartphones, using your cellphone camera and making bird spotting an enjoyable mobile activity.

As I said before, more fun and brilliant ideas will be implemented soon!

---

## Tech Stack

* **Tensorflow:** Used for creating the machine learning model for bird recognition.
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

## Reference and Special Thanks

I wrote most of the code myself, and the code I referred to on the Internet was also modified considerably. However, I cannot help but admit that I have received a lot of help from the following contents.

- [Teachable Machine](https://teachablemachine.withgoogle.com/)
- [SweetAlert2](https://sweetalert2.github.io/)
- [Pokedex](https://pokemonkorea.co.kr/pokedex)
- [JoCoding](https://www.youtube.com/@jocoding)
- [Flask lecture of coohde](https://www.youtube.com/playlist?list=PLuHgQVnccGMClNOIuT3b3M4YZjxmult2y)

---

## Contact
If you have any queries or suggestions, feel free to reach out to us.
You can contact me at 📧[moordo91@gmail.com](mailto:moordo91@gmail.com).

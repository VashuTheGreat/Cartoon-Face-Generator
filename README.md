# Emoji Face Generator 🎨🤖

A Deep Learning project that generates custom emoji-style faces using Generative Adversarial Networks (GANs). This model is trained on the Google Cartoon Set to create diverse and unique cartoon avatars.

## 🚀 Overview

The **Emoji Face Generator** leverages the power of GANs to synthesize high-quality cartoon faces. By training on a massive dataset of 100,000 cartoon images, the model learns to generate various facial features, expressions, and styles, providing a fun way to create custom avatars.

## 📊 Dataset

The model is trained on the **[Google Cartoon Set (100k)](https://www.kaggle.com/datasets/brendanartley/cartoon-faces-googles-cartoon-set)**.
- **Size**: 100,000 images.
- **Format**: 2D cartoon avatars with various attributes (hair, eyes, face shape, etc.).
- **Diversity**: High variability in facial features and accessories.

## 🧠 Architecture

The project implements a standard GAN architecture:
- **Generator**: A convolutional neural network that takes random noise as input and transforms it into a realistic cartoon face.
- **Discriminator**: A convolutional neural network that learns to distinguish between real images from the dataset and fake images produced by the generator.

The two networks are trained simultaneously in a competitive process, leading to the generation of increasingly realistic faces.

## 🛠️ Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/emohi_face_generator.git
   cd emohi_face_generator
   ```

2. **Install dependencies**:
   Ensure you have Python installed, then run:
   ```bash
   pip install torch torchvision matplotlib numpy kagglehub
   ```

3. **Download the Dataset**:
   The notebook includes a script to download the dataset using `kagglehub`.

## 📖 Usage

1. Open the Jupyter Notebook:
   ```bash
   jupyter notebook Emoji_Face_Generator.ipynb
   ```
2. Run the cells sequentially to:
   - Download and preprocess the dataset.
   - Define the Generator and Discriminator models.
   - Start the training process.
   - Generate and visualize new emoji faces.

## 🖼️ Results

*Generated faces will appear here after training.*

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙌 Acknowledgments

- Thanks to Google for providing the Cartoon Set.
- Inspired by various GAN implementations in the PyTorch community.

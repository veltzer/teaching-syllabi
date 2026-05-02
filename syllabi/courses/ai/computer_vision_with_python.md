---
tags:
  - data-and-ai:machine-learning
  - languages:python
level: intermediate
category: ai
duration_hours: 32
audience:
  - audiences:developers
  - audiences:data-scientists
---
<!-- course: computer_vision_with_python -->
# Computer Vision with `Python`

## Description
This course provides a comprehensive guide to computer vision using `Python`. Participants will progress
from digital image fundamentals and classical image processing with `OpenCV` to modern `deep learning`
approaches for image classification, object detection, and segmentation. The course covers feature
detection, transfer learning with architectures like ResNet and EfficientNet, object detection
with YOLO and `Faster R-CNN`, image segmentation with `U-Net` and `Mask R-CNN`, face recognition,
OCR, and an overview of generative models. Hands-on work uses `PyTorch` and `TensorFlow`/`Keras`.

## Duration
32 hours / 4 days

## Intended Audience
* software developers building vision-based applications
* data scientists working with image and video data

## Prerequisites
* Proficiency in `Python` programming
* Basic understanding of `machine learning` concepts (training, evaluation, overfitting)
* Familiarity with `NumPy` and `array` operations
* Basic linear algebra knowledge (matrices, convolutions)

## Objectives
* **Process and manipulate images** using `OpenCV` for filtering, edge detection, morphology, and contour analysis
* **Detect and describe features** using classical methods such as SIFT, ORB, and HOG
* **Build image classification models** using CNNs and transfer learning with ResNet, VGG, and EfficientNet
* **Implement object detection pipelines** using YOLO, `SSD`, and `Faster R-CNN`
* **Perform image segmentation** using `U-Net` and `Mask R-CNN` for pixel-level predictions
* **Deploy computer vision models** for production use with `PyTorch` and `TensorFlow`/`Keras`

## Outline
<!-- chapter: digital-image-fundamentals, duration: 2h -->
* Digital Image Fundamentals
    * Image representation
        * Pixels, channels, and color spaces
        * Image formats and encoding
        * Coordinate systems
    * Image operations
        * Reading and writing images
        * Resizing and cropping
        * Color space conversions (RGB, HSV, grayscale)
    * Image histograms
        * Histogram computation
        * Histogram equalization
        * Histogram comparison
<!-- chapter: image-processing-with-opencv, duration: 4h -->
* Image Processing with `OpenCV`
    * Filtering
        * Gaussian blur and smoothing
        * Median and bilateral filtering
        * Sharpening and custom kernels
    * Edge detection
        * Sobel and Scharr operators
        * Canny edge detection
        * Laplacian edge detection
    * Morphological operations
        * Erosion and dilation
        * Opening and closing
        * Morphological gradient
        * `Top` hat and black hat
    * Contours
        * Contour detection and extraction
        * Contour properties (area, perimeter, bounding box)
        * Contour approximation
        * Shape matching
    * Geometric transformations
        * Affine transformations
        * Perspective transformations
        * Image warping
<!-- chapter: feature-detection, duration: 3h -->
* Feature Detection
    * SIFT (Scale-Invariant Feature Transform)
        * Keypoint detection
        * Descriptor computation
        * Feature matching
    * ORB (Oriented FAST and Rotated BRIEF)
        * Fast keypoint detection
        * Binary descriptors
        * Matching strategies
    * HOG (Histogram of Oriented Gradients)
        * Gradient computation
        * Cell and block normalization
        * Applications in pedestrian detection
    * Feature matching
        * Brute-force matching
        * FLANN-based matching
        * Ratio test filtering
        * Homography estimation
<!-- chapter: image-classification, duration: 3h -->
* Image Classification
    * Convolutional Neural Networks
        * Convolution layers
        * Pooling layers
        * Activation functions
        * Building a CNN from scratch
    * Transfer learning
        * Pre-trained model concepts
        * VGG architecture
        * ResNet architecture
        * EfficientNet architecture
    * Training strategies
        * Fine-tuning vs feature extraction
        * Data augmentation
        * Learning rate scheduling
        * Regularization techniques
    * Model evaluation
        * Accuracy, precision, recall, F1
        * Confusion matrix
        * ROC and AUC curves
        * Grad-CAM visualization
<!-- chapter: object-detection, duration: 4h -->
* Object Detection
    * Object detection fundamentals
        * Bounding box regression
        * Intersection over Union (IoU)
        * Non-maximum suppression
        * Anchor boxes
    * YOLO (You Only Look Once)
        * YOLO architecture overview
        * YOLOv5 and YOLOv8 variants
        * Training custom YOLO models
        * Real-time detection
    * `SSD` (Single Shot Detector)
        * Multi-scale feature maps
        * Default boxes
        * Training and inference
    * `Faster R-CNN`
        * Region proposal network
        * RoI pooling
        * Two-stage detection pipeline
        * Fine-tuning for custom datasets
    * Model evaluation
        * Mean average precision (mAP)
        * Precision-recall curves
        * Speed-accuracy trade-offs
<!-- chapter: image-segmentation, duration: 3h -->
* Image Segmentation
    * Semantic segmentation
        * Pixel-level classification
        * Fully convolutional networks
        * `U-Net` architecture
        * Training with segmentation masks
    * Instance segmentation
        * `Mask R-CNN` architecture
        * Instance mask generation
        * Panoptic segmentation overview
    * Training segmentation models
        * Loss functions (cross-entropy, Dice loss, focal loss)
        * Data preparation and annotation
        * Augmentation for segmentation
    * Evaluation metrics
        * IoU (Jaccard index)
        * Dice coefficient
        * Pixel accuracy
<!-- chapter: face-detection-and-recognition, duration: 3h -->
* Face Detection and Recognition
    * Face detection
        * Haar cascades
        * HOG-based detection
        * `Deep learning` face detectors (MTCNN, RetinaFace)
    * Face recognition
        * Face embeddings
        * FaceNet and ArcFace
        * Similarity and verification
    * Face analysis
        * Landmark detection
        * Age and gender estimation
        * Emotion recognition
    * Practical considerations
        * Privacy and ethical concerns
        * Bias in face recognition systems
        * Real-time face processing
<!-- chapter: optical-character-recognition, duration: 3h -->
* Optical Character Recognition
    * OCR fundamentals
        * Text detection vs text recognition
        * Document image preprocessing
        * Binarization and deskewing
    * Tesseract OCR
        * Tesseract configuration
        * Page segmentation modes
        * Language and script support
        * Custom training
    * `Deep learning`-based OCR
        * CRNN architecture
        * Attention-based recognition
        * Scene text detection (EAST, CRAFT)
    * Post-processing
        * Spell checking and correction
        * Layout analysis
        * Structured data extraction
<!-- chapter: image-generation, duration: 2h -->
* Image Generation
    * Generative Adversarial Networks
        * GAN architecture (generator and discriminator)
        * Training dynamics
        * DCGAN and StyleGAN overview
        * Image-to-image translation (Pix2Pix, CycleGAN)
    * Diffusion models overview
        * Denoising diffusion concepts
        * `Stable Diffusion` architecture
        * Conditional generation
    * Practical applications
        * Data augmentation with generative models
        * Super-resolution
        * Inpainting
<!-- chapter: video-analysis, duration: 2h -->
* Video Analysis
    * Video processing fundamentals
        * Frame extraction and processing
        * Video `I/O` with `OpenCV`
        * Frame rate and resolution handling
    * Motion and tracking
        * Optical flow
        * Background subtraction
        * Object tracking algorithms (SORT, DeepSORT)
    * Video understanding
        * Action recognition
        * Temporal modeling
        * Video classification
<!-- chapter: model-deployment, duration: 3h -->
* Model Deployment
    * Model export and optimization
        * `ONNX` export
        * TorchScript and tracing
        * Model quantization
        * TensorRT optimization
    * Serving infrastructure
        * `REST` `API` serving (Flask, `FastAPI`)
        * Batch inference pipelines
        * Edge deployment considerations
    * Working with `PyTorch`
        * `PyTorch` model development workflow
        * torchvision utilities
        * Custom datasets and data loaders
    * Working with `TensorFlow`/`Keras`
        * `Keras` model development workflow
        * tf.data pipeline
        * `TensorFlow` Lite for mobile
        * `TensorFlow`.js for browser

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026

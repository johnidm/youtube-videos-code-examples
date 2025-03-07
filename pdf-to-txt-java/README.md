# OCR in Java

This project demonstrates how to perform Optical Character Recognition (OCR) using the Tesseract library in Java.

## Setup

#### Install Tesseract OCR:

On Mac OS, you can install Tesseract using Homebrew:
```sh
brew install tesseract
```

On Debian-based distributions (e.g., Ubuntu), you can install Tesseract using apt:
```sh
sudo apt install tesseract-ocr tesseract-ocr-eng
```

## Usage

The main class is `org.example.Main`. It performs OCR on an image file named `contract.jpg` located in the `resources` directory.

## Dependencies

- [Tess4J](https://github.com/nguyenq/tess4j) - A Java JNA wrapper for Tesseract OCR API.

## Running the Project

To run the project, use the following command:
```sh
mvn exec:java -Dexec.mainClass="org.example.Main"
```
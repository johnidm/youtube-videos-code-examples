package org.example;

import net.sourceforge.tess4j.Tesseract;
import net.sourceforge.tess4j.TesseractException;

import java.io.File;
import java.util.Objects;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        // On Mac OS, solve the 'libtesseract.dylib not found' error.
        // https://github.com/nguyenq/tess4j/issues/194
        if (System.getProperty("os.name").toLowerCase().contains("mac")) {
            System.setProperty("jna.library.path", "/opt/homebrew/Cellar/tesseract/5.5.0/lib");
        }
        System.setProperty("jna.library.path", "/opt/homebrew/Cellar/tesseract/5.5.0/lib");

        Tesseract tesseract = new Tesseract();

        // Set the path to the Tesseract data directory
        // Replace this with the path where you stored the language data files
        String datapath;
        if (System.getProperty("os.name").toLowerCase().contains("mac")) {
            datapath = "/opt/homebrew/Cellar/tesseract/5.5.0/share/tessdata/";    
        } else {
            datapath = "/usr/share/tesseract-ocr/4.00/tessdata";
        }
        tesseract.setDatapath(datapath);

        // Perform OCR on the image
        tesseract.setLanguage("eng");

        try {
            String imagePath = Objects.requireNonNull(Main.class.getClassLoader().getResource("contract.jpg")).getPath();
            File imageFile = new File(imagePath);

            String result = tesseract.doOCR(imageFile);

            System.out.println("OCR Result:");
            System.out.println(result);
        } catch (TesseractException e) {
            System.err.println("Error during OCR process: " + e.getMessage());
        }
    }
}
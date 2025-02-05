package org.example.service;

import java.io.File;

import org.example.helpers.Logging;

import net.sourceforge.tess4j.Tesseract;

public class OcrParserTesseractService implements OcrParser {

    @Override
    public String parse(String imagePath) throws Exception {
        Logging.info("OcrParserTesseractService.parse()");

        // On Mac OS, solve the 'libtesseract.dylib not found' error.
        // https://github.com/nguyenq/tess4j/issues/194
        boolean isMac = System.getProperty("os.name").toLowerCase().contains("mac");
        if (isMac) {
            System.setProperty("jna.library.path", "/opt/homebrew/Cellar/tesseract/5.5.0/lib");
        }

        Tesseract tesseract = new Tesseract();

        // Set the path to the Tesseract data directory
        // Replace this with the path where you stored the language data files
        // https://github.com/tesseract-ocr/tessdata_fast/
        //  wget https://github.com/tesseract-ocr/tessdata_fast/raw/refs/heads/main/por.traineddata
        String datapath;
        if (isMac) {
            datapath = "/opt/homebrew/Cellar/tesseract/5.5.0/share/tessdata/";
        } else {
            datapath = "/usr/share/tesseract-ocr/4.00/tessdata";
        }
        tesseract.setDatapath(datapath);

        // Perform OCR on the image
        tesseract.setLanguage("por"); // Set the language if the image is in a different language

        File imageFile = new File(imagePath);

        return tesseract.doOCR(imageFile);
    }

}

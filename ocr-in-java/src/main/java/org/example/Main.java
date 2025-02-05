package org.example;

import org.example.helpers.Logging;
import org.example.service.OcrParser;
import org.example.service.OcrParserTesseractService;
import org.example.service.PdfParser;
import org.example.service.PdfParserPDFBoxService;
import java.io.FileWriter;
import java.io.IOException;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {

    public static void saveTextToFile(String text, String outputPath) {
        try (FileWriter writer = new FileWriter(outputPath)) {
            writer.write(text);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    public static void main(String[] args) throws Exception {
        // String filePath = "/Users/johnimarangon/Projects/youtube-videos-code-examples/ocr-in-java/contrato.pdf";
        String filePath = "/Users/johnimarangon/Projects/youtube-videos-code-examples/ocr-in-java/contarto-imagem.pdf";

        PdfParser pdf = new PdfParserPDFBoxService();
        String text = pdf.parse(filePath);
        if (text.trim().isEmpty()) {
            OcrParser ocr = new OcrParserTesseractService();
            text = ocr.parse(filePath);
        }
        Logging.print(text);
        String outputPath = "/Users/johnimarangon/Projects/youtube-videos-code-examples/ocr-in-java/output.txt";
        saveTextToFile(text, outputPath);
    }
}
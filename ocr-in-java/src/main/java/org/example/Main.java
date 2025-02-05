package org.example;

import org.example.helpers.Logging;
import org.example.service.OcrParser;
import org.example.service.OcrParserTesseractService;
import org.example.service.PdfParser;
import org.example.service.PdfParserPDFBoxService;
import java.io.FileWriter;
import java.io.IOException;
import java.io.File;
import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void saveTextToFile(String text, String outputPath) {
        try (FileWriter writer = new FileWriter(outputPath)) {
            writer.write(text);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static List<String> listPDFFiles(String directoryPath) {
        List<String> pdfFiles = new ArrayList<>();
        File directory = new File(directoryPath);
        if (directory.exists() && directory.isDirectory()) {
            File[] files = directory.listFiles((_, name) -> name.toLowerCase().endsWith(".pdf"));
            if (files != null) {
                for (File file : files) {
                    pdfFiles.add(file.getAbsolutePath());
                }
            }
        }
        return pdfFiles;
    }

    public static String convertoToText(String filePath) throws Exception {
        Logging.success(filePath);
        PdfParser pdf = new PdfParserPDFBoxService();
        String text = pdf.parse(filePath);
        if (text.trim().isEmpty()) {
            OcrParser ocr = new OcrParserTesseractService();
            text = ocr.parse(filePath);
        }
        Logging.print(text);
        return text;
    }

    public static void main(String[] args) throws Exception {
        String directoryPath = "/home/johni.marangon@softplan.com.br/Projects/sienge-ai-instrucoes/documents/";
        List<String> pdfFiles = listPDFFiles(directoryPath);
        for (String pdfFile : pdfFiles) {
            String text = convertoToText(pdfFile);
            String outputPath = pdfFile.replace(".pdf", ".txt");
            saveTextToFile(text, outputPath);
        }
    }
}
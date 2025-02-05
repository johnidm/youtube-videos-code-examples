package org.example.service;

import org.apache.pdfbox.Loader;
import org.apache.pdfbox.io.RandomAccessReadBufferedFile;
import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.text.PDFTextStripper;
import org.example.helpers.Logging;

public class PdfParserPDFBoxService implements PdfParser {

    @Override
    public String parse(String filePath) throws Exception {
        Logging.info("PdfParserPDFBoxService.parse()");
        PDDocument document = Loader.loadPDF(new RandomAccessReadBufferedFile(filePath));
        if (!document.isEncrypted()) {
            PDFTextStripper pdfStripper = new PDFTextStripper();
            return pdfStripper.getText(document);
        }
        return "";
    }

}

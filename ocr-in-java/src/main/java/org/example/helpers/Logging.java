package org.example.helpers;

import static com.diogonunes.jcolor.Ansi.colorize;
import static com.diogonunes.jcolor.Attribute.*;

public class Logging {

    public static void info(String message) {
        System.out.println(colorize(message, BOLD(), BRIGHT_YELLOW_TEXT()));
    }

    public static void print(String message) {
        System.out.println(colorize(message, BOLD(), BRIGHT_YELLOW_TEXT(), RED_BACK()));

    }

}

#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <unistd.h>
#include <iomanip>

std::string convertToEnglish(double number) {
    std::ostringstream oss;
    oss << number;
    std::string numberStr = oss.str();
    std::string command = "number -l " + numberStr;
    FILE* pipe = popen(command.c_str(), "r");
    if (!pipe) {
        return "";
    }
    char buffer[128];
    std::string result = "";
    while (fgets(buffer, sizeof(buffer), pipe) != NULL) {
        result += buffer;
    }
    pclose(pipe);
    result.erase(result.find_last_not_of(" \n\r\t")+1); // Remove trailing whitespace and line breaks
    return result;
}

int main() {
    // Install bsdgames using apt-get
    std::system("sudo apt-get install bsdgames");

    // Given data
    std::vector<double> ratings = {3.0, 3.0, 4.0, 4.5, 4.5, 4.5, 5.5, 5.5, 5.5, 5.5, 5.5, 6.5, 6.5, 7.0, 7.0, 7.0, 7.5, 7.5, 7.5, 7.5};

    // Calculate the 5-number summary
    double min_val = *std::min_element(ratings.begin(), ratings.end());
    double q1 = *std::next(ratings.begin(), static_cast<int>(ratings.size() * 0.25));
    double median = *std::next(ratings.begin(), static_cast<int>(ratings.size() * 0.5));
    double q3 = *std::next(ratings.begin(), static_cast<int>(ratings.size() * 0.75));
    double max_val = *std::max_element(ratings.begin(), ratings.end());

    // Convert the numbers to English
    std::string min_english = convertToEnglish(min_val);
    std::string q1_english = convertToEnglish(q1);
    std::string median_english = convertToEnglish(median);
    std::string q3_english = convertToEnglish(q3);
    std::string max_english = convertToEnglish(max_val);

    // Set column width for better formatting
    int column_width = 20;

    // Print the 5-number summary header
    std::cout << "The 5-number summary is:" << std::endl;

    // Print the column titles
    std::cout << std::left << std::setw(column_width) << "Quartiles:" << std::setw(column_width) << "Number:" << std::setw(column_width) << "English:" << std::endl;

    // Print the 5-number summary
    std::cout << std::left << std::setw(column_width) << "Minimum:" << std::setw(column_width) << min_val << std::setw(column_width) << min_english << std::endl;
    std::cout << std::left << std::setw(column_width) << "Quartile Q1:" << std::setw(column_width) << q1 << std::setw(column_width) << q1_english << std::endl;
    std::cout << std::left << std::setw(column_width) << "Median:" << std::setw(column_width) << median << std::setw(column_width) << median_english << std::endl;
    std::cout << std::left << std::setw(column_width) << "Quartile Q3:" << std::setw(column_width) << q3 << std::setw(column_width) << q3_english << std::endl;
    std::cout << std::left << std::setw(column_width) << "Maximum:" << std::setw(column_width) << max_val << std::setw(column_width) << max_english << std::endl;

    return 0;
}

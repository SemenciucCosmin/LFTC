from Labs.Lab3Lab4.pythonProject.Scanner.Scanner import Scanner

if __name__ == "__main__":
    scanner = Scanner()
    scanner.empty_output_file()
    scanner.load_tokens()
    scanner.scan_file("Programs/p1.txt")
    scanner.scan_file("Programs/p2.txt")
    scanner.scan_file("Programs/p3.txt")
    scanner.scan_file("Programs/p1err.txt")

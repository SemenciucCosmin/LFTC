from Labs.Lab3.pythonProject.Scanner import Scanner

if __name__ == "__main__":
    scanner = Scanner()
    scanner.empty_output_file()
    scanner.load_tokens()
    scanner.scan_file("p1.txt")
    scanner.scan_file("p2.txt")
    scanner.scan_file("p3.txt")
    scanner.scan_file("p1err.txt")

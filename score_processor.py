class ScoreProcessor:

    def process_score_file(self, file_path: str) -> int:
        file = None

        try:
            # Open the file
            file = open(file_path, "r")

            # Read content and remove extra spaces
            content = file.read().strip()

            # Convert to integer
            score = int(content)

            # Multiply by 10
            result = score * 10

        except FileNotFoundError:
            print("Error: File not found.")
            raise

        except ValueError:
            print("Error: Invalid data format. File must contain a number.")
            raise

        else:
            print("Data processed successfully")
            return result

        finally:
            # Cleanup block
            if file:
                file.close()

            print("File cleanup completed")


# Optional manual testing
if __name__ == "__main__":
    processor = ScoreProcessor()

    try:
        output = processor.process_score_file("score.txt")
        print("Final Result:", output)

    except Exception:
        print("Program ended with an error.")
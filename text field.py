import re

# Input and output file paths
input_file = "emails.txt"
output_file = "extracted_emails.txt"

# Read content from the input file
with open(input_file, "r") as file:
    content = file.read()

# Regular expression to extract emails
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", content)

# Write the extracted emails to output file
with open(output_file, "w") as file:
    for email in emails:
        file.write(email + "\n")

print("✅ All email addresses extracted and saved successfully.")
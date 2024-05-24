def wrap_text(text, line_length):
    words = text.split()  # Split the text into words
    lines = []
    current_line = []

    for word in words:
        if len(' '.join(current_line + [word])) <= line_length:
            current_line.append(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]

    if current_line:
        lines.append(' '.join(current_line))

    return '\n'.join(lines)

# Read the text from a file
with open('input.txt', 'r') as file:
    text = file.read()

# Specify the desired line length
line_length = 20  # Adjust this to your preferred line length

# Wrap the text to the desired line length
wrapped_text = wrap_text(text, line_length)

# Write the wrapped text to a new file
with open('output.txt', 'w') as file:
    file.write(wrapped_text)

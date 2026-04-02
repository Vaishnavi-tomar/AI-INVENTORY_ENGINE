# 1. Use an official Python image with GPU support (Slim version to save space)
FROM python:3.10-slim

# 2. Set the directory inside the container where our code will live
WORKDIR /app

# 3. Copy our list of libraries into the container
COPY requirements.txt .

# 4. Install the AI libraries (Torch, Chronos, Gradio)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of our project files (The Engine and Data)
COPY . .

# 6. Open the "Port" that Gradio uses to show the website
EXPOSE 7860

# 7. The command to start our AI Engine
CMD ["python", "Inventory_Engine.py"]

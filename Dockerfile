FROM python:3.11-slim
WORKDIR /app
COPY *.py inventory.json ./
# Default: run every Lab 8 section test in order. Run the menu app with:
#   docker run -it <image> python main.py
CMD ["sh", "-c", "for f in [0-9]*test.py; do echo \"\n########## $f ##########\"; python \"$f\" || exit 1; done"]

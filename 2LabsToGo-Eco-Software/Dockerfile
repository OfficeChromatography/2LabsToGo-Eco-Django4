FROM debian:bookworm

ENV PYTHONUNBUFFERED=1

# Install prerequisites (gnupg for adding the Raspberry Pi repo)
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    gnupg \
    ca-certificates \
    curl

# Add the Raspberry Pi repository and GPG key
RUN echo "deb http://archive.raspberrypi.org/debian/ bookworm main" > /etc/apt/sources.list.d/raspi.list \
    && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 82B129927FA3303E

# Install Python and picamera2
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-picamera2

# Clean up APT caches to reduce image size
RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements/base.txt /base_requirements4.txt
RUN pip install --no-cache-dir --break-system-packages -r /base_requirements4.txt

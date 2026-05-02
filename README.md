# Bright-Vision

### A Smart Wearable for the Visually Impaired 🚀

**Bright Vision** is a portable, prototype assistive device developed in 2023 to help visually impaired individuals navigate their environment and read text more independently. The project was presented at the **Palestine Science & Technology Fair**.

---

### 📖 The Story Behind the Build
This project was built during the early days of the AI revolution, just two months after the release of ChatGPT. While I was a novice to programming at the time, I used a "planning mindset" and AI-assisted development to "vibe code" a functional system that integrates complex computer vision and hardware logic.

### 🛠️ How It Works
The system is built on a **Raspberry Pi 4 Model B** and utilizes a camera mounted on a wearable glove to process the surroundings. Users interact with the device through a physical limit switch that cycles through three distinct operational modes:

* **Text-to-Speech (TTS):** Captures text and reads it aloud to the user.
* **Braille Teaching:** Translates captured text into real-time Braille feedback via six vibration motors on the fingers.
* **Object Detection:** Identifies obstacles and surroundings to assist in navigation.

### 🚀 Technical Features
* **Multilingual Support:** Provides audio feedback in both Arabic and English to guide the user through mode selection.
* **Hardware-Software Integration:** Uses `RPi.GPIO` to handle real-time interrupts from a physical limit switch.
* **Process Orchestration:** Manages multiple Python sub-processes (OpenCV, Tesseract OCR, and TensorFlow) using a master control loop to optimize performance on the Raspberry Pi.

### 📁 Project Structure
* **controlling_scripts.py:** The "brain" of the device that manages mode switching and hardware interrupts.
* **text_to_speech_mode.py:** Handles optical character recognition and audio playback.
* **teaching_braille_mode.py:** Manages the vibration motor array for Braille output.
* **object_detection_mode.py:** Runs the object detection models.

### 🔧 Requirements
* Raspberry Pi 4
* Raspberry Pi Camera Rev 1.3
* 6x Vibration Motors
* **Libraries:** `opencv-python`, `pytesseract`, `tensorflow`, `pygame`, `RPi.GPIO`

---
*Developed as a contribution to assistive technology and a testament to the power of learning by building.*

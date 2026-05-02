# Bright-Vision

### A Smart Wearable for the Visually Impaired 🚀

**Bright Vision** is a portable, prototype assistive device developed in 2023 to help visually impaired individuals navigate their environment and read text more independently[cite: 1, 2]. The project was presented at the **Palestine Science & Technology Fair**[cite: 1].

---

### 📖 The Story Behind the Build
This project was built during the early days of the AI revolution, just two months after the release of ChatGPT[cite: 2]. While I was a novice to programming at the time, I used a "planning mindset" and AI-assisted development to "vibe code" a functional system that integrates complex computer vision and hardware logic[cite: 2].

### 🛠️ How It Works
The system is built on a **Raspberry Pi 4 Model B** and utilizes a camera mounted on a wearable glove to process the surroundings[cite: 1, 2]. Users interact with the device through a physical limit switch that cycles through three distinct operational modes[cite: 2]:

* **Text-to-Speech (TTS):** Captures text and reads it aloud to the user[cite: 1, 2].
* **Braille Teaching:** Translates captured text into real-time Braille feedback via six vibration motors on the fingers[cite: 1, 2].
* **Object Detection:** Identifies obstacles and surroundings to assist in navigation[cite: 1, 2].

### 🚀 Technical Features
* **Multilingual Support:** Provides audio feedback in both Arabic and English to guide the user through mode selection[cite: 1, 2].
* **Hardware-Software Integration:** Uses `RPi.GPIO` to handle real-time interrupts from a physical limit switch[cite: 2].
* **Process Orchestration:** Manages multiple Python sub-processes (OpenCV, Tesseract OCR, and TensorFlow) using a master control loop to optimize performance on the Raspberry Pi[cite: 1, 2].

### 📁 Project Structure
* **controlling_scripts.py:** The "brain" of the device that manages mode switching and hardware interrupts[cite: 2].
* **text_to_speech_mode.py:** Handles optical character recognition and audio playback[cite: 2].
* **teaching_braille_mode.py:** Manages the vibration motor array for Braille output[cite: 2].
* **object_detection_mode.py:** Runs the object detection models[cite: 2].

### 🔧 Requirements
* Raspberry Pi 4[cite: 1]
* Raspberry Pi Camera Rev 1.3[cite: 2]
* 6x Vibration Motors[cite: 2]
* **Libraries:** `opencv-python`, `pytesseract`, `tensorflow`, `pygame`, `RPi.GPIO`[cite: 1, 2]

---
*Developed as a contribution to assistive technology and a testament to the power of learning by building.*[cite: 1]

# 🖥️ System Health Dashboard

A lightweight desktop tool that provides at-a-glance system health stats — ideal for IT support, quick diagnostics, or personal monitoring.  
Built for simplicity, speed, and clarity.

---

## 📌 Features

- **Real-time Metrics**: Monitor CPU, RAM, disk usage, and network activity.
- **Clean UI**: Minimal, distraction-free design using Tkinter.
- **Cross-Platform**: Works on Windows, macOS, and Linux (Python 3.8+).
- **Lightweight**: No heavy dependencies.
- **Extensible**: Easily add more modules (e.g., process monitor, uptime, temperature).

---

## 🚀 Getting Started

1. **Clone the repository**
    
        git clone https://github.com/UzayrManuel/simple-system-health.git
        cd simple-system-health

2. **Install dependencies**
    
        pip install -r requirements.txt

3. **Run the app**
    
        python dashboard.py

---

## 📂 Project structure

        system-health-dashboard/
        │
        ├── dashboard.py        # Main application entry point
        ├── modules/            # Separate modules for metrics (CPU, RAM, etc.)
        ├── assets/             # Icons, images, or style files
        ├── requirements.txt    # Python dependencies
        └── README.md           # You're reading it!

---

## ⚙️ Configuration

- **Config file:** `config.json`
- **Adjustable settings:** refresh rate, theme, monitored metrics
- **Default refresh:** every 2 seconds

---

## 🧪 Requirements

- **Python:** 3.8 or newer
- **OS:** Windows, macOS, or Linux
- **Suggested packages:** `psutil`, `tkinter` (built-in on most platforms)

To install from `requirements.txt`:

        pip install -r requirements.txt

---

## 📈 Future enhancements

- **Dark mode**
- **Threshold alerts** (CPU/memory)
- **Export reports** (CSV, PDF)
- **Process monitor** with quick kill
- **Temperature & fan speed** (where supported)
- **Remote monitoring** (agent + API)

---

## 🤝 Contributing

- **Issues:** Use GitHub Issues to report bugs or request features.
- **PRs:** Open a pull request with a clear description and screenshots if UI changes.
- **Style:** Keep modules small and focused; prefer functions with clear names and docstrings.

---

## 🖼️ Screenshots

Add screenshots to the `assets/` folder and embed them here:

    ![Dashboard Light Mode](assets/screenshot-light.png)
    ![Dashboard Dark Mode](assets/screenshot-dark.png)

---

## 📜 License

This project is licensed under the MIT License — see the `LICENSE` file for details.

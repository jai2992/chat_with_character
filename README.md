# Chat with Character

## 🌟 Overview
**Chat with Character** is an interactive AI-powered chatbot that allows users to engage in immersive conversations with fictional or historical characters. Users can create and customize characters, define their personalities, and chat with them while the AI ensures responses stay true to the character's traits, background, and tone.

## 🚀 Features
- 🏷️ **Create and Save Characters** – Users can define characters with unique names and descriptions.
- 🗣️ **Role-Consistent AI Conversations** – The AI maintains character consistency in responses.
- 📜 **Character Selection** – Choose from previously saved characters to engage in conversations.
- 💾 **Persistent Storage** – Characters are stored in a JSON file for reuse.
- ⚡ **Powered by LLaMA 3.3-70B (Groq API)** – Ensuring intelligent and contextually relevant responses.

## 🎮 How to Use
1. **Install Dependencies:** Ensure you have the required libraries installed.
   ```bash
   pip install streamlit langchain-groq
   ```
2. **Set up API Key:** Store your Groq API key in `secrets.toml` (for security in Streamlit deployment).
3. **Run the App:**
   ```bash
   streamlit run app.py
   ```
4. **Interact:**
   - Create a character with a name and description via the sidebar.
   - Select a character from the dropdown menu.
   - Start chatting and get responses true to the character’s nature.

## 🛠️ Technologies Used
- **Streamlit** – For building the interactive UI.
- **LangChain** – For handling AI-driven conversations.
- **Groq API (LLaMA 3.3-70B)** – For generating character-based responses.
- **JSON** – For storing character profiles.

## 🔥 Future Enhancements
- 🎭 **Voice Interaction** – Enable text-to-speech for character responses.
- 📜 **Conversation History Persistence** – Store past chats for continued discussions.
- 🌍 **Multilingual Support** – Extend conversations beyond English.

## 🤝 Contributing
Feel free to contribute to the project! Fork the repository, submit pull requests, or suggest improvements via issues.

## 📜 License
This project is licensed under the MIT License.

---
✨ *Engage in lifelike AI conversations with your favorite characters today!* ✨


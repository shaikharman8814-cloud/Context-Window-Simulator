# Context Window Simulator

A Python project that simulates how Large Language Models (LLMs) manage conversation history when the context window exceeds the maximum token limit.

This project demonstrates the core backend logic used by AI chat applications such as ChatGPT, Gemini, and Claude to manage conversation memory.

---

## Features

- Store conversation history
- Build a conversation context
- Count tokens using `tiktoken`
- Simulate a maximum context window
- Automatically remove the oldest messages when the token limit is exceeded
- Recalculate the context and token count after each removal

---

## Tech Stack

- Python
- tiktoken

---

## Project Structure

```
Context-Window-Simulator/
│
├── context_window.py
├── requirements.txt
└── README.md
```

---

## How It Works

1. Store conversation messages in a list.
2. Combine all messages into a single context.
3. Convert the context into tokens.
4. Count the total number of tokens.
5. Compare the token count with the maximum context limit.
6. If the limit is exceeded, remove the oldest message.
7. Rebuild the context and recalculate the token count.
8. Repeat until the conversation fits within the context window.

---

## Workflow

```
Messages
    ↓
Build Context
    ↓
Tokenize
    ↓
Count Tokens
    ↓
Token Limit Exceeded?
       │
   Yes │ No
       ↓
Remove Oldest Message
       ↓
Rebuild Context
       ↓
Recalculate Tokens
       ↓
Repeat Until Safe
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Context-Window-Simulator.git
```

Install the required package:

```bash
pip install tiktoken
```

Run the project:

```bash
python context_window.py
```

---

## Learning Objectives

This project helps understand:

- Python Lists
- Loops (`for` and `while`)
- String manipulation
- Tokenization
- Context Windows
- Token Limits
- Conversation Memory
- Backend logic behind LLM chat applications

---

## Future Improvements

- Interactive Gradio interface
- Visual token usage dashboard
- Support for multiple LLM tokenizers
- Conversation memory visualization
- Token cost estimation
- Chat simulation with dynamic user input

---

## License

This project is licensed under the MIT License.

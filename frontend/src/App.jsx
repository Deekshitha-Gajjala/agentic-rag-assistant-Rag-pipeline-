import { useState, useEffect } from "react";
import { FaRobot } from "react-icons/fa";

import Sidebar from "./Sidebar";
import ChatWindow from "./ChatWindow";
import ChatInput from "./ChatInput";

import "./App.css";

function App() {
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const [chats, setChats] = useState([
    {
      title: "New Chat",
      messages: [],
    },
  ]);

  const [currentChat, setCurrentChat] = useState(0);

  // Load saved chats
  useEffect(() => {
    const savedChats = localStorage.getItem("chats");

    if (savedChats) {
      const parsedChats = JSON.parse(savedChats);

      setChats(parsedChats);

      if (parsedChats.length > 0) {
        setCurrentChat(0);
        setMessages(parsedChats[0].messages);
      }
    }
  }, []);

  // Save chats
  useEffect(() => {
    localStorage.setItem(
      "chats",
      JSON.stringify(chats)
    );
  }, [chats]);

  // Create New Chat
  const createNewChat = () => {
    const newChat = {
      title: "New Chat",
      messages: [],
    };

    const updatedChats = [...chats, newChat];

    setChats(updatedChats);
    setCurrentChat(updatedChats.length - 1);
    setMessages([]);
  };

  // Load Existing Chat
  const loadChat = (index) => {
    setCurrentChat(index);
    setMessages(chats[index].messages);
  };

  // Ask Question
  const askQuestion = async () => {
    if (!question.trim()) return;

    const userMessage = {
      sender: "user",
      text: question,
    };

    const tempMessages = [
      ...messages,
      userMessage,
    ];

    setMessages(tempMessages);
    setLoading(true);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/chat",
        {
          method: "POST",
          headers: {
            "Content-Type":
              "application/json",
          },
          body: JSON.stringify({
            question,
            history: tempMessages,
          }),
        }
      );

      const data = await response.json();

      const updatedMessages = [
        ...tempMessages,
        {
          sender: "bot",
          text: data.answer,
        },
      ];

      setMessages(updatedMessages);

      setChats((prevChats) => {
        const copy = [...prevChats];

        copy[currentChat] = {
          title:
            question.length > 30
              ? question.slice(0, 30) + "..."
              : question,
          messages: updatedMessages,
        };

        return copy;
      });
    } catch (error) {
      const updatedMessages = [
        ...tempMessages,
        {
          sender: "bot",
          text: "Unable to connect to backend.",
        },
      ];

      setMessages(updatedMessages);
    }

    setQuestion("");
    setLoading(false);
  };

  return (
    <div className="app">

      <Sidebar
        chats={chats}
        currentChat={currentChat}
        loadChat={loadChat}
        createNewChat={createNewChat}
      />

      <div className="main">

        <div className="header">
          <div className="logo">
            <FaRobot />
            Agentic RAG Assistant
          </div>

          <div className="status">
            <span className="status-dot"></span>
            Online
          </div>
        </div>

        {messages.length === 0 ? (
          <div className="hero-section">

            <h1>
              <FaRobot />
              Agentic RAG Assistant
            </h1>

            <p>
              Upload PDFs, search the web,
              ask questions and chat with AI.
            </p>

            <div className="feature-grid">
              <div className="feature-card">
                📄 PDF Analysis
              </div>

              <div className="feature-card">
                🌐 Web Search
              </div>

              <div className="feature-card">
                🎤 Voice Assistant
              </div>

              <div className="feature-card">
                🧠 RAG Memory
              </div>
            </div>

          </div>
        ) : (
          <ChatWindow
            messages={messages}
            loading={loading}
          />
        )}

        <ChatInput
          question={question}
          setQuestion={setQuestion}
          askQuestion={askQuestion}
        />

      </div>
    </div>
  );
}

export default App;
import { useState } from "react";

import ChatMessage from "./ChatMessage";
import ChatInput from "./ChatInput";

import { sendMessage } from "../services/chatService";


function ChatWindow() {

  const [messages, setMessages] = useState([
    {
      role: "assistant",
      message:
        "Hello! 👋 Welcome to my portfolio. I'm an AI assistant here to help you learn about my skills, projects, education and experience. What would you like to know?",
      sources: [],
    },
  ]);

  const [loading, setLoading] = useState(false);


  const handleSendMessage = async (question) => {

    if (!question.trim() || loading) return;

    // Add user message
    const userMessage = {
      role: "user",
      message: question,
      sources: [],
    };

    setMessages((previous) => [
      ...previous,
      userMessage,
    ]);

    setLoading(true);

    try {

      // Send question to FastAPI
      const response = await sendMessage(question);

      // Add AI response
      const assistantMessage = {
        role: "assistant",
        message: response.answer,
        sources: response.sources || [],
      };

      setMessages((previous) => [
        ...previous,
        assistantMessage,
      ]);

    } catch (error) {

      console.error("Chat error:", error);

      setMessages((previous) => [
        ...previous,
        {
          role: "assistant",
          message:
            "Sorry, something went wrong. Please check your connection and try again.",
          sources: [],
        },
      ]);

    } finally {

      setLoading(false);

    }
  };


  return (
    <section className="chat-container">

      {/* Chat Header */}
      <div className="chat-heading">

        <div className="assistant-avatar">
          AI
        </div>

        <div>
          <h1>Ask me anything</h1>

          <p>
            I'm Pasindu's AI portfolio assistant.
            Ask me about skills, projects, education and experience.
          </p>
        </div>

      </div>


      {/* Chat Messages */}
      <div className="messages-container">

        {messages.map((msg, index) => (

          <ChatMessage
            key={index}
            role={msg.role}
            message={msg.message}
            sources={msg.sources || []}
          />

        ))}


        {/* Loading Indicator */}
        {loading && (
          <div className="loading-message">

            <div className="message-avatar">
              AI
            </div>

            <div className="typing-indicator">
              <span></span>
              <span></span>
              <span></span>
              <small>AI is thinking...</small>
            </div>

          </div>
        )}

      </div>


      {/* Chat Input */}
      <ChatInput
        onSendMessage={handleSendMessage}
        disabled={loading}
      />

    </section>
  );
}

export default ChatWindow;
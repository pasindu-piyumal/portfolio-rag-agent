import { useState } from "react";

function ChatInput({ onSendMessage, disabled }) {

  const [message, setMessage] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();

    const trimmedMessage = message.trim();

    if (!trimmedMessage || disabled) return;

    onSendMessage(trimmedMessage);

    setMessage("");
  };


  return (
    <form
      className="chat-input-container"
      onSubmit={handleSubmit}
    >

      <input
        type="text"
        placeholder="Ask me about my projects, skills, education..."
        value={message}
        onChange={(event) => setMessage(event.target.value)}
        disabled={disabled}
      />

      <button
        type="submit"
        disabled={!message.trim() || disabled}
      >
        <span>{disabled ? "Thinking..." : "Send"}</span>
        <span>➤</span>
      </button>

    </form>
  );
}

export default ChatInput;
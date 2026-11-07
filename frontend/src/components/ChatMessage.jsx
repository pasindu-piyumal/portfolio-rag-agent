function ChatMessage({ role, message, sources = [] }) {
  const isAssistant = role === "assistant";

  return (
    <div
      className={`message-row ${
        isAssistant ? "assistant-row" : "user-row"
      }`}
    >
      {isAssistant && (
        <div className="message-avatar">AI</div>
      )}

      <div className="message-content">

        <div
          className={`message-bubble ${
            isAssistant ? "assistant-bubble" : "user-bubble"
          }`}
        >
          <p>{message}</p>
        </div>

      </div>

      {!isAssistant && (
        <div className="message-avatar user-avatar">
          You
        </div>
      )}
    </div>
  );
}

export default ChatMessage;
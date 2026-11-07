import ChatWindow from "./components/ChatWindow";
import "./App.css";

function App() {
  return (
    <div className="app-container">
      <header className="app-header">
        <div className="brand">
          <div className="brand-icon">P</div>

          <div>
            <h2>Portfolio AI</h2>
            <span>Personal AI Assistant</span>
          </div>
        </div>

        <div className="status">
          <span className="status-dot"></span>
          AI Online
        </div>
      </header>

      <main className="main-content">
        <ChatWindow />
      </main>

      <footer className="app-footer">
        Powered by Gemini 2.5 Flash · Built with RAG
      </footer>
    </div>
  );
}

export default App;
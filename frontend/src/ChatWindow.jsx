import Message from "./Message";

function ChatWindow({
  messages,
  loading,
}) {
  return (
    <div className="chat-window">

      {messages.map(
        (msg, index) => (
          <Message
            key={index}
            msg={msg}
          />
        )
      )}

      {loading && (
        <div className="message bot-message">
          Thinking...
        </div>
      )}

    </div>
  );
}

export default ChatWindow;
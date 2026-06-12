import ReactMarkdown from "react-markdown";

function Message({ msg }) {
  return (
    <div
      className={`message ${
        msg.sender === "user"
          ? "user-message"
          : "bot-message"
      }`}
    >
      {msg.sender === "bot" ? (
        <ReactMarkdown>
          {msg.text}
        </ReactMarkdown>
      ) : (
        msg.text
      )}
    </div>
  );
}

export default Message;